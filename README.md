# E-Commerce Sales & Customer Analysis

End-to-end analysis of 50,000 e-commerce transactions (₹25.16M revenue,
9 Mar 2023 – 8 Mar 2025) using Python, SQL and Power BI.


## Project Overview
This project takes a public e-commerce dataset from raw data to a finished
dashboard. The data was cleaned and prepared in Python, analyzed with SQL,
and presented in an interactive Power BI report.

## Tools Used
- Python (pandas): data cleaning and preparation
- SQL: aggregation and analysis queries
- Power BI (DAX): dashboard and reporting

## Dataset
- Source: [add dataset link here]
- Size: 50,000 transactions, 100 distinct user names
- Coverage: 10 countries, 8 product categories, 6 payment methods
- Columns: Transaction_ID, User_Name, Age, Country, Product_Category,
  Purchase_Amount, Payment_Method, Transaction_Date, Year, Month,
  Month_Name, Age_Group

## Workflow
1. Data preparation (Python): cleaned and prepared the dataset and
   created Year, Month, Month_Name and Age_Group columns.
2. Analysis (SQL): queried revenue by country, product category and
   payment method, the monthly trend, and top customers.
3. Dashboard (Power BI): built KPI cards, a monthly revenue trend,
   breakdown charts, a customer segment donut, a Top 10 customers table,
   and a country × product category heatmap matrix.

## Dashboard Contents
- KPI cards: total revenue, total transactions, unique customers,
  average purchase
- Monthly revenue trend
- Revenue by country
- Revenue by product category
- Revenue by payment method
- Customer segment distribution (by age group)
- Top 10 customers by spending
- Country × product category matrix

## Key Findings
- Revenue is spread evenly across markets. All 10 countries fall between
  ₹2.47M and ₹2.55M (about 10% each). France is first and the UK is last.
- Monthly revenue is stable at roughly ₹1.05M, with no strong growth
  or seasonality.
- Product categories are close together. Shares range from 12.2%
  (Beauty) to 12.7% (Sports).
- Payment methods are nearly equal, each between 16% and 17% of revenue.
  Cash on Delivery is slightly ahead on revenue, and UPI has the most
  transactions.
- The 56-70 age group has the largest share (28% of transactions),
  partly because it covers a wider age range than the other groups.
- Average purchase is ₹503.16, and it varies very little between
  payment methods (₹497 to ₹507).

## Data Notes and Limitations
- The first and last months are partial (data starts on 9 Mar 2023 and
  ends on 8 Mar 2025), so they show lower revenue.
- `User_Name` is not a unique customer ID, so "unique customers" means
  distinct names.
- The data appears synthetic, which explains why results are so uniform.

## Repository Structure
```
├── data/        cleaned dataset
├── python/      cleaning and preparation notebook
├── sql/         analysis queries
├── powerbi/     dashboard file (.pbix)
└── images/      dashboard screenshots
```

## How to Use
1. Open the notebook in `python/` to see the data preparation steps.
2. Run the queries in `sql/` against the cleaned dataset.
3. Open the `.pbix` file in Power BI Desktop to explore the dashboard.

## Author
[Ayushi Kumar] | [www.linkedin.com/in/ayushi-kumari-880134286] | 
