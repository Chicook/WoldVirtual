from flask import Flask, jsonify, request, render_template_string
import hashlib
import json
import random
import time

# Importar funciones de otros módulos
from prb2 import registrar_usuario, verificar_credenciales, registrar_actividad_css
from prb3 import manejar_accion, registrar_actividad_js
from prb4 import get_blockchain, add_block, get_block
from prb5 import crear_wallet, validar_registro

app = Flask(__name__)

# Datos simulados de una blockchain (para fines de ejemplo)
blockchain = []

# Usuarios registrados (simulación)
usuarios = {}

# Rutas de la API
@app.route('/registro', methods=['POST'])
def registro():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    wallet = data.get('wallet')
    if username and password and wallet:
        registrar_usuario(username, password, wallet)
        registrar_actividad_css(f"Usuario registrado: {username}")
        return jsonify({"message": "Usuario registrado exitosamente"}), 201
    return jsonify({"error": "Datos incompletos"}), 400

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if verificar_credenciales(username, password):
        registrar_actividad_css(f"Inicio de sesión: {username}")
        return jsonify({"message": "Inicio de sesión exitoso"}), 200
    return jsonify({"error": "Credenciales incorrectas"}), 401

@app.route('/accion', methods=['POST'])
def accion():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    accion = data.get('accion')
    if verificar_credenciales(username, password):
        manejar_accion(username, accion)
        registrar_actividad_css(f"Acción realizada: {accion} por {username}")
        return jsonify({"message": "Acción realizada"}), 200
    return jsonify({"error": "Credenciales incorrectas"}), 401

@app.route('/blockchain', methods=['GET'])
def blockchain_route():
    return jsonify({'blockchain': blockchain})

@app.route('/add_block', methods=['POST'])
def add_block_route():
    return add_block()

@app.route('/block/<int:block_index>', methods=['GET'])
def block_route(block_index):
    return get_block(block_index)

@app.route('/crear_wallet', methods=['POST'])
def crear_wallet_route():
    wallet = crear_wallet()
    registrar_actividad_css(f"Wallet creada: {wallet['id']}")
    return jsonify({"message": "Wallet creada", "wallet": wallet}), 201

@app.route('/validar_registro', methods=['POST'])
def validar_registro_route():
    data = request.get_json()
    forks = data.get('forks')
    valor = validar_registro(forks)
    registrar_actividad_css(f"Registro validado: forks={forks}, valor={valor}")
    return jsonify({"message": "Registro validado", "valor": valor}), 200

# Ruta para la página web
@app.route('/')
def index():
    html_content = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Ejemplo de Aplicación</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <h1>Ejemplo de Aplicación</h1>
        <div id="content">
            <h2>Registro de Usuario</h2>
            <button onclick="generarWallet()">Generar Wallet</button>
            <input type="text" id="wallet" placeholder="Wallet ID" readonly>
            <input type="text" id="username" placeholder="Nombre de usuario">
            <input type="password" id="password" placeholder="Contraseña">
            <input type="text" id="codigo" placeholder="Código Temporal" readonly>
            <button onclick="registrarUsuario()">Registrar</button>

            <h2>Inicio de Sesión</h2>
            <input type="text" id="loginUsername" placeholder="Nombre de usuario">
            <input type="password" id="loginPassword" placeholder="Contraseña">
            <button onclick="iniciarSesion()">Iniciar Sesión</button>

            <h2>Acción de Usuario</h2>
            <input type="text" id="accion" placeholder="Acción (explorar/intercambiar)">
            <button onclick="realizarAccion()">Realizar Acción</button>

            <h2>Blockchain</h2>
            <button onclick="verBlockchain()">Ver Blockchain</button>

            <h2>Crear Wallet</h2>
            <button onclick="crearWallet()">Crear Wallet</button>

            <h2>Validar Registro</h2>
            <input type="number" id="forks" placeholder="Número de forks">
            <button onclick="validarRegistro()">Validar Registro</button>
        </div>
        <script src="/static/script.js"></script>
    </body>
    </html>
    """
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True)
