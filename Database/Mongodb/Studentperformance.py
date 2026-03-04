from pymongo import MongoClient
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# db setup
client = MongoClient("mongodb://localhost:27017/")
db = client["school"]
collection = db["student_performance"]


collection.drop()

# generated random student data
genders = np.random.choice(["Male", "Female"], 50)
math_scores = np.random.randint(20, 100, 50)
science_scores = np.random.randint(20, 100, 50)
english_scores = np.random.randint(20, 100, 50)
attendance = np.random.randint(40, 100, 50)

student_data = []
for i in range(50):
    student_data.append({
        "StudentID": i + 1,
        "Gender": genders[i],
        "Math": int(math_scores[i]),
        "Science": int(science_scores[i]),
        "English": int(english_scores[i]),
        "Attendance": int(attendance[i])
    })

collection.insert_many(student_data)

# load into pandas
cursor = collection.find({}, {"_id": 0})
df = pd.DataFrame(list(cursor))

# calc average and check if they passed (40 is the cutoff)
df['Average_Marks'] = df[['Math', 'Science', 'English']].mean(axis=1)
df['Result'] = np.where(df['Average_Marks'] >= 40, 'Pass', 'Fail')

print(" Student Analysis ")
subject_avgs = df[['Math', 'Science', 'English']].mean()
print("Average Score per Subject:\n", subject_avgs)

correlation = df['Attendance'].corr(df['Average_Marks'])
print(f"\nCorrelation (Attendance vs Average Marks): {correlation:.2f}")

gender_performance = df.groupby('Gender')['Average_Marks'].mean()
print("\nPerformance by Gender:\n", gender_performance)

pass_fail_counts = df['Result'].value_counts()
print("\nPass vs Fail Counts:\n", pass_fail_counts)

# charts

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