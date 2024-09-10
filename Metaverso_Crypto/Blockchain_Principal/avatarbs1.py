# prb1.py
from flask import Flask, request, jsonify
from flask_socketio import SocketIO
from prb2 import Blockchain
from prb3 import log_action
from prb4 import comprimir_datos, descomprimir_datos
from prb5 import procesar_transaccion, cambiar_estructura_avatar

app = Flask(__name__)
socketio = SocketIO(app)

blockchain = Blockchain()

@app.route('/registrar', methods=['POST'])
def registrar():
    data = request.json
    nombre = data['nombre']
    log_action(f"Usuario registrado: {nombre}")
    cambiar_estructura_avatar()
    return jsonify({"mensaje": "Usuario registrado exitosamente"}), 201

@app.route('/verificar', methods=['POST'])
def verificar():
    data = request.json
    nombre = data['nombre']
    log_action(f"Usuario verificado: {nombre}")
    cambiar_estructura_avatar()
    return jsonify({"mensaje": "Usuario verificado"}), 200

@app.route('/eliminar', methods=['DELETE'])
def eliminar():
    data = request.json
    nombre = data['nombre']
    log_action(f"Usuario eliminado: {nombre}")
    cambiar_estructura_avatar()
    return jsonify({"mensaje": "Usuario eliminado"}), 200

def iniciar_servidor():
    log_action("Servidor iniciado")
    socketio.run(app, debug=True)

if __name__ == "__main__":
    iniciar_servidor()
