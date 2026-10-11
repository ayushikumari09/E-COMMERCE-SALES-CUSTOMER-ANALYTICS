import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/ecommerce_transactions.csv")
# Basic inspection
print("Shape:", df.shape)

print("\nFirst 5 rows:")
print(df.head())

print("\nDataset information:")
print(df.info())

print("\nSummary statistics:")
print(df.describe())

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

# Convert Transaction_Date to datetime
df["Transaction_Date"] = pd.to_datetime(df["Transaction_Date"])

print("\nUpdated data types:")
print(df.dtypes)

# Create date-related columns
df["Year"] = df["Transaction_Date"].dt.year
df["Month"] = df["Transaction_Date"].dt.month
df["Month_Name"] = df["Transaction_Date"].dt.month_name()

print("\nDate columns:")
print(df[["Transaction_Date", "Year", "Month", "Month_Name"]].head())

# Basic Business KPIs

total_revenue = df["Purchase_Amount"].sum()
total_transactions = df["Transaction_ID"].nunique()
average_purchase = df["Purchase_Amount"].mean()
unique_customers = df["User_Name"].nunique()

print("\n--- BUSINESS KPIs ---")
print("Total Revenue:", round(total_revenue, 2))
print("Total Transactions:", total_transactions)
print("Average Purchase Amount:", round(average_purchase, 2))
print("Unique Customers:", unique_customers)

# Revenue by Country

country_analysis = df.groupby("Country").agg(
    Total_Revenue=("Purchase_Amount", "sum"),
    Transactions=("Transaction_ID", "count"),
    Average_Purchase=("Purchase_Amount", "mean")
).sort_values("Total_Revenue", ascending=False)

print("\n--- COUNTRY ANALYSIS ---")
print(country_analysis)

# Product Category Analysis

category_analysis = df.groupby("Product_Category").agg(
    Total_Revenue=("Purchase_Amount", "sum"),
    Transactions=("Transaction_ID", "count"),
    Average_Purchase=("Purchase_Amount", "mean")
).sort_values("Total_Revenue", ascending=False)

print("\n--- PRODUCT CATEGORY ANALYSIS ---")
print(category_analysis)

# Payment Method Analysis

payment_analysis = df.groupby("Payment_Method").agg(
    Total_Revenue=("Purchase_Amount", "sum"),
    Transactions=("Transaction_ID", "count"),
    Average_Purchase=("Purchase_Amount", "mean")
).sort_values("Total_Revenue", ascending=False)

print("\n--- PAYMENT METHOD ANALYSIS ---")
print(payment_analysis)

# Customer Analysis

customer_analysis = df.groupby("User_Name").agg(
    Total_Spending=("Purchase_Amount", "sum"),
    Number_of_Transactions=("Transaction_ID", "count"),
    Average_Purchase=("Purchase_Amount", "mean")
).sort_values("Total_Spending", ascending=False)

print("\n--- TOP 10 CUSTOMERS BY SPENDING ---")
print(customer_analysis.head(10))

# Customer-level averages

avg_customer_spending = customer_analysis["Total_Spending"].mean()
avg_customer_transactions = customer_analysis["Number_of_Transactions"].mean()

print("\n--- CUSTOMER AVERAGES ---")
print("Average Customer Spending:", round(avg_customer_spending, 2))
print("Average Customer Transactions:", round(avg_customer_transactions, 2))

# Create customer segments

def classify_customer(row):
    if row["Total_Spending"] >= avg_customer_spending and row["Number_of_Transactions"] >= avg_customer_transactions:
        return "High Value"
    elif row["Total_Spending"] >= avg_customer_spending:
        return "High Spender"
    elif row["Number_of_Transactions"] >= avg_customer_transactions:
        return "Frequent Buyer"
    else:
        return "Low Engagement"

customer_analysis["Customer_Segment"] = customer_analysis.apply(
    classify_customer, axis=1
)

print("\n--- CUSTOMER SEGMENTS ---")
print(customer_analysis["Customer_Segment"].value_counts())

# Yearly Sales Analysis

yearly_analysis = df.groupby("Year").agg(
    Total_Revenue=("Purchase_Amount", "sum"),
    Transactions=("Transaction_ID", "count"),
    Average_Purchase=("Purchase_Amount", "mean")
).sort_index()

print("\n--- YEARLY SALES ANALYSIS ---")
print(yearly_analysis)


monthly_analysis = df.groupby(["Year", "Month"]).agg(
    Total_Revenue=("Purchase_Amount", "sum"),
    Transactions=("Transaction_ID", "count"),
    Average_Purchase=("Purchase_Amount", "mean")
).reset_index()

print("\n--- MONTHLY SALES ANALYSIS ---")
print(monthly_analysis)

monthly_analysis["Month_Name"] = monthly_analysis["Month"].map(
    dict(enumerate([
        "", "January", "February", "March", "April",
        "May", "June", "July", "August", "September",
        "October", "November", "December"
    ]))
)


# Create age groups
bins = [17, 25, 35, 45, 55, 70]
labels = ["18-25", "26-35", "36-45", "46-55", "56-70"]

df["Age_Group"] = pd.cut(
    df["Age"],
    bins=bins,
    labels=labels
)

age_analysis = df.groupby("Age_Group", observed=True).agg(
    Total_Revenue=("Purchase_Amount", "sum"),
    Transactions=("Transaction_ID", "count"),
    Average_Purchase=("Purchase_Amount", "mean"),
    Unique_Customers=("User_Name", "nunique")
)

print("\n--- AGE GROUP ANALYSIS ---")
print(age_analysis)

country_category_analysis = df.groupby(
    ["Country", "Product_Category"]
).agg(
    Total_Revenue=("Purchase_Amount", "sum"),
    Transactions=("Transaction_ID", "count"),
    Average_Purchase=("Purchase_Amount", "mean")
).sort_values(
    "Total_Revenue",
    ascending=False
)

print("\n--- COUNTRY × CATEGORY ANALYSIS ---")
print(country_category_analysis.head(20))


customer_value = df.groupby("User_Name").agg(
    Total_Spending=("Purchase_Amount", "sum"),
    Number_of_Transactions=("Transaction_ID", "count"),
    Average_Purchase=("Purchase_Amount", "mean")
)

# Calculate percentage contribution to total revenue
customer_value["Revenue_Contribution_%"] = (
    customer_value["Total_Spending"]
    / df["Purchase_Amount"].sum()
) * 100

customer_value = customer_value.sort_values(
    "Total_Spending",
    ascending=False
)

print("\n--- TOP 10 CUSTOMERS BY REVENUE CONTRIBUTION ---")
print(customer_value.head(10))

print("\n--- FINAL DATASET SHAPE ---")
print(df.shape)

print("\n--- FINAL COLUMNS ---")
print(df.columns.tolist())

# Revenue by Year

yearly_analysis["Total_Revenue"].plot(
    kind="bar",
    figsize=(8, 5)
)

plt.title("Revenue by Year")
plt.xlabel("Year")
plt.ylabel("Revenue")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


monthly_trend = df.groupby(
    ["Year", "Month"]
)["Purchase_Amount"].sum().reset_index()

monthly_trend["Period"] = (
    monthly_trend["Year"].astype(str)
    + "-"
    + monthly_trend["Month"].astype(str).str.zfill(2)
)

plt.figure(figsize=(12, 5))

plt.plot(
    monthly_trend["Period"],
    monthly_trend["Purchase_Amount"],
    marker="o"
)

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



category_revenue = (
    df.groupby("Product_Category")["Purchase_Amount"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(9, 5))

category_revenue.plot(kind="bar")

plt.title("Revenue by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


country_revenue = (
    df.groupby("Country")["Purchase_Amount"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(9, 5))

country_revenue.plot(kind="bar")

plt.title("Revenue by Country")
plt.xlabel("Country")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


segment_counts = customer_analysis["Customer_Segment"].value_counts()

plt.figure(figsize=(8, 5))

segment_counts.plot(kind="bar")

plt.title("Customer Segmentation")
plt.xlabel("Customer Segment")
plt.ylabel("Number of Customers")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

# Save cleaned dataset
df.to_csv("data/ecommerce_cleaned.csv", index=False)

print("\nCleaned dataset saved successfully!")
