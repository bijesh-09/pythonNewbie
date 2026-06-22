import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url) # returns a response object
    # print(response)
    if response.status_code == 200: # 200 means the request was successful
        print("Data retrieved successfully!")
        pokemon = response.json() # converts the response to a dictionary
        return pokemon
    else:
        print(f"Error: {response.status_code}")
        print(f"Error message: {response.json().get('detail', 'Unknown error')}")
        return None

pokemon_name = "pikachu"
pokemon_info = get_pokemon(pokemon_name)

if pokemon_info:
    print(f"Pokemon\'s name: {pokemon_info['name']}")
    print(f"Pokemon\'s id: {pokemon_info['id']}")
    print(f"Pokemon\'s height: {pokemon_info['height']}")
    print(f"Pokemon\'s weight: {pokemon_info['weight']}")