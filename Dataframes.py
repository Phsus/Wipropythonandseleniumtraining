import pandas as pd
import numpy as np

# Create DataFrame from List of Dictionaries
print("--- DataFrame from List of Dictionaries ---")
data = [
    {"Name": "Ram", "Age": 25},
    {"Name": "Sam", "Age": 30},
    {"Name": "John", "Age": 28}
]

df1 = pd.DataFrame(data)
print(df1)
print("\n")


# Create DataFrame from Dictionary of Series
print("--- DataFrame from Dictionary of Series ---")
s1 = pd.Series([1, 2, 3])
s2 = pd.Series([4, 5, 6])

df2 = pd.DataFrame({"A": s1, "B": s2})
print(df2)
print("\n")


# Create DataFrame from NumPy Array
print("--- DataFrame from NumPy Array ---")
arr = np.array([[1, 2], [3, 4], [5, 6]])

df3 = pd.DataFrame(arr, columns=["Col_1", "Col_2"])
print(df3)