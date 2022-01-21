import requests

pokemonss = {}


class Pokemon:
    def __init__(self, name):
        if name in pokemonss:
            pp = pokemonss[name]
            print(*pp.b)
        else:
            url = "https://pokeapi.co/api/v2/pokemon/"+name
            req = requests.get(url)
            if req.status_code == 404:
                print("Дурачок")
                return
            pokemon = req.json()
            self.b = []
            for i in pokemon["abilities"]:
                self.b.append(i["ability"]["name"])
            print(*self.b, sep=", ")



while True:
    command = input()

    if command == "get":
        name = input("Ну шо ты, пиши имя: ")
        url = "https://pokeapi.co/api/v2/pokemon/" + name
        req = requests.get(url)
        if req.status_code == 404:
            print("Дурачок")
        else:
            pokemon = Pokemon(name)
            pokemonss[name] = pokemon
    else:
        print("Дурачок")
