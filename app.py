import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Amazon India Analytics",
    layout="wide"
)

df = pd.read_csv("../data/cleaned/cleaned_transactions.csv")

st.title("🛒 Amazon India Sales Analytics Dashboard")

page = st.sidebar.radio(
    "Select Dashboard Page",
    [
        "Executive Summary",
        "Revenue Analytics",
        "Customer Analytics",
        "Product Analytics",
        "Operations Analytics"
    ]
)

total_revenue = df["final_amount_inr"].sum()
total_orders = df["transaction_id"].count()
total_customers = df["customer_id"].nunique()
aov = total_revenue / total_orders

if page == "Executive Summary":
    st.header("Executive Summary")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Revenue", f"₹{total_revenue:,.0f}")
    c2.metric("Total Orders", f"{total_orders:,}")
    c3.metric("Total Customers", f"{total_customers:,}")
    c4.metric("Average Order Value", f"₹{aov:,.0f}")

    st.subheader("Revenue by Year")
    yearly = df.groupby("order_year")["final_amount_inr"].sum()
    st.bar_chart(yearly)

    st.subheader("Revenue by Category")
    category = df.groupby("category")["final_amount_inr"].sum()
    st.bar_chart(category)

elif page == "Revenue Analytics":
    st.header("Revenue Analytics")

    monthly = df.groupby("order_month")["final_amount_inr"].sum()
    st.subheader("Monthly Revenue")
    st.bar_chart(monthly)

    festival = df.groupby("festival_name")["final_amount_inr"].sum()
    st.subheader("Festival Sales")
    st.bar_chart(festival)

elif page == "Customer Analytics":
    st.header("Customer Analytics")

    prime = df.groupby("is_prime_member")["final_amount_inr"].sum()
    st.subheader("Prime vs Non-Prime Revenue")
    st.bar_chart(prime)

    age = df.groupby("customer_age_group")["final_amount_inr"].sum()
    st.subheader("Revenue by Age Group")
    st.bar_chart(age)

    city = df.groupby("customer_city")["final_amount_inr"].sum().sort_values(ascending=False).head(10)
    st.subheader("Top 10 Cities by Revenue")
    st.bar_chart(city)

elif page == "Product Analytics":
    st.header("Product Analytics")

    brand = df.groupby("brand")["final_amount_inr"].sum().sort_values(ascending=False).head(10)
    st.subheader("Top Brands by Revenue")
    st.bar_chart(brand)

    products = df.groupby("product_name")["final_amount_inr"].sum().sort_values(ascending=False).head(10)
    st.subheader("Top Products by Revenue")
    st.bar_chart(products)

elif page == "Operations Analytics":
    st.header("Operations Analytics")

    payment = df["payment_method"].value_counts()
    st.subheader("Payment Method Distribution")
    st.bar_chart(payment)

    returns = df["return_status"].value_counts()
    st.subheader("Return Status")
    st.bar_chart(returns)

    delivery = df.groupby("delivery_days")["transaction_id"].count()
    st.subheader("Delivery Days Distribution")
    st.bar_chart(delivery)