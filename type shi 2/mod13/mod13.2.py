from flask import Flask, jsonify, abort
import sqlite3

app = Flask(__name__)


def getinfo(icao_code):
    conn = sqlite3.connect('airports.db')
    cursor = conn.cursor()
    cursor.execute("SELECT icao_code, name, municipality FROM airports WHERE icao_code = ?", (icao_code,))
    row = cursor.fetchone()

    conn.close()

    if row:
        return {
            "ICAO": row[0],
            "Name": row[1],
            "Municipality": row[2]
        }
    else:
        return None


@app.route('/kenttä/<string:icao_code>', methods=['GET'])
def kent(icao_code):
    airinf = getinfo(icao_code.upper())

    if airinf:
        return jsonify(airinf)
    else:
        abort(404, description="Lentokenttää ei löydy ICAO-koodilla")


if __name__ == '__main__':
    app.run(port=3000)
