import matplotlib.pyplot as plt
import numpy as np

ages = np.random.randint(22, 60, 200)

plt.hist(ages, bins=10, color='skyblue', edgecolor='black')
plt.title("Employee Age Distribution")
plt.xlabel("Age Ranges")
plt.ylabel("Number of Employees")
plt.show()