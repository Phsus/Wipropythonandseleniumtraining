import pandas as pd
import numpy as np

# 1. Creating a Series from a list with a custom index
print("--- Series from List ---")
data1 = ['steve', '35', 'Male', '3.5']
series1 = pd.Series(data1, index=['Name', 'Age', 'Gender', 'Rating'])
print(series1)
print("\n")

# 2. Creating a Series from a list of numbers with a custom index
print("--- Series with Custom Index ---")
data2 = [100, 200, 300]
s2 = pd.Series(data2, index=['a', 'b', 'c'])
print(s2)
print("\n")

# 3. Creating a Series from a Python dictionary
print("--- Series from Dictionary ---")
data3 = {'a': 1, 'b': 2, 'c': 3} # Fixed dictionary syntax here
s3 = pd.Series(data3)
print(s3)
print("\n")

# 4. Creating a Series from a NumPy array
print("--- Series from NumPy Array ---")
arr = np.array([5, 10, 15])
s4 = pd.Series(arr)
print(s4)
print("\n")

# 5. Creating an empty Series with a specific data type
print("--- Empty Series ---")
s5 = pd.Series(dtype=float)
print(s5)

