import pandas as pd
import sqlite3

# 1️⃣ Extract — Load CSV files
employees = pd.read_csv("employees.csv")
orders = pd.read_csv("orders.csv")

# 2️⃣ Transform

# Filter employees older than 27
employees_filtered = employees[employees['age'] > 27]

# Aggregate total order amount per employee
orders_agg = orders.groupby('employee_id')['amount'].sum().reset_index()
orders_agg.rename(columns={'amount':'total_order_amount'}, inplace=True)

# Merge employee data with total orders
df_final = pd.merge(employees_filtered, orders_agg, on='employee_id', how='left')
df_final['total_order_amount'] = df_final['total_order_amount'].fillna(0)

# Optional Enhancement — Add age_group
df_final['age_group'] = df_final['age'].apply(lambda x: 'Young' if x < 30 else 'Senior')

# 3️⃣ Load — Save to SQLite
conn = sqlite3.connect('company.db')
df_final.to_sql('employee_orders', conn, if_exists='replace', index=False)

print("✅ ETL Completed. Data loaded into SQLite database 'company.db'.")

# Optional — Export final table to CSV (for portfolio)
df_final.to_csv("employee_orders_final.csv", index=False)
print("✅ Final table exported to employee_orders_final.csv")