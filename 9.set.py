x = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8]
y = set(x)
z = list(y)

import requests
get_data = requests.get('https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0')
data_json = get_data.json()
results = data_json['results']
pokemon_names = [ item['name']for item in results]
print(pokemon_names)
print(len(list(set(pokemon_names))))