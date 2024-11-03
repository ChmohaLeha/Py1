import requests

def saa(kaup):
    pyyd = (f"https://api.openweathermap.org"
            f"/data/2.5/weather?q={kaup}&"
            f"appid=259fbb404512322b82e7a1e012bb912f&units=metric&lang=fi")
    r = requests.get(pyyd).json()
    weather = r["weather"][0]["description"]
    temp = r["main"]["temp"]
    print(weather)
    print(f"Lämpötila on {temp:.1f} astetta")

kaup = input("Kaupunki?: ")
saa(kaup)