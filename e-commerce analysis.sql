CREATE DATABASE EcommerceAnalytics;
GO

USE EcommerceAnalytics;
GO

CREATE TABLE EcommerceTransactions (
    Transaction_ID INT,
    User_Name VARCHAR(100),
    Age INT,
    Country VARCHAR(50),
    Product_Category VARCHAR(50),
    Purchase_Amount DECIMAL(10,2),
    Payment_Method VARCHAR(50),
    Transaction_Date DATE,
    Year INT,
    Month INT,
    Month_Name VARCHAR(20),
    Age_Group VARCHAR(20)
);

USE EcommerceAnalytics;
GO

SELECT DB_NAME() AS CurrentDatabase;

USE EcommerceAnalytics;
GO

SELECT COUNT(*) AS Total_Rows
FROM dbo.EcommerceTransactions;

SELECT TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_TYPE = 'BASE TABLE';

SELECT COUNT(*) AS Total_Rows
FROM ecommerce_cleaned;

SELECT TOP 10 *
FROM ecommerce_cleaned;

SELECT 
    COUNT(*) AS Total_Rows
FROM ecommerce_cleaned;

-- 1. Overall Business KPIs

SELECT
    COUNT(*) AS Total_Transactions,
    SUM(Purchase_Amount) AS Total_Revenue,
    AVG(Purchase_Amount) AS Average_Purchase,
    COUNT(DISTINCT User_Name) AS Unique_Customers
FROM ecommerce_cleaned;

-- 2. Revenue by Country

SELECT
    Country,
    SUM(Purchase_Amount) AS Total_Revenue,
    COUNT(*) AS Transactions,
    AVG(Purchase_Amount) AS Average_Purchase
FROM ecommerce_cleaned
GROUP BY Country
ORDER BY Total_Revenue DESC;

-- 3. Revenue by Product Category

SELECT
    Product_Category,
    SUM(Purchase_Amount) AS Total_Revenue,
    COUNT(*) AS Transactions,
    AVG(Purchase_Amount) AS Average_Purchase
FROM ecommerce_cleaned
GROUP BY Product_Category
ORDER BY Total_Revenue DESC;

-- 4. Payment Method Analysis

SELECT
    Payment_Method,
    SUM(Purchase_Amount) AS Total_Revenue,
    COUNT(*) AS Transactions,
    AVG(Purchase_Amount) AS Average_Purchase
FROM ecommerce_cleaned
GROUP BY Payment_Method
ORDER BY Total_Revenue DESC;

-- 5. Yearly Revenue

SELECT
    Year,
    SUM(Purchase_Amount) AS Total_Revenue,
    COUNT(*) AS Transactions,
    AVG(Purchase_Amount) AS Average_Purchase
FROM ecommerce_cleaned
GROUP BY Year
ORDER BY Year;

-- 6. Monthly Revenue

SELECT
    Year,
    Month,
    Month_Name,
    SUM(Purchase_Amount) AS Total_Revenue,
    COUNT(*) AS Transactions
FROM ecommerce_cleaned
GROUP BY Year, Month, Month_Name
ORDER BY Year, Month;

-- 7. Age Group Analysis

SELECT
    Age_Group,
    SUM(Purchase_Amount) AS Total_Revenue,
    COUNT(*) AS Transactions,
    AVG(Purchase_Amount) AS Average_Purchase,
    COUNT(DISTINCT User_Name) AS Unique_Customers
FROM ecommerce_cleaned
GROUP BY Age_Group
ORDER BY Total_Revenue DESC;

-- 8. Top 10 Customers by Spending

SELECT TOP 10
    User_Name,
    SUM(Purchase_Amount) AS Total_Spending,
    COUNT(*) AS Number_of_Transactions,
    AVG(Purchase_Amount) AS Average_Purchase
FROM ecommerce_cleaned
GROUP BY User_Name
ORDER BY Total_Spending DESC;