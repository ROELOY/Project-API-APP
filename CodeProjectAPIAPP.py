import requests , json , random , Functies_API

while True:

    print("\n-----------------------------------------------------------")
    print("welkom bij het keuzemenu")
    print("-----------------------------------------------------------")
    print("1. zoek een willekeurige character van een Disney film.")
    print("2. Zoek een character van een aantal Disney film/serie/shortfilm en extra info. ")
    print("3. Zoek een character van een bepaalde Disney film. ")
    print("4. Wilt u stoppen met de app? ")

    print("-----------------------------------------------------------")

    antwoordVraag1 = input("\n Maak een keuze van bovenstaande Info: ")

    print("-----------------------------------------------------------")

    if antwoordVraag1 == "1":
        RandomPersonage = Functies_API.get_random_character()
        print(f"De Personage die je hebt heet {RandomPersonage['name']}.")
        print(f"De Personage komt voor in de volgende Films/Series/Shortfilm:")
        if RandomPersonage['films'] == []:
            print(f"- {RandomPersonage['name']} komt niet voor in een film.")
        else:
            print(f"-Films:{RandomPersonage['films']}")
        if RandomPersonage['tvShows'] == []:
            print(f"- {RandomPersonage['name']} komt niet voor in een serie.")
        else:
            print(f"-Series:{RandomPersonage['tvShows']}")
        if RandomPersonage['shortFilms'] == []:
            print(f"- {RandomPersonage['name']} komt niet voor in een short-film.")
        else:
            print(f"-ShortFilms:{RandomPersonage['shortFilms']}")

        print("-----------------------------------------------------------")
        antwoordVraag2 = input(f"\n Wil je een foto van het character {RandomPersonage['name']} zien (ja/nee): ")
        print("-----------------------------------------------------------")
        if antwoordVraag2.upper() == "NEE":
            continue
        else:
            Image_url = RandomPersonage['imageUrl']
            print(f"-Image-URL: {Image_url}")

    elif antwoordVraag1 == "2":
        naam = input("\n Welke naam wil je opzoeken voor een aantal films/series/shortfilms van Disney: ")
        resultaten = Functies_API.Naam_Ver_Films(naam)

        if not resultaten:
            print("Geen character gevonden met die naam.")
            continue

        print("-----------------------------------------------------------")
        Keuze_Video = input("\n Wil je meer weten in welke film / serie / shortfilm: ")
        print("-----------------------------------------------------------")

        character = resultaten[0]

        films = character.get("films", [])
        series = character.get("tvShows", [])
        shorts = character.get("shortFilms", [])

        if Keuze_Video.upper() == "FILM":
            print(f"Het character {character['name']} komt voor in de volgende films:")
            if films:
                for film in films:
                    print(f"- {film}")
            else:
                print("Geen films gevonden.")
        elif Keuze_Video.upper() == "SERIE":
            print(f"Het character {character['name']} komt voor in de volgende series:")
            if series:
                for serie in series:
                    print(f"- {serie}")
            else:
                print("Geen series gevonden.")
        elif Keuze_Video.upper() == "SHORTFILM":
            print(f"Het character {character['name']} komt voor in de volgende shortfilms:")
            if shorts:
                for short in shorts:
                    print(f"- {short}")
            else:
                print("Geen shortfilms gevonden.")
        else:
            print("Ongeldige keuze. Typ FILM, SERIE of SHORTFILM.")

        print("-----------------------------------------------------------")
        antwoordVraag2 = input(f"\n Wil je een foto van het character {character['name']} zien (ja/nee): ")
        print("-----------------------------------------------------------")
        if antwoordVraag2.upper() == "NEE":
            print('Volgende vraag')

        else:
            Image_url = character['imageUrl']
            print(f"-Image-URL: {Image_url}")

        print("-----------------------------------------------------------")
        antwoordVraag3 = input(f"\n Wil je meer info weten van {character['name']} (ja/nee): ")
        print("-----------------------------------------------------------")

        if antwoordVraag3.upper() == "NEE":
            continue
        else:
            antwoordVraag4 = input(f"\n Wil je weten als {character['name']} bondgenoten heeft (ja/nee): ")
            print("-----------------------------------------------------------")

            if antwoordVraag4.upper() == "NEE":
                print("-Voorlaatste vraag")
                print("-----------------------------------------------------------")
            else:
                if character['allies'] == []:
                    print(f"{character['name']} Heeft geen bondgenoten.")
                    print("-----------------------------------------------------------")
                    print("-Voorlaatste vraag")
                    print("-----------------------------------------------------------")
                else:
                    print(f"{character['name']} heeft deze bondgenoten:")
                    print(f"- {character['allies']}")
                    print("-----------------------------------------------------------")
                    print("-Voorlaatste vraag") 
                    print("-----------------------------------------------------------")

            antwoordVraag5 = input(f"\n Wil je weten als {character['name']} vijanden heeft (ja/nee): ")
            print("-----------------------------------------------------------")

            if antwoordVraag5.upper() == "NEE":
                print("-laatste vraag")
                print("-----------------------------------------------------------")
            else:
                if character['enemies'] == []:
                    print(f"{character['name']} Heeft geen vijanden.")
                    print("-----------------------------------------------------------")
                    print("-laatste vraag")
                    print("-----------------------------------------------------------")
                else:
                    print(f"{character['name']} heeft deze vijanden:")
                    print(f"- {character['enemies']}")
                    print("-----------------------------------------------------------")
                    print("-laatste vraag")
                    print("-----------------------------------------------------------")

            antwoordVraag6 = input(f"\n Wil je weten als {character['name']} een attractie heeft (ja/nee): ")
            print("-----------------------------------------------------------")

            if antwoordVraag6.upper() == "NEE":
                print("-----------------------------------------------------------")
            else:
                if character['enemies'] == []:
                    print(f"{character['name']} Heeft geen attractie.")
                    print("-----------------------------------------------------------")
                else:
                    print(f"{character['name']} heeft deze attractie's:")
                    print(f"- {character['parkAttractions']}")
                    print("-----------------------------------------------------------")



    elif antwoordVraag1 == "3":
        input("\n Welke naam wil je opzoeken van een bepaalde film van Disney: ")

        print("-----------------------------------------------------------")

        input("\n Van welke film wil je dit character opzoeken: ")

    elif antwoordVraag1 == "4":
        break

    else:
        print("Ongeldige input. Probeer opnieuw...")
        print("-----------------------------------------------------------")