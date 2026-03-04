import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# --- First Plot: Bar Chart using NumPy Arrays ---
# x axis data
x = np.array([1, 2, 3, 4])

# y axis data
y = x * 2

plt.bar(x, y)
plt.show()


# --- Second Plot: Bar Chart using Pandas ---
# line plot using pandas (Note: using kind="bar" to make a bar chart)
data = {
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "Steps": [4000, 5500, 7000, 6500, 8000]
}

df = pd.DataFrame(data)

# kind="bar" tells Pandas to draw vertical bars instead of a line
df.plot(x="Day", y="Steps", kind="bar")

plt.title("Daily Steps Count")
plt.xlabel("Day")
plt.ylabel("Steps")
plt.show()