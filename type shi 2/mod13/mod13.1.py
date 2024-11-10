from flask import Flask, jsonify

app = Flask(__name__)

def hui(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

@app.route('/alkuluku/<int:number>', methods=['GET'])
def alkluk(number):
    vast = {
        "Numero": number,
        "on Alkuluku": hui(number)
    }
    return jsonify(vast)

if __name__ == '__main__':
    app.run(port=3000)
