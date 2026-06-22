# E-commerce Sales Analysis Project

Description of the project. 

Analysis of the dataset of the Brazilian e-commerce platform, Olist. 
The objective is to create a visualization of the top 10 states based on order volume, payment methods, and order status with the use of Python and SQL. 

The development of the database creation, writing SQL queries and visualization of the data. 

#Goals

Using SQLite to load and structure your data. 

Analyze the data using SQL
Present using Python
Construct a full data analysis pipeline 

#Tools Used

Python 
Pandas 
SQLite3 
Matplotlib 
Jupyter Notebooks 
SQL 

#Project Structure

olist-ecommerce-analysis/

data/Raw dataset (CSV files)

notebooks/Jupyter analysis notebook

src/Data loading scripts

visuals/Generated graphs

olist.db - SQLite database

README.md


Description of Project Stages: 


#. Data Loading: 
CSV files were uploaded into SQLite databases using Python (pandas)

#. database build: 
A relational database was produced using SQLite which is titled “olist.db” with the lists below displaying the tables used that comprise this relational database. 
Customers, Orders, Order Items, Products, Payments, Reviews 


#. SQL Analysis. 
SQL Queries were developed to examine: order status distributions, customer distributions by state and payment methods. 


#. Data Visualisation: 
The Matplotlib bar chart was generated to graphically represent: Top states by order volume, Payment method distribution, Order status distribution. 


Key Findings: 
A majority of orders come in from a few states
Credit cards account for most of the payment method used
pretty much all of the orders have made it to their destinations, but there was some delay in operations and there were some orders that are still awaiting completion

#How to Run

1. Clone repository

2. Install dependencies: pip install pandas matplotlib jupyter

3. Run data loader: python src/load_data.py

4. Open Jupyter Notebook:
