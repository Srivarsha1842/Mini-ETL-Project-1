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
orders.csv


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



How to Run

Clone the repository

Run the script:

python etl_script.py


Open company.db using any SQLite viewer

Execute the SQL queries above
