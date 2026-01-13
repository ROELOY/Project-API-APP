import requests
import random
import json

info_url = "https://api.disneyapi.dev/character"
info_response = requests.get(info_url).json()

totaalPaginas = info_response["info"]["totalPages"] # de variabele totaal_paginas is van de response de info en de totalPages.

while True: # als waar
    randomPage = random.randint(1, totaalPaginas) # variabele random_Page wordt gebruikt met de hand van de module Random . randint om in die range te blijven van 1 en het aantal totale paginas

    page_url = f"https://api.disneyapi.dev/character?page={randomPage}" # dan wordt de url gevraagd met de varaiabele random_page voor die pagina wat de variabele is
    pageResponse = requests.get(page_url).json() # krijgen wij weer een nieuwe response
    with open(r"C:\Users\Roelo\OneDrive - MOSA-RT\2025-2026\prog2\Project-API-APP\ProjectAPI-allCharacters.json", "w") as fp:
        json.dump(pageResponse, fp, indent=4)

    characters = pageResponse.get("data", []) # de characters van die pagina komen allemaal in de variabele characters.

    if characters == []: # als er geen charcters zijn dan...
        continue # doe verder zoeken

    character = random.choice(characters) # kies een random character van die pagina.
    break

# Test Print
# character = get_random_character()

print(f"Naam: {character['name']}")
print(f"Films: {character['films']}")
print(f"Enemies: {character['enemies']}")
print(f"Image URL: {character['imageUrl']}")
print(f"Id: {character['_id']}")

