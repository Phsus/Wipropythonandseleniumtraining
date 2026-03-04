import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("student_performance.csv")

df['Average_Marks'] = df[['Math', 'Science', 'English']].mean(axis=1)
df['Result'] = np.where(df['Average_Marks'] >= 40, 'Pass', 'Fail')

print("Analysis Results")
subject_avgs = df[['Math', 'Science', 'English']].mean()
print("Average Score per Subject:\n", subject_avgs)

correlation = df['Attendance'].corr(df['Average_Marks'])
print(f"\nCorrelation (Attendance vs Average Marks): {correlation:.2f}")

gender_performance = df.groupby('Gender')['Average_Marks'].mean()
print("\nPerformance by Gender:\n", gender_performance)

pass_fail_counts = df['Result'].value_counts()
print("\nPass vs Fail Counts:\n", pass_fail_counts)

plt.figure(figsize=(8, 5))
subject_avgs.plot(kind='bar', color=['blue', 'orange', 'green'])
plt.title('Average Subject Scores')
plt.ylabel('Score')
plt.show()

plt.figure(figsize=(8, 5))
plt.scatter(df['Attendance'], df['Average_Marks'], alpha=0.7, color='purple')
plt.title('Attendance vs Average Marks')
plt.xlabel('Attendance (%)')
plt.ylabel('Average Marks')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

plt.figure(figsize=(8, 5))
df.boxplot(column='Average_Marks', by='Gender', grid=False)
plt.title('Marks Distribution by Gender')
plt.suptitle('')
plt.ylabel('Average Marks')
plt.show()

plt.figure(figsize=(8, 8))
pass_fail_counts.plot(kind='pie', autopct='%1.1f%%', colors=['lightgreen', 'lightcoral'])
plt.title('Pass vs Fail')
plt.ylabel('')
plt.show()