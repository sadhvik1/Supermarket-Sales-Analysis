import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Connect to database and load sales data
conn = sqlite3.connect("supermarket_sales.db")
df = pd.read_sql("SELECT Date, SUM(Total_Sales) as Daily_Sales FROM sales_data GROUP BY Date;", conn)
conn.close()

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Convert dates to numerical format (days since the first date)
df['Days'] = (df['Date'] - df['Date'].min()).dt.days

# Prepare data for training
X = df[['Days']]  # Independent variable
y = df['Daily_Sales']  # Dependent variable

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict next 7 days
future_days = np.array(range(df['Days'].max() + 1, df['Days'].max() + 8)).reshape(-1, 1)
future_sales = model.predict(future_days)

# Plot results
plt.figure(figsize=(12, 6))
plt.scatter(df['Days'], df['Daily_Sales'], color='blue', label="Actual Sales")
plt.plot(df['Days'], model.predict(X), color='red', label="Regression Line")
plt.scatter(future_days, future_sales, color='green', label="Predicted Sales", marker='o')
plt.xlabel("Days Since Start")
plt.ylabel("Daily Sales")
plt.title("Supermarket Sales Prediction for Next 7 Days")
plt.legend()
plt.show()

# Print predicted values
print("Predicted Sales for the Next 7 Days:")
for i, sales in enumerate(future_sales):
    print(f"Day {i+1}: ${sales:.2f}")
