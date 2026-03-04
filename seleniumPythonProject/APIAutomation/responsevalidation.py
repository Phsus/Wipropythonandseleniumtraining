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

        dta = response.json()

        print(response.text)
        print(response.content)
        print(response.status_code)
        print(response.headers)
        print(response.history)
        print(response.url)
        content_type = response.headers.get('content-Type')
        print(content_type)

        dta = response.json()
        print(dta)



    else: print(f"Error: Received status code {response.status_code}")

# Fixed RequestsException to RequestException
except requests.exceptions.RequestException as e:
    # Fixed prin to print
    print(f" An error occured: {e}")