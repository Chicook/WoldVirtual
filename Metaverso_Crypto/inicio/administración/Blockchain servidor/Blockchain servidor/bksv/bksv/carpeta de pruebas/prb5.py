import json
import hashlib
from flask import Flask, request, jsonify
from prb2 import registrar_actividad_css

app = Flask(__name__)

def crear_wallet():
    wallet_id = "bkmv" + hashlib.sha256().hexdigest()[:8]
    wallet = {'id': wallet_id, 'balance': 0}
    with open(f'{wallet_id}.json', 'w') as f:
        json.dump(wallet, f)
    registrar_actividad_css(f"Wallet creada: {wallet_id}")
    return wallet

def validar_registro(forks):
    if forks == 4:
        valor = 30000000.000
    else:
        valor = 0.001
    registrar_actividad_css(f"Registro validado: forks={forks}, valor={valor}")
    return valor

@app.route('/crear_wallet', methods=['POST'])
def crear_wallet_route():
    wallet = crear_wallet()
    return jsonify({"message": "Wallet creada", "wallet": wallet}), 201

@app.route('/validar_registro', methods=['POST'])
def validar_registro_route():
    data = request.get_json()
    forks = data.get('forks')
    valor = validar_registro(forks)
    return jsonify({"message": "Registro validado", "valor": valor}), 200

if __name__ == '__main__':
    app.run(debug=True)
    
