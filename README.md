# Amazon India Sales Analytics Dashboard

## Project Overview

This project analyzes Amazon India sales data from 2015–2025 to uncover revenue trends, customer behavior, product performance, festival sales impact, and operational insights.

The project demonstrates an end-to-end Data Analytics workflow including:

* Data Cleaning & Transformation
* Exploratory Data Analysis (EDA)
* SQL Database Preparation
* Interactive Streamlit Dashboard Development
* Business Insights & Recommendations

---

## Project Objectives

* Analyze revenue growth across years
* Understand customer purchasing behavior
* Evaluate Prime vs Non-Prime customer performance
* Identify top-performing brands and products
* Measure festival sales impact
* Analyze payment methods and delivery performance
* Create an interactive dashboard for business decision-making

---

## Tech Stack

### Programming & Analytics

* Python
* Pandas
* NumPy

### Data Visualization

* Matplotlib
* Seaborn
* Plotly
* Streamlit

### Database

* SQLite
* SQLAlchemy

### Development Environment

* Jupyter Notebook
* Anaconda

---

## Project Structure

Amazon_India_Analytics/

├── dashboard/

│ └── app.py

├── notebooks/

│ ├── 01_data_cleaning.ipynb

│ └── 02_eda_analysis.ipynb

├── sql/

│ └── create_tables.sql

├── reports/

│ └── business_insights.md

├── outputs/

│ └── screenshots/

├── README.md

└── requirements.txt

---

## Data Cleaning Challenges Completed

### Challenge 1 – Missing Value Analysis

* Identified missing values across the dataset
* Validated data quality

### Challenge 2 – Duplicate Record Detection

* Checked duplicate transactions
* Ensured data uniqueness

### Challenge 3 – Date Standardization

* Converted order dates into datetime format
* Extracted year, month, and quarter

### Challenge 4 – Payment Method Standardization

* Standardized payment method names
* Removed inconsistent formatting

### Challenge 5 – Boolean Field Standardization

* Standardized True/False values
* Cleaned Prime membership and festival indicators

### Challenge 6 – Customer City Cleaning

* Corrected city naming inconsistencies

### Challenge 7 – Customer State Cleaning

* Standardized state values

### Challenge 8 – Customer Rating Validation

* Verified rating ranges and quality

### Challenge 9 – Data Type Corrections

* Converted columns to appropriate data types

### Challenge 10 – Export Cleaned Dataset

* Generated cleaned analytical datasets

---

## Exploratory Data Analysis

### Revenue Analytics

* Revenue Trend Analysis (2015–2025)
* Year-over-Year Revenue Growth
* Monthly Revenue Distribution
* Monthly Revenue Heatmap
* Revenue by Category

### Customer Analytics

* Prime vs Non-Prime Revenue
* Average Order Value by Membership
* Revenue by Age Group
* Top Cities by Revenue
* Top States by Revenue
* Customer RFM Analysis

### Product Analytics

* Top Brands by Revenue
* Top Products by Revenue
* Product Rating Analysis
* Price vs Demand Analysis

### Festival Analytics

* Festival Sales Performance
* Seasonal Revenue Trends

### Operations Analytics

* Payment Method Distribution
* Payment Method Evolution
* Return Status Analysis
* Delivery Performance Analysis

---

## Key Business Insights

### Revenue Performance

* Revenue showed consistent growth from 2015 to 2020.
* Peak revenue occurred in 2020.
* Revenue declined after 2020, indicating market changes and increasing competition.

### Customer Insights

* Prime members generated significantly higher revenue than Non-Prime customers.
* Customers aged 26–35 contributed the highest revenue.
* Mumbai, Delhi, Bengaluru, and Chennai emerged as top-performing cities.

### Product Insights

* Samsung, Apple, and OnePlus were among the highest-performing brands.
* Mid-range products generated the highest sales volume.
* Higher-priced products experienced lower demand.

### Festival Insights

* Back-to-School Sale generated the highest revenue.
* Diwali Sale and Amazon Great Indian Festival significantly boosted sales.
* Q4 months delivered the strongest performance.

### Operational Insights

* UPI emerged as the most preferred payment method.
* Most orders were delivered within 2–5 days.
* Return rates remained relatively low.

---

## Dashboard Features

### Executive Summary

* Total Revenue
* Total Orders
* Total Customers
* Average Order Value
* Revenue by Year
* Revenue by Category

### Revenue Analytics

* Monthly Revenue Trends
* Festival Sales Analysis

### Customer Analytics

* Prime vs Non-Prime Revenue
* Revenue by Age Group
* Top Cities by Revenue

### Product Analytics

* Top Brands by Revenue
* Top Products by Revenue

### Operations Analytics

* Payment Method Distribution
* Return Status Analysis
* Delivery Days Distribution

---

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

---

## Dataset

The project uses Amazon India sales transaction data covering the period from 2015–2025.

Due to GitHub file size limitations, the complete raw and processed datasets are not included in this repository. The analysis, notebooks, SQL scripts, dashboard code, and business insights are provided to demonstrate the full analytical workflow.

---

## How to Run

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Launch Dashboard

```bash
streamlit run dashboard/app.py
```

---

## Business Value

This project demonstrates:

* Data Cleaning & Transformation
* Exploratory Data Analysis
* Business Intelligence Reporting
* Customer Analytics
* Product Analytics
* Revenue Forecasting Foundations
* Dashboard Development
* SQL & Database Preparation

---

## Author

**Swetha Dasari**

Power BI Developer | Data Analyst | Python Developer

LinkedIn: [www.linkedin.com/in/swethadasari](http://www.linkedin.com/in/swethadasari)

GitHub: https://github.com/dasariswetha611-design
