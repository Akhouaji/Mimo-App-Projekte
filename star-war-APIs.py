from pip._vendor import requests

def fetch_data(option):
  url = f"https://swapi.mimo.dev/api/{option}/"
  data = []

  try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data
 
  except requests.HTTPError as e:
    print(e)
    return None

user_input = input("What Starwars you would like to explore?")
option = user_input.strip().lower()

data = fetch_data(option)

if data:
  for i in data:
    print(i["name"])
else:
  print("Unable to download data")
