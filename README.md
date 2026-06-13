Amazon India Sales Analytics Dashboard

Project Overview

This project analyzes Amazon India sales data from 2015–2025 to identify sales trends, customer behavior, product performance, and operational insights.

The project includes:

Data Cleaning & Transformation
Exploratory Data Analysis (EDA)
SQL Database Integration
Interactive Streamlit Dashboard
Business Insights & Recommendations
Tech Stack
Programming
Python
Pandas
NumPy
Visualization
Matplotlib
Seaborn
Plotly
Streamlit
Database
SQLite
SQLAlchemy
Project Structure
Amazon_India_Analytics/
│
├── data/
│   ├── raw/
│   ├── cleaned/
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_eda_analysis.ipynb
│
├── sql/
│   ├── create_tables.sql
│
├── dashboard/
│   ├── app.py
│
├── database/
│   ├── amazon_india.db
│
├── reports/
│   ├── business_insights.md
│
├── requirements.txt
└── README.md
Data Cleaning Challenges Completed
Challenge 1

Missing Value Analysis

Challenge 2

Duplicate Record Detection

Challenge 3

Date Standardization

Challenge 4

Payment Method Standardization

Challenge 5

Boolean Field Standardization

Challenge 6

Customer City Cleaning

Challenge 7

Customer State Cleaning

Challenge 8

Customer Rating Validation

Challenge 9

Data Type Corrections

Challenge 10

Export Cleaned Dataset

Exploratory Data Analysis
Revenue Analytics
Revenue Trend (2015–2025)
Revenue Growth Analysis
Monthly Revenue Distribution
Revenue Heatmap
Customer Analytics
Prime vs Non-Prime Revenue
Age Group Revenue Analysis
Top Cities Analysis
Product Analytics
Top Brands by Revenue
Top Products by Revenue
Price vs Demand Analysis
Operations Analytics
Payment Method Distribution
Return Status Analysis
Delivery Days Distribution
Festival Analytics
Festival Sales Performance
Key Business Insights
Revenue Trend

Revenue grew steadily from 2015 and peaked around 2020 before showing a decline in later years.

Customer Segment

Prime customers generated significantly higher revenue and higher average order values.

Geographic Performance

Mumbai, Delhi, Bengaluru and Chennai contributed the highest revenue.

Product Performance

Samsung, Apple and OnePlus emerged as top-performing brands.

Seasonal Trends

December generated the highest revenue, indicating strong holiday season sales.

Festival Sales

Back-to-School and Diwali sales campaigns generated the highest revenues.

## Dashboard Screenshots

### Executive Summary

![Executive Summary](outputs/screenshots/executive_summary.png)

### Revenue Analytics

![Revenue Analytics](outputs/screenshots/revenue_analytics.png)

### Customer Analytics

![Customer Analytics](outputs/screenshots/customer_analytics.png)

### Product Analytics

![Product Analytics](outputs/screenshots/product_analytics.png)

### Operations Analytics

![Operations Analytics](outputs/screenshots/operations_analytics.png)

Dashboard Features
Executive Summary
Total Revenue
Total Orders
Total Customers
Average Order Value
Revenue Analytics
Revenue by Year
Revenue by Category
Monthly Revenue
Customer Analytics
Prime vs Non-Prime Revenue
Revenue by Age Group
Top Cities
Product Analytics
Top Brands
Top Products
Operations Analytics
Payment Methods
Returns
Delivery Performance
How to Run

Install dependencies:

pip install -r requirements.txt

Run dashboard:

streamlit run dashboard/app.py
Author

Swetha Dasari

Power BI Developer | Data Analyst | Python Developer