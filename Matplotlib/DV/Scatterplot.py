import matplotlib.pyplot as plt

hours_studied = [1, 2, 2.5, 3, 4, 4.5, 5, 6, 7, 8]
exam_scores = [40, 45, 50, 60, 65, 75, 80, 85, 90, 95]

plt.scatter(hours_studied, exam_scores, color='red', marker='x')
plt.title("Study Hours vs Exam Score")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()