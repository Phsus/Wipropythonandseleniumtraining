import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# --- First Plot: Using NumPy Arrays ---

# x axis data
x = np.array([1, 2, 3, 4])

# y axis data (vectorized math)
y = x * 2

plt.plot(x, y)
plt.show()

# --- Second Plot: Using a Pandas DataFrame ---

# line plot using pandas
data = {
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "Steps": [4000, 5500, 7000, 6500, 8000]
}

df = pd.DataFrame(data)

# Pandas has built-in plotting capabilities that use Matplotlib under the hood
df.plot(x="Day", y="Steps", kind="line")

plt.title("Daily Steps Count")
plt.xlabel("Day")
plt.ylabel("Steps")
plt.show()