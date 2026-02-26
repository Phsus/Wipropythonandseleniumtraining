import requests

try:
    dta ={
            "category": "Platform",
            "name": "Mario",
            "rating": "Mature",
            "releaseDate": "2012-05-04",
            "reviewScore": 85
        }


    response = requests.put("https://videogamedb.uk:443/api/v2/videogame/1" , json=dta)
    print(response)

    if response.status_code == 200:
        print("status code is 200 k")

        data = response.json()
        print(data)

    else: print(f"Error: Received status code {response.status_code}")

except requests.exceptions.RequestsException as e:
    prin(f" An error occured: {e}")