import pandas as pd
import numpy as np

dates = pd.date_range(start="2023-01-01", periods=50, freq="W")

retail_data = {
    "OrderID": range(1001, 1051),
    "Date": dates,
    "Region": np.random.choice(["North", "South", "East", "West"], 50),
    "Product": np.random.choice(["Laptop", "Mouse", "Keyboard", "Monitor", "Desk"], 50),
    "Category": np.random.choice(["Electronics", "Accessories", "Furniture"], 50),
    "Quantity": np.random.randint(1, 15, 50),
    "Price": np.random.randint(20, 1000, 50)
}

pd.DataFrame(retail_data).to_csv("retail_sales.csv", index=False)

student_data = {
    "StudentID": range(1, 51),
    "Gender": np.random.choice(["Male", "Female"], 50),
    "Math": np.random.randint(20, 100, 50),
    "Science": np.random.randint(20, 100, 50),
    "English": np.random.randint(20, 100, 50),
    "Attendance": np.random.randint(40, 100, 50)
}

pd.DataFrame(student_data).to_csv("student_performance.csv", index=False)