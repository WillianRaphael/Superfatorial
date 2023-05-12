from flask import Flask, jsonify

app = Flask(__name__)

def calcular_fatorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * calcular_fatorial(numero - 1)

def calcular_super_fatorial(numero):
    super_fatorial = 1
    for i in range(1, numero + 1):
        super_fatorial *= calcular_fatorial(i)
    return super_fatorial

@app.route('/super_fatorial/<int:numero>')
def rota_super_fatorial(numero):
    resultado = calcular_super_fatorial(numero)
    resposta = {
        'numero': numero,
        'super_fatorial': resultado
    }
    return jsonify(resposta)

if __name__ == '__main__':
    app.run(debug=True)
