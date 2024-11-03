import requests

def vitsi():
    pyynto = "https://api.chucknorris.io/jokes/random"
    data = requests.get(pyynto).json()
    return data["value"]

jo = input("Painamalla enter saat vitsin")

print(vitsi())