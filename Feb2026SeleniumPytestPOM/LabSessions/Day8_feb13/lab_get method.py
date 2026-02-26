import requests

try:

    response = requests.get("https://api.restful-api.dev/objects")
    print(response)

    if response.status_code == 200:
        print("status code is 200 k")

        data = response.json()
        print(data)

    else: print(f"Error: Received status code {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f" An error occured: {e}")