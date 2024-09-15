from geopy import distance
import mysql.connector

con = mysql.connector.connect(
    host="127.0.0.1",
    port = 3306,
    database="flight_game",
    user="root",
    password="hui",
    autocommit=True,
    collation="utf8mb4_general_ci",
)

def koord(icao)
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = "{icao}""
    cursor = con.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()"
    return result

icao1 = input("Syötä 1. lentoasema ICAO-koodi: ").upper()
icao2 = input("Syötä 2. lentoasema ICAO-koodi: ").upper()

kord1 = koord(icao1)
kord2 = koord(icao2)

print(f"Etäisyys kenttien välillä on {distance.distance(kord1, kord2).km:.2f} kilometriä:")
