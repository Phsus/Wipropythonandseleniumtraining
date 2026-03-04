import mysql.connector
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# db connection
db_conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sushh@586"
)
cursor = db_conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS company_db")
db_conn.close()

# connect to company_db
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sushh@586",
    database="company_db"
)
cursor = connection.cursor()


cursor.execute("DROP TABLE IF EXISTS retail_sales")
cursor.execute("""
    CREATE TABLE retail_sales (
        OrderID INT,
        Date DATE,
        Region VARCHAR(50),
        Product VARCHAR(50),
        Category VARCHAR(50),
        Quantity INT,
        Price INT
    )
""")

# dummy data
dates = pd.date_range(start="2023-01-01", periods=50, freq="W").strftime('%Y-%m-%d').tolist()
regions = np.random.choice(["North", "South", "East", "West"], 50)
products = np.random.choice(["Laptop", "Mouse", "Keyboard", "Monitor", "Desk"], 50)
categories = np.random.choice(["Electronics", "Accessories", "Furniture"], 50)
quantities = np.random.randint(1, 15, 50)
prices = np.random.randint(20, 1000, 50)


sales_data = []
for i in range(50):
    sales_data.append((
        1001 + i, dates[i], regions[i], products[i],
        categories[i], int(quantities[i]), int(prices[i])
    ))


sql = "INSERT INTO retail_sales (OrderID, Date, Region, Product, Category, Quantity, Price) VALUES (%s, %s, %s, %s, %s, %s, %s)"
cursor.executemany(sql, sales_data)
connection.commit()

# fetch back from db
cursor.execute("SELECT * FROM retail_sales")
rows = cursor.fetchall()
columns = cursor.column_names

df = pd.DataFrame(rows, columns=columns)


cursor.close()
connection.close()


df['Date'] = pd.to_datetime(df['Date'])
df['Revenue'] = df['Quantity'] * df['Price']

print("Retail Analysis")
print("Highest Revenue Region:", df.groupby('Region')['Revenue'].sum().idxmax())


df['Month'] = df['Date'].dt.to_period('M')
monthly_trend = df.groupby('Month')['Revenue'].sum()
print("\nMonthly Sales Trend:\n", monthly_trend)

print("\nBest Performing Category:", df.groupby('Category')['Revenue'].sum().idxmax())

top_5_products = df.groupby('Product')['Revenue'].sum().nlargest(5)
print("\nTop 5 Products:\n", top_5_products)

#  charts
plt.figure(figsize=(8, 5))
df.groupby('Region')['Revenue'].sum().plot(kind='bar', color='skyblue')
plt.title('Revenue by Region')
plt.xlabel('Region')
plt.ylabel('Revenue')
plt.show()

plt.figure(figsize=(8, 5))
monthly_trend.plot(kind='line', marker='o', color='green')
plt.title('Monthly Revenue Trend')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.show()

plt.figure(figsize=(8, 8))
df.groupby('Category')['Revenue'].sum().plot(kind='pie', autopct='%1.1f%%')
plt.title('Category Contribution')
plt.ylabel('')
plt.show()

plt.figure(figsize=(8, 5))
top_5_products.sort_values().plot(kind='barh', color='orange')
plt.title('Top 5 Products by Revenue')
plt.xlabel('Revenue')
plt.ylabel('Product')
plt.show()