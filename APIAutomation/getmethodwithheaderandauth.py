import requests
from requests.auth import HTTPBasicAuth

try:
    headers = {
        "User-Agent": "MyApp/1.0",
        "Accept": "application/json"
    }

    # Fixed the auth syntax and brackets
    response = requests.get(
        "https://videogamedb.uk:443/api/v2/videogame",
        auth=HTTPBasicAuth('username', 'password'),
        timeout=5,
        headers=headers
    )
    print(response)

    if response.status_code == 200:
        print("status code is 200 k")

        data = response.json()
        print(data)

    else: print(f"Error: Received status code {response.status_code}")

# Fixed RequestsException to RequestException
except requests.exceptions.RequestException as e:
    # Fixed prin to print
    print(f" An error occured: {e}")