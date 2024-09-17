import time
from flask import Flask, request, jsonify
from flask_socketio import SocketIO
from Metaverso_Crypto.inicio.Zona_depruebas.webadministrativa.Blockchain_Principal.Zona_de_pruebas.admin.pruebas2.Bk_Servidor.BK_dbts.src.BK_mdsl.BK_app2 import Blockchain, Block
from Metaverso_Crypto.inicio.Zona_depruebas.webadministrativa.Blockchain_Principal.Zona_de_pruebas.admin.pruebas2.Bk_Servidor.BK_dbts.src.BK_rts.BK_app3 import log_action
from Metaverso_Crypto.inicio.Zona_depruebas.webadministrativa.Blockchain_Principal.Zona_de_pruebas.admin.pruebas2.Bk_Servidor.BK_dbts.src.BK_Scv.BK_app4 import comprimir_datos, descomprimir_datos
from Wold_Virtual.BK_Adm_prb.BK_Inicio.BK_Blockchain_Principal.Bk_Servidor.BK_RCS.BK_Admin_web.BK_Scr1.BK_Stst.BK_App5 import procesar_transaccion, validar_transaccion, gestionar_usuario, auditar_transacciones

app = Flask(__name__)
socketio = SocketIO(app)

blockchain = Blockchain()

@app.route('/registrar', methods=['POST'])
def registrar():
    data = request.json
    nombre = data['nombre']
    contraseña = data['contraseña']
    gestionar_usuario("registrar", nombre)
    return jsonify({"mensaje": "Usuario registrado exitosamente"}), 201

@app.route('/verificar', methods=['POST'])
def verificar():
    data = request.json
    nombre = data['nombre']
    gestionar_usuario("verificar", nombre)
    return jsonify({"mensaje": "Usuario verificado"}), 200

@app.route('/eliminar', methods=['DELETE'])
def eliminar():
    data = request.json
    nombre = data['nombre']
    gestionar_usuario("eliminar", nombre)
    return jsonify({"mensaje": "Usuario eliminado"}), 200

@app.route('/auditar', methods=['GET'])
def auditar():
    auditar_transacciones()
    return jsonify({"mensaje": "Auditoría de transacciones realizada"}), 200

def iniciar_servidor():
    log_action("Servidor iniciado")
    socketio.run(app, debug=True)

def main():
    datos_usuario = ["file1.txt", "file2.txt"]
    archivo_comprimido = "datos_comprimidos.gz"
    comprimir_datos(datos_usuario, archivo_comprimido)
    descomprimir_datos(archivo_comprimido)
    procesar_transaccion("transaccion_ejemplo")
    iniciar_servidor()

if __name__ == "__main__":
    main()
