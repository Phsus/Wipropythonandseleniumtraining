import requests

try:
    # Attempting to delete object ID 7 (a standard example ID for this API)
    response = requests.delete("https://api.restful-api.dev/objects/1")
    print(response)

    # Note: Some APIs return 200 OK, others return 204 No Content for deletes
    if response.status_code == 200:
        print("status code is 200 k")

        # Only attempt to parse JSON if the response actually has a body
        try:
            data = response.json()
            print(data)
        except:
            print("Resource deleted successfully (No JSON body returned)")

    else:
        print(f"Error: Received status code {response.status_code}")
        print(f"Response: {response.text}")

except requests.exceptions.RequestException as e:
    # Corrected 'RequestsException' to 'RequestException' and 'prin' to 'print'
    print(f" An error occured: {e}")