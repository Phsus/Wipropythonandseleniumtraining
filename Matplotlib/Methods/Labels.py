import matplotlib.pyplot as plt

def add_labels(x, y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i])  # Placing text slightly above the bar

# Data for the bar chart
x = ["Engineering", "BSc", "MBA", "Bcom", "BBA", "MSc"]
y = [9330, 4050, 3030, 5500, 8040, 4560]

# Creating bar chart
plt.bar(x, y)

# Adding value labels
add_labels(x, y)

# Adding title and labels
plt.title("College Admission")
plt.xlabel("Courses")
plt.ylabel("Number of Admissions")

# Display the chart
plt.show()