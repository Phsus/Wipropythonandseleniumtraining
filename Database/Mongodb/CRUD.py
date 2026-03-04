from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
print("Connected successfully")

db = client["school"]
collection = db["students"]

students = [
    {"name": "Ravi", "subject": "Science", "marks": 90},
    {"name": "Sneha", "subject": "Math", "marks": 78},
    {"name": "Kiran", "subject": "Science", "marks": 88}
]

collection.insert_many(students)

for doc in collection.find():
    print(doc)

collection.update_one(
    {"name": "Ravi"},
    {"$set": {"marks": 95}}
)

collection.delete_one({"name": "Sneha"})