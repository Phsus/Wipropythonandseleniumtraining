from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["school"]
collection = db["students"]

students_data = [
    {"name": "Ram", "age": 20, "grade": "A", "marks": 85, "subject": "Maths"},
    {"name": "Sam", "age": 21, "grade": "B", "marks": 78, "subject": "Science"},
    {"name": "John", "age": 20, "grade": "A", "marks": 92, "subject": "Maths"},
    {"name": "Alice", "age": 22, "grade": "C", "marks": 65, "subject": "Science"}
]

collection.insert_many(students_data)

print("Data inserted successfully!")