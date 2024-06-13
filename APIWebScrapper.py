import requests
import pprint
import inflection

# Note about the exercise:
# The script webscrapes the API endpoint "http://swapi.dev/api/starships/"
# using the request library. The script first records the name of the Star
# Wars starships and then prints them. The "ordinal()" method of the inflection
# library is used in this printing. The "pprint()" method of the "pprint" library
# is used to format printing while exploring the data.

URL="http://swapi.dev/api/starships/"

r = requests.get(URL)
type(r)

data = r.json()
pprint.pprint(data)

type(data) # data is a dictionary
data.keys() # Exploring the keys 

pprint.pprint(data['results'][0])

starship_names = [element['name'] for element in data['results']]

for idx, starship in enumerate(starship_names):
  ord = inflection.ordinal(idx+1)
  print(f'The {idx+1}{ord} starship name is {starship}\n')
