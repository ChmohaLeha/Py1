import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    password='kisumisu24',
    autocommit=True
)


def airport_select():
    sql = """SELECT iso_country, ident, name, latitude_deg, longitude_deg
    FROM airport
    WHERE iso_country='FI'
    AND type IN ('medium_airport', 'large_airport')
    ORDER by RAND()
    ;"""
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


kilsat_pelaaja = 1500


def alku():
    lentokent = "EFHK"
    return lentokent
aloitus = alku()




def sijainti(kilsat_pelaaja, icao, aika, game_id):
    sql = f'''UPDATE game SET location = %s, kilsat_pelaaja = %s, aika = %s WHERE id = %s'''
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql, (kilsat_pelaaja, icao, aika, game_id))



def lahikentat(icao, a_ports, kilsat_pelaaja):
    lahel = []
    for a_port in a_ports:
        pituus = etaisuuden_lasku(icao, a_port['ident'])
        if pituus <= kilsat_pelaaja and pituus > 0:
            lahel.append({'airport': a_port, 'distance': pituus})
    lahel = sorted(lahel, key=lambda x: x['distance'])
    return lahel[:3]







