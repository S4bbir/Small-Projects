import requests
import json

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info():
    pokemon_name = get_pokemon_name()
    url = f"{base_url}/pokemon/{pokemon_name}"

#   print(requests.get(f"{base_url}/pokemon/{pokemon_name}"))

    response = requests.get(url)
    if response.status_code == 200:
        print(f"Data Retrieved")
        return json.dumps(response.json(), indent = 3)

        #pokemon_data = response.json()
        #return pokemon_data

    else:
        print(f"Failed to retrieve data {response.status_code}")

def get_pokemon_name():
    return str(input("Enter the pokemon name: "))

print(get_pokemon_info())


