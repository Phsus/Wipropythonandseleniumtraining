import matplotlib.pyplot as plt

# --- First Graph: Simple Mathematical Plot ---
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Creates the line graph
plt.plot(x, y)

# Axis labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple plot')

# The show method will display the data in a popup window
plt.show()


# --- Second Graph: Student Marks ---
subjects = ["Maths", "Science", "English", "History", "Computer"]
marks = [85, 78, 92, 74, 88]

# Creates the line graph
plt.plot(subjects, marks)

# Axis labels and title
plt.title("Student Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")

# Displays the second popup window
plt.show()