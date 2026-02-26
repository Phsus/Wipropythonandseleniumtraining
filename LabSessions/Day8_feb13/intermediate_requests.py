import requests
import json

# 6. Fetch users and print usernames in uppercase

users = requests.get("https://jsonplaceholder.typicode.com/users").json()
usernames = [user['username'].upper() for user in users]
print(usernames)

# 7. Timeout handling

try:
    requests.get("https://jsonplaceholder.typicode.com/users", timeout=2)
    print("Request finished within 2 seconds.")
except requests.exceptions.Timeout:
    print("The request timed out!")

# 8. Session object and cookies

session = requests.Session()
# Setting a cookie on a mock mirror site
session.get("https://httpbin.org/cookies/set/session_id/12345")
response_cookies = session.get("https://httpbin.org/cookies")
print(f"Persisted Cookies: {response_cookies.json()}")

# 9. File upload

# Creating a dummy file locally to upload
with open("test_upload.txt", "w") as f:
    f.write("Hello World")

with open("test_upload.txt", "rb") as f:
    files = {'file': f}
    upload_resp = requests.post("https://httpbin.org/post", files=files)
    print(f"Server received file: {upload_resp.status_code}")

# 10. Fetch posts and save to JSON file

posts = requests.get("https://jsonplaceholder.typicode.com/posts").json()
with open("posts.json", "w") as f:
    json.dump(posts, f, indent=4)
print("Saved posts to posts.json")