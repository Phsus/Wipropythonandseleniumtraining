import matplotlib.pyplot as plt

labels = ['Maths', 'Science', 'English', 'History']
scores = [85, 90, 75, 80]

plt.pie(scores, labels=labels, autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
plt.title("Marks Distribution")
plt.show()