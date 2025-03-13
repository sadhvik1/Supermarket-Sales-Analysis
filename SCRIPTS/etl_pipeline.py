import pandas as pd
import sqlite3

# Define file path
file_path = r"C:\Users\Sadhvik\OneDrive\Desktop\study\PROJECT\archive\SuperMarket Analysis.csv"

def etl_pipeline(file_path):
    # Load Data
    df = pd.read_csv(file_path)

    # Data Cleaning & Transformation
    df['Date'] = pd.to_datetime(df['Date'])
    df['Total_Sales'] = df['Unit price'] * df['Quantity']
    df.drop(columns=['Invoice ID'], inplace=True, errors='ignore')

    # Store in SQLite
    conn = sqlite3.connect("supermarket_sales.db")
    df.to_sql("sales_data", conn, if_exists="replace", index=False)
    conn.close()

    print("ETL Process Completed Successfully!")

# Run the pipeline
etl_pipeline(file_path)