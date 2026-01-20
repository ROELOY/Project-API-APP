import requests , json

url = "https://api.disneyapi.dev/character"
response_json1 = requests.get(url).json()

# JSON opslaan
with open(r"C:\Users\Roelo\OneDrive - MOSA-RT\2025-2026\prog2\Project-API-APP\ProjectAPI-allCharacters.json", "w") as fp:
    json.dump(response_json1, fp, indent=4)

url = "https://api.disneyapi.dev/character/5"
response_json2 = requests.get(url).json()

# JSON opslaan
with open(r"C:\Users\Roelo\OneDrive - MOSA-RT\2025-2026\prog2\Project-API-APP\ProjectAPI-1specifiekeCharacter.json", "w") as fp:
    json.dump(response_json2, fp, indent=4)

url = "https://api.disneyapi.dev/character?name=Donald Duck"
response_json3 = requests.get(url).json()

# JSON opslaan
with open(r"C:\Users\Roelo\OneDrive - MOSA-RT\2025-2026\prog2\Project-API-APP\ProjectAPI-CharacterFilter.json", "w") as fp:
    json.dump(response_json3, fp, indent=4)