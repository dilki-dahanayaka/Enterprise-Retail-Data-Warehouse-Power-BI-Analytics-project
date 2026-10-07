import pandas as pd
import os

input_folder = "./cleaned_output"

def load_and_standardize(file_name):
    path = os.path.join(input_folder, file_name)
    if os.path.exists(path):
        df = pd.read_csv(path)
        df.columns = df.columns.str.lower().str.strip()
        return df
    else:
        return pd.DataFrame()

# Load Cleaned Tables
orders = load_and_standardize("Orders.csv")
order_items = load_and_standardize("Order_Items.csv")
products = load_and_standardize("Products.csv")
customers = load_and_standardize("Customers.csv")
stores = load_and_standardize("Stores.csv")
returns = load_and_standardize("Returns.csv")
employees = load_and_standardize("Employees.csv")
suppliers = load_and_standardize("Suppliers.csv")
shipments = load_and_standardize("Shipments.csv")
categories = load_and_standardize("Categories.csv")
promotions = load_and_standardize("Promotions.csv")

print("--- PYTHON KPI VERIFICATION OUTPUT (PAGES 1 - 7) ---")

if not order_items.empty and not products.empty:
    # Merge order_items with products
    df_sales = order_items.merge(products, on="product_id", how="left")

    # Helper function to find matching column safely
    def find_col(possible_names, df):
        for name in possible_names:
            if name in df.columns:
                return name
        for col in df.columns:
            for name in possible_names:
                if col.startswith(name):
                    return col
        return None

    # Dynamically locate columns present in df_sales
    qty_col = find_col(['quantity', 'qty'], df_sales)
    price_col = find_col(['unit_price', 'price'], df_sales)
    cost_col = find_col(['unit_cost', 'cost'], df_sales)
    disc_col = find_col(['discount', 'discount_rate', 'disc'], df_sales)

    # Clean & Convert columns safely
    df_sales['qty_clean'] = pd.to_numeric(df_sales[qty_col], errors='coerce').fillna(1) if qty_col else 1
    df_sales['price_clean'] = pd.to_numeric(df_sales[price_col], errors='coerce').fillna(0) if price_col else 0
    df_sales['cost_clean'] = pd.to_numeric(df_sales[cost_col], errors='coerce').fillna(0) if cost_col else 0
    
    # Check discount in df_sales
    if disc_col:
        df_sales['disc_clean'] = pd.to_numeric(df_sales[disc_col], errors='coerce').fillna(0)
    else:
        df_sales['disc_clean'] = 0

    # Calculate Total Discounts
    # If discount values are like 5, 10 instead of 0.05, 0.10, convert percentage
    if df_sales['disc_clean'].max() > 1.0:
        df_sales['disc_clean'] = df_sales['disc_clean'] / 100.0

    df_sales['discount_amount'] = df_sales['qty_clean'] * df_sales['price_clean'] * df_sales['disc_clean']
    df_sales['revenue'] = (df_sales['qty_clean'] * df_sales['price_clean']) - df_sales['discount_amount']
    df_sales['cost'] = df_sales['qty_clean'] * df_sales['cost_clean']
    df_sales['profit'] = df_sales['revenue'] - df_sales['cost']
else:
    df_sales = pd.DataFrame()

# PAGE 1: EXECUTIVE OVERVIEW
tot_rev = df_sales['revenue'].sum() if not df_sales.empty else 0
tot_orders = orders['order_id'].nunique() if not orders.empty else 0
gross_prof = df_sales['profit'].sum() if not df_sales.empty else 0
aov = tot_rev / tot_orders if tot_orders > 0 else 0

print(f"\n[PAGE 1: EXECUTIVE OVERVIEW]")
print(f"1. Total Revenue: ${tot_rev:,.2f}")
print(f"2. Total Orders: {tot_orders:,}")
print(f"3. Gross Profit: ${gross_prof:,.2f}")
print(f"4. Average Order Value (AOV): ${aov:,.2f}")

# PAGE 2: SALES & REVENUE ANALYSIS
tot_discount = df_sales['discount_amount'].sum() if not df_sales.empty else 0

# If no discount in order_items, check if discount exists in promotions table
if tot_discount == 0 and not promotions.empty:
    disc_promo_col = find_col(['discount_percent', 'discount', 'discount_rate'], promotions)
    if disc_promo_col and not orders.empty and 'promotion_id' in orders.columns:
        orders_promo = orders.merge(promotions, on='promotion_id', how='inner')
        if not orders_promo.empty and disc_promo_col in orders_promo.columns:
            # Estimate discount from promo
            promo_disc_rate = pd.to_numeric(orders_promo[disc_promo_col], errors='coerce').fillna(0)
            if promo_disc_rate.max() > 1.0:
                promo_disc_rate = promo_disc_rate / 100.0
            tot_discount = (tot_rev * promo_disc_rate.mean())

print(f"\n[PAGE 2: SALES & REVENUE ANALYSIS]")
print(f"1. Total Discounts Given: ${tot_discount:,.2f}")

# PAGE 3: CUSTOMER INSIGHTS
tot_cust = customers['customer_id'].nunique() if not customers.empty else 0
print(f"\n[PAGE 3: CUSTOMER INSIGHTS]")
print(f"1. Total Unique Customers: {tot_cust:,}")

# PAGE 4: PRODUCT PERFORMANCE
tot_units = df_sales['qty_clean'].sum() if not df_sales.empty else 0
tot_ret = returns['return_id'].nunique() if not returns.empty else 0
ret_rate = (tot_ret / tot_units) * 100 if tot_units > 0 else 0

print(f"\n[PAGE 4: PRODUCT PERFORMANCE]")
print(f"1. Total Units Sold: {int(tot_units):,}")
print(f"2. Total Returns Count: {tot_ret:,}")
print(f"3. Return Rate: {ret_rate:.2f}%")

# PAGE 5: STORE & REGIONAL OPERATIONS
tot_emp = employees['employee_id'].nunique() if not employees.empty else 1
sales_per_emp = tot_rev / tot_emp

print(f"\n[PAGE 5: STORE & REGIONAL OPERATIONS]")
print(f"1. Active Employees: {tot_emp:,}")
print(f"2. Sales per Employee: ${sales_per_emp:,.2f}")

# PAGE 6: LOGISTICS & ORDER FULFILLMENT
tot_shipments = shipments['shipment_id'].nunique() if not shipments.empty else 0
print(f"\n[PAGE 6: LOGISTICS & ORDER FULFILLMENT]")
print(f"1. Total Shipments Tracked: {tot_shipments:,}")

# PAGE 7: SUPPLIER & CATEGORY ANALYTICS
tot_supp = suppliers['supplier_id'].nunique() if not suppliers.empty else 0
tot_cat = categories['category_id'].nunique() if not categories.empty else 0
print(f"\n[PAGE 7: SUPPLIER & CATEGORY ANALYTICS]")
print(f"1. Total Suppliers: {tot_supp:,}")
print(f"2. Total Product Categories: {tot_cat:,}")
