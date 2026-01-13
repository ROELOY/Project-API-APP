import requests , json , random , Functies_API

while True:

    print("\n-----------------------------------------------------------")
    print("welkom bij het keuzemenu")
    print("-----------------------------------------------------------")
    print("1. zoek een willekeurige character van een Disney film")
    print("2. Zoek een character van een aantal Disney film. ")
    print("3. Zoek een character van een bepaalde Disney film. ")

    print("-----------------------------------------------------------")

    antwoordVraag1 = input("\n Maak een keuze van bovenstaande Info: ")

    print("-----------------------------------------------------------")

    if antwoordVraag1 == "1":
        RandomPersonage = Functies_API.get_random_character()
        print(f"De Personage die je hebt heet {RandomPersonage['name']}.")
        print(f"De Personage komt voor in de volgende Films/Series/Shortfilm:")
        if RandomPersonage['films'] == []:
            continue
        else:
            print(f"-Films:{RandomPersonage['films']}")
        if RandomPersonage['tvShows'] == []:
            continue
        else:
            print(f"-Series:{RandomPersonage['tvShows']}")
        if RandomPersonage['shortFilms'] == []:
            continue
        else:
            print(f"-ShortFilms:{RandomPersonage['shortFilms']}")

    elif antwoordVraag1 == "2":
        input("\n Welke naam wil je opzoeken voor een aantal films van Disney: ")

    elif antwoordVraag1 == "3":
        input("\n Welke naam wil je opzoeken van een bepaalde film van Disney: ")

        print("-----------------------------------------------------------")

        input("\n Van welke film wil je dit character opzoeken: ")

    else:
        print("Ongeldige input. Probeer opnieuw...")
        print("-----------------------------------------------------------")