from flask import Flask, jsonify

app = Flask(__name__)


def calcular_fatorial(numero):
    if numero < 0:
        return "Número deve ser não-negativo."
    elif numero == 0 or numero == 1:
        return 1
    else:
        fatorial = 1
        for i in range(1, numero + 1):
            fatorial *= i
        return fatorial


@app.route('/fatorial/<int:numero>', methods=['GET'])
def obter_fatorial(numero):
    resultado = calcular_fatorial(numero)
    return jsonify({'numero': numero, 'fatorial': resultado})


if __name__ == '__main__':
    app.run(debug=True)