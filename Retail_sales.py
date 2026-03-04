import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("retail_sales.csv")

df['Date'] = pd.to_datetime(df['Date'])
df = df.dropna()
df['Revenue'] = df['Quantity'] * df['Price']

print("Analysis Results")
print("Highest Revenue Region:", df.groupby('Region')['Revenue'].sum().idxmax())

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
top_5_products.sort_values().plot(kind='bar', color='orange')
plt.title('Top 5 Products by Revenue')
plt.xlabel('Revenue')
plt.ylabel('Product')
plt.show()