from flask import Flask, jsonify, request, render_template_string
import hashlib
import json

# Importar funciones de otros módulos
from prb2 import registrar_usuario, verificar_credenciales
from prb3 import manejar_accion
from prb4 import get_blockchain, add_block, get_block
from prb5 import crear_wallet, validar_registro

app = Flask(__name__)

# Datos simulados de una blockchain (para fines de ejemplo)
blockchain = []

# Usuarios registrados (simulación)
usuarios = {}

# Funciones de blockchain
def registrar_actividad(actividad):
    new_block = {'index': len(blockchain) + 1, 'data': actividad}
    blockchain.append(new_block)

# Rutas de la API
@app.route('/registro', methods=['POST'])
def registro():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if username and password:
        registrar_usuario(username, password)
        registrar_actividad(f"Usuario registrado: {username}")
        return jsonify({"message": "Usuario registrado exitosamente"}), 201
    return jsonify({"error": "Datos incompletos"}), 400

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if verificar_credenciales(username, password):
        registrar_actividad(f"Inicio de sesión: {username}")
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
        registrar_actividad(f"Acción realizada: {accion} por {username}")
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
    registrar_actividad(f"Wallet creada: {wallet['id']}")
    return jsonify({"message": "Wallet creada", "wallet": wallet}), 201

@app.route('/validar_registro', methods=['POST'])
def validar_registro_route():
    data = request.get_json()
    forks = data.get('forks')
    valor = validar_registro(forks)
    registrar_actividad(f"Registro validado: forks={forks}, valor={valor}")
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
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 20px;
            }
            h1, h2 {
                color: #333;
            }
            #content {
                max-width: 600px;
                margin: auto;
            }
            input {
                display: block;
                margin-bottom: 10px;
                padding: 8px;
                width: 100%;
                box-sizing: border-box;
            }
            button {
                padding: 10px 15px;
                background-color: #007BFF;
                color: white;
                border: none;
                cursor: pointer;
            }
            button:hover {
                background-color: #0056b3;
            }
        </style>
    </head>
    <body>
        <h1>Ejemplo de Aplicación</h1>
        <div id="content">
            <h2>Registro de Usuario</h2>
            <input type="text" id="username" placeholder="Nombre de usuario">
            <input type="password" id="password" placeholder="Contraseña">
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
        <script>
            async function registrarUsuario() {
                const username = document.getElementById('username').value;
                const password = document.getElementById('password').value;
                const response = await fetch('/registro', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ username, password })
                });
                const data = await response.json();
                alert(data.message);
            }

            async function iniciarSesion() {
                const username = document.getElementById('loginUsername').value;
                const password = document.getElementById('loginPassword').value;
                const response = await fetch('/login', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ username, password })
                });
                const data = await response.json();
                alert(data.message);
            }

            async function realizarAccion() {
                const username = document.getElementById('loginUsername').value;
                const password = document.getElementById('loginPassword').value;
                const accion = document.getElementById('accion').value;
                const response = await fetch('/accion', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ username, password, accion })
                });
                const data = await response.json();
                alert(data.message);
            }

            async function verBlockchain() {
                const response = await fetch('/blockchain');
                const data = await response.json();
                alert(JSON.stringify(data.blockchain, null, 2));
            }

            async function crearWallet() {
                const response = await fetch('/crear_wallet', {
                    method: 'POST'
                });
                const data = await response.json();
                alert(data.message);
            }

            async function validarRegistro() {
                const forks = document.getElementById('forks').value;
                const response = await fetch('/validar_registro', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ forks })
                });
                const data = await response.json();
                alert(data.message);
            }
        </script>
    </body>
    </html>
    """
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True)
