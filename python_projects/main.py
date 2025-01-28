import requests

URL = 'https://api.pokemonbattle.ru/v2/'
HEADER = {
    'Content-Type': 'application/json',
    'trainer_token': 'TOKEN'
}
body_spawn = {
    "name": "питонорожденный",
    "photo_id": 35
}
body_change = {
    "pokemon_id": "205800",
    "name": "Pythonborn",
    "photo_id": 35
}
body_catch = {
    "pokemon_id": "205800"
}

'''response_spawn = requests.post(url = f'{URL}pokemons', headers = HEADER, json = body_spawn)
print(response_spawn.text)'''

'''response_change = requests.put(url = f'{URL}pokemons', headers = HEADER, json = body_change)
print(response_change.text)'''

respons_catch = requests.post(url = f'{URL}trainers/add_pokeball', headers = HEADER, json = body_catch)
print(respons_catch.text)