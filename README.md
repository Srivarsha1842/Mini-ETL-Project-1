Mini ETL Project — Python + SQLite + SQL

This project demonstrates a simple ETL pipeline (Extract → Transform → Load) using Python, Pandas, and SQLite. It is designed as a beginner-friendly data engineering mini project.


Project Goal

Build a mini ETL pipeline:

Extract data from CSV files

Transform the data using Pandas

Load the processed data into SQLite

Run SQL queries on the final table

Dataset
employees.csv

employee_id, employee_name, age, city, salary
1, Ravi, 28, Chennai, 50000
2, Anita, 32, Bangalore, 60000
3, Kiran, 29, Chennai, 55000
4, Meera, 26, Hyderabad, 45000
5, Suresh, 35, Bangalore, 70000

orders.csv

order_id, employee_id, order_date, amount
101, 1, 2024-01-10, 1200
102, 3, 2024-01-12, 800
103, 2, 2024-01-15, 450
104, 1, 2024-01-20, 2200
105, 5, 2024-01-22, 1500

ETL Pipeline Overview
1. Extract

Read CSV files using Pandas.

2. Transform

Filter employees older than 27

Aggregate total order amount per employee

Merge employee details with order totals

Add "age_group" column

Fill missing total order values with 0

3. Load

Load the final processed data into SQLite (company.db)

Export the output as employee_orders_final.csv

SQL Queries Used
1. List all employees with total orders
SELECT * FROM employee_orders;

2. Employees with total order amount > 1000
SELECT * FROM employee_orders WHERE total_order_amount > 1000;

3. Sort employees by highest total order amount
SELECT * FROM employee_orders ORDER BY total_order_amount DESC;

4. Top employee by order amount
SELECT employee_name, salary, total_order_amount
FROM employee_orders
ORDER BY total_order_amount DESC
LIMIT 1;

Output Files

employee_orders_final.csv

company.db (SQLite database)

Skills Demonstrated

Python ETL (Extract → Transform → Load)

Pandas data manipulation

SQLite database loading

SQL querying

Data aggregation & joining

Building a portfolio-ready mini project

How to Run

Clone the repository

Run the script:

python etl_script.py


Open company.db using any SQLite viewer

Execute the SQL queries above
