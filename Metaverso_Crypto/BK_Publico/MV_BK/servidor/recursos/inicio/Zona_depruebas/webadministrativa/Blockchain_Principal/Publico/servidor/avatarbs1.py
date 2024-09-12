# en un principio toca revisar primero 
# antes de la implementación.

from flask import Flask, request, jsonify
from flask_socketio import SocketIO
from Metaverso_Crypto.webadministrativa.Blockchain_Principal.Publico.servidor.avatarbs2 import Blockchain
from Metaverso_Crypto.webadministrativa.Blockchain_Principal.Publico.servidor.avatarbs3 import log_action
from Metaverso_Crypto.webadministrativa.Blockchain_Principal.Publico.servidor.avatarbs4 import comprimir_datos, descomprimir_datos
from Metaverso_Crypto.webadministrativa.Blockchain_Principal.Publico.servidor.avatarbs5 import procesar_transaccion, cambiar_estructura_avatar

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
