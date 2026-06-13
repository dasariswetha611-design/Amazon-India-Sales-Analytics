CREATE TABLE products (
    product_id VARCHAR(50) PRIMARY KEY,
    product_name VARCHAR(255),
    category VARCHAR(100),
    subcategory VARCHAR(100),
    brand VARCHAR(100)
);

CREATE TABLE customers (
    customer_id VARCHAR(50) PRIMARY KEY,
    customer_city VARCHAR(100),
    customer_state VARCHAR(100),
    customer_age_group VARCHAR(50),
    customer_spending_tier VARCHAR(50)
);

CREATE TABLE transactions (
    transaction_id VARCHAR(50) PRIMARY KEY,
    customer_id VARCHAR(50),
    product_id VARCHAR(50),
    order_date DATE,
    quantity INT,
    final_amount_inr FLOAT,
    payment_method VARCHAR(50)
);

CREATE TABLE time_dimension (
    order_date DATE PRIMARY KEY,
    year INT,
    month INT,
    quarter INT,
    day INT
);