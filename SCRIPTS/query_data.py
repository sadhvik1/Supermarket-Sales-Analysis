import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect("supermarket_sales.db")

# Query the first 5 rows from the sales_data table
df = pd.read_sql("SELECT * FROM sales_data LIMIT 10;", conn)

# Display the queried data
print(df)

# Close the database connection
conn.close()
