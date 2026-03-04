import pandas as pd
import numpy as np


data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'Age': [24, 27, np.nan, 32, 29, np.nan],
    'Salary': [50000, 60000, 55000, np.nan, 70000, 45000],
    'Department': ['IT', 'HR', 'IT', 'Finance', 'IT', 'HR'],
    'City': ['Bangalore', 'Mumbai', 'Bangalore', 'Delhi', 'Bangalore', 'Pune']
}
df = pd.DataFrame(data)
print(df)
print("\n")


print(df.isna())
print("\n")

# 3. Replace missing values with 0.

df_filled = df.fillna(0)
print(df_filled)
print("\n")

# 4. Drop rows containing missing values.
df_dropped = df.dropna()
print(df_dropped)
print("\n")

# 5. Sort the DataFrame by Age in ascending order.
df_sorted_age = df.sort_values(by='Age')
print(df_sorted_age)
print("\n")

# 6. Sort the DataFrame by Salary in descending order.
df_sorted_salary = df.sort_values(by='Salary', ascending=False)
print(df_sorted_salary)
print("\n")

# 7. Perform groupby on Department and find average Salary per department.
avg_salary = df_filled.groupby('Department')['Salary'].mean()
print(avg_salary)
print("\n")

# 8. Find total Salary per department using groupby.
total_salary = df_filled.groupby('Department')['Salary'].sum()
print(total_salary)
print("\n")

# 9. Filter employees where Age > 25 AND City = 'Bangalore'.
filtered_df = df[(df['Age'] > 25) & (df['City'] == 'Bangalore')]
print(filtered_df)
print("\n")

# 10. Create a new column 'Tax' which is 10% of Salary using apply().
df_filled['Tax'] = df_filled['Salary'].apply(lambda x: x * 0.10)
print(df_filled)