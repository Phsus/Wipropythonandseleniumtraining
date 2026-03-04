import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "Steps": [4000, 5500, 7000, 6500, 8000]
}

df = pd.DataFrame(data)
df.plot(x="Day", y="Steps", kind="bar")

plt.title("Daily Steps Count")
plt.xlabel("Day")
plt.ylabel("Steps")

plt.savefig("BarChart.jpg")
plt.savefig("bar.pdf", format="pdf")