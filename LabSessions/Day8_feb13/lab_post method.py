import requests

try:
    # Defining the data payload for the cart
    dta = {
        "id": 0,
        "userId": 0,
        "products": [
            {
                "id": 0,
                "title": "string",
                "price": 0.1,
                "description": "string",
                "category": "string",
                "image": "http://example.com"
            }
        ]
    }

    # Using POST to send the data to the carts endpoint
    response = requests.post("https://fakestoreapi.com/carts", json=dta)
    print(response)

    if response.status_code == 200:
        print("status code is 200 k")

        data = response.json()
        print(data)

    else: print(f"Error: Received status code {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f" An error occured: {e}")