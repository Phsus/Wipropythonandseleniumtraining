import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sushh@586",
    database="school"
)

cursor = connection.cursor()

cursor.execute("ALTER TABLE students ADD COLUMN marks INT")
cursor.execute("ALTER TABLE students ADD COLUMN subject VARCHAR(50)")

sql = "INSERT INTO students (name, age, grade, marks, subject) VALUES (%s, %s, %s, %s, %s)"
val = [
    ("Ram", 20, "A", 85, "Maths"),
    ("Sam", 21, "B", 78, "Science"),
    ("John", 20, "A", 92, "Maths"),
    ("Alice", 22, "C", 65, "Science")
]

cursor.executemany(sql, val)
connection.commit()

print("Columns added and data inserted successfully!")