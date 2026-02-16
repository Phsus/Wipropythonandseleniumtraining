import requests

# 1. GET request and print name and email

response = requests.get("https://jsonplaceholder.typicode.com/users")
users = response.json()
for user in users:
    print(f"Name: {user['name']} | Email: {user['email']}")

# 2. GET with query parameters

params = {'userId': 2}
response_posts = requests.get("https://jsonplaceholder.typicode.com/posts", params=params)
print(f"Number of posts returned: {len(response_posts.json())}")

# 3. POST request to create resource

new_data = {"title": "foo", "body": "bar", "userId": 1}
post_response = requests.post("https://jsonplaceholder.typicode.com/posts", json=new_data)
print(f"Status Code: {post_response.status_code}") # Should be 201

# 4. Difference between data= and json=
"""
Answer: 
- data=: Sends form-encoded data (Content-Type: application/x-www-form-urlencoded).
- json=: Automatically serializes a Python dict to a JSON string and sets 
         Content-Type: application/json.
"""

# 5. Check if not 200 and raise exception

try:
    bad_response = requests.get("https://jsonplaceholder.typicode.com/invalid-path")
    if bad_response.status_code != 200:
        bad_response.raise_for_status() # Raises HTTPError
except requests.exceptions.HTTPError as e:
    print(f"Caught expected error: {e}")