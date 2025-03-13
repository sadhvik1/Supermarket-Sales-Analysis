import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to SQLite database
conn = sqlite3.connect("supermarket_sales.db")

# Load data into a Pandas DataFrame
df = pd.read_sql("SELECT * FROM sales_data;", conn)

# Close connection
conn.close()

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Set Seaborn style
sns.set_style("whitegrid")

# --- Visualization 1: Total Sales by Product Line ---
plt.figure(figsize=(10, 5))
sns.barplot(x=df['Product line'], y=df['Total_Sales'], estimator=sum, ci=None, palette="viridis")
plt.xticks(rotation=45)
plt.title("Total Sales by Product Line")
plt.xlabel("Product Line")
plt.ylabel("Total Sales")
plt.show()

# --- Visualization 2: Daily Sales Trend ---
plt.figure(figsize=(12, 6))
df.groupby('Date')['Total_Sales'].sum().plot(marker='o', linestyle='-', color='b')
plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.grid()
plt.show()

# --- Visualization 3: Sales Distribution by Payment Method ---
plt.figure(figsize=(8, 4))
sns.countplot(x=df["Payment"], palette="coolwarm")
plt.title("Sales Distribution by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Count")
plt.show()

# Extract hour from the 'Time' column
df['Hour'] = pd.to_datetime(df['Time']).dt.hour

# --- Visualization 4: Peak Sales Hours ---
plt.figure(figsize=(10, 5))
sns.barplot(x=df['Hour'], y=df['Total_Sales'], estimator=sum, ci=None, palette="magma")
plt.xticks(rotation=0)
plt.title("Peak Sales Hours")
plt.xlabel("Hour of the Day")
plt.ylabel("Total Sales")
plt.show()

# Connect to the database
conn = sqlite3.connect("supermarket_sales.db")

# Query top 5 selling products by total sales
query = """
SELECT "Product line", SUM(Total_Sales) AS total_revenue
FROM sales_data
GROUP BY "Product line"
ORDER BY total_revenue DESC
LIMIT 5;
"""

# Run query and store results in Pandas
df = pd.read_sql(query, conn)

# Close database connection
conn.close()

# Display results
print("Top 5 Best-Selling Product Lines:")
print(df)