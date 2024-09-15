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

icao = input("Syötä ICAO koodi: ").upper()

def prcnt(icao):
    sql = "SELECT name, municipality FROM airport"
    sql += f" WHERE ident = '{icao}'"
    cursor = con.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"Lentoaseman nimi on {row[0]} ja sen seijaintikunta {row[1]}")
            return
prcnt(icao)
