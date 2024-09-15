from multiprocessing import connection


def ica(code):
    sql = f"SELECT name, municipality FROM airport WHERE ident = '{code}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    return result

use_input = input("Anna ICAO koodi: ")
use_input = use_input.upper()
result = ica(use_input)
for hui in result:
    print(f"Haettu kenttä: {hui[0]}, {hui[1]}")
else:
    print(f"EI löydy.")

