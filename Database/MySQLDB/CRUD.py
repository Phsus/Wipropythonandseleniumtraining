import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sushh@586"
)

cursor = connection.cursor()
print("Connected successfully")

cursor.execute("CREATE DATABASE IF NOT EXISTS school")
connection.commit()

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sushh@586",
    database="school"
)

cursor = connection.cursor()
print("Connected successfully to school database")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        age INT,
        grade VARCHAR(10)
    )
""")
connection.commit()
print("Table created successfully")