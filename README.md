# 📊 Enterprise Retail Data Warehouse & Power BI Analytics Solution

A comprehensive, end-to-end Enterprise Business Intelligence (BI) and Data Engineering project built on a **12-table relational retail data warehouse dataset containing over 1 Million+ transaction rows**.

This repository documents the entire enterprise analytics lifecycle—from relational data modeling (ERD), ETL pipeline engineering (Python & SQL), DAX metric calculations, Software Quality Assurance (SQA) verification, to a 7-page executive Power BI dashboard.

---

## 🖼️ Executive Dashboard Preview

Below is the primary **Executive Overview** dashboard summarizing core enterprise financial KPIs, sales trajectories, and regional revenue shares:

![Executive Overview Dashboard](images/executive_overview.png)

---

## 🏗️ End-to-End Project Workflow

```text
[Raw Relational Dataset (12 Tables)]
                 │
                 ▼
[Data Modeling & ER Diagramming (Draw.io)]
                 │
                 ▼
[ETL & Query Optimization (PostgreSQL / SQLite)]
                 │
                 ▼
[Python Data Processing & Audit (pandas, NumPy)]
                 │
                 ▼
[Power BI Modeling & DAX Calculation Engine]
                 │
                 ▼
[SQA & Metric Verification Scripts]
                 │
                 ▼
[7-Page Power BI Executive Dashboard]


📌 Complete Project Lifecycle Breakdown
1. Data Architecture & Relational Modeling
Data Scale: 1M+ rows across 12 normalized relational entities designed in a star/snowflake schema.

Core Entities: Fact_Sales, Dim_Customer, Dim_Product, Dim_Store, Dim_Category, Dim_Date, Dim_Payment, Dim_Supplier, Dim_Geography, Dim_Shipping, Dim_Order, and Dim_Promotion.

Referential Integrity: Mapped Primary Keys (PK) and Foreign Keys (FK) using Draw.io to prevent orphan records during transactional aggregation.

2. ETL Pipelines & SQL Optimization
SQL Querying: Standardized relational join strategies, group-by aggregations, and window functions to query revenue and inventory trends across database nodes.

Python ETL (pandas, NumPy, openpyxl): Automated data cleansing pipelines, missing value imputation, transaction formatting, and pre-visualization anomaly detection.

3. Power BI Modeling & DAX Metric Engine
Power Query (M-Code): Transformed raw database schemas, standardized data types, and generated a custom 5-year calendar dimension table.

Key Calculated DAX Measures:

Total Revenue: SUM(Fact_Sales[Revenue]) ($4.00 Billion)

Total Net Profit: SUM(Fact_Sales[Profit]) ($1.15 Billion)

Profit Margin %: DIVIDE([Total Profit], [Total Revenue], 0) (30.0%)

Average Order Value (AOV): DIVIDE([Total Revenue], [Total Orders], 0) ($12.76K)

Customer Purchase Frequency: DIVIDE([Total Orders], [Total Customers], 0) (6.00)

4. Software Quality Assurance (SQA) & Data Auditing
Validation Scripts: Built custom Python verification scripts to cross-check Power BI measure aggregates against raw SQLite query totals.

Dashboard Testing: Performed filter-context sanity checks, dynamic slicer responsiveness testing, and spatial UI validation across all report pages.

5. Multi-Page Power BI Analytics Breakdown
The Power BI report workbook features 7 specialized analytical pages:

Executive Overview (Page 1): Strategic cockpit tracking $4B Revenue, $1.15B Profit, 300K Orders, regional market shares (Mumbai leading at 31.09%), and 5-year revenue trends.

Sales & Revenue Analysis (Page 2): In-depth transaction breakdown across payment modes (Payment ID 299998 leading at 35.65%), order volume trajectories, and category sales splits.

Customer Insights (Page 3): CRM analytics covering 50K registered accounts, customer acquisition trends (2019–2024), VIP high-value segment rankings ($150K+ spenders), and city customer density.

Product Performance (Page 4): Catalog-level inventory analytics tracking 2M units sold, SKU-level margins (30%), discount vs. sales correlations, and category profit contributions ($233.68M top group).

Store & Regional Operations (Page 5): Physical retail footprint evaluation across 100 store outlets ($38.28M average sales/store), city net profits, and spatial GIS mapping across Indian commercial hubs.

Logistics & Order Fulfillment (Page 6): Supply chain monitoring evaluating 300K shipments, delivery completion rates (33% delivered, 33% late, 33% in-transit), return volumes (30K returned orders), and regional courier throughput.

Supplier & Category Analytics (Page 7): Vendor management evaluating 200 suppliers ($19.14M avg revenue/vendor), 30 product categories, procurement lead times, and category return distribution.

📈 Key Enterprise Impact & Performance Metrics
Total Enterprise Revenue: $4.00 Billion

Total Net Profit: $1.15 Billion (Consistent 30% Profit Margin)

Order Processing Volume: 300,000+ Unique Transactions (AOV: $12.76K)

Customer Base: 50,000 Active Accounts (6.0 Orders/Customer)

Inventory Units Sold: 2.0 Million Physical Units

Retail Outlet Footprint: 100 Physical Stores across 4 major Indian metros (Mumbai, Pune, Delhi, Bangalore)

🛠️ Complete Technology Stack
Database & Querying: PostgreSQL, SQLite, Draw.io (Data Architecture & Schema Design)

Data Engineering & ETL: Python (pandas, NumPy, openpyxl, Matplotlib, Seaborn)

Business Intelligence: Microsoft Power BI Desktop, Power Query (M-Code), DAX

Quality Assurance: Data Verification Scripts, Boundary Condition & Defect Testing

📂 Project Repository Structure
├── README.md
├── docs/
│   ├── Architecture_ERD_Diagram.png
│   └── SQA_Data_Verification_Report.pdf
├── scripts/
│   ├── etl_data_processing.py
│   └── sql_kpi_verification.sql
├── Retail_Enterprise_Analytics.pbix
└── images/
    └── executive_overview.png
