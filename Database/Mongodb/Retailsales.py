from pymongo import MongoClient
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# connect to local mongodb
client = MongoClient("mongodb://localhost:27017/")
db = client["company_db"]
collection = db["retail_sales"]

collection.drop()

# generate data
dates = pd.date_range(start="2023-01-01", periods=50, freq="W").strftime('%Y-%m-%d').tolist()
regions = np.random.choice(["North", "South", "East", "West"], 50)
products = np.random.choice(["Laptop", "Mouse", "Keyboard", "Monitor", "Desk"], 50)
categories = np.random.choice(["Electronics", "Accessories", "Furniture"], 50)
quantities = np.random.randint(1, 15, 50)
prices = np.random.randint(20, 1000, 50)

# format data as list of dictionaries
sales_data = []
for i in range(50):
    sales_data.append({
        "OrderID": 1001 + i,
        "Date": dates[i],
        "Region": regions[i],
        "Product": products[i],
        "Category": categories[i],
        "Quantity": int(quantities[i]),
        "Price": int(prices[i])
    })

# save to db
collection.insert_many(sales_data)

# fetch data back,
cursor = collection.find({}, {"_id": 0})
df = pd.DataFrame(list(cursor))

#  calc total revenue
df['Date'] = pd.to_datetime(df['Date'])
df['Revenue'] = df['Quantity'] * df['Price']

print(" Retail Analysis ")
print("Highest Revenue Region:", df.groupby('Region')['Revenue'].sum().idxmax())

# group by month
df['Month'] = df['Date'].dt.to_period('M')
monthly_trend = df.groupby('Month')['Revenue'].sum()
print("\nMonthly Sales Trend:\n", monthly_trend)

print("\nBest Performing Category:", df.groupby('Category')['Revenue'].sum().idxmax())

top_5_products = df.groupby('Product')['Revenue'].sum().nlargest(5)
print("\nTop 5 Products:\n", top_5_products)


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