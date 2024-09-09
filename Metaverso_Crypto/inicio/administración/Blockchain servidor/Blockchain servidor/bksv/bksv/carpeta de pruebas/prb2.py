from flask import Flask, jsonify, request, render_template_string
import hashlib
import json
import time
import random

app = Flask(__name__)

# Datos simulados de una blockchain (para fines de ejemplo)
blockchain = []

# Usuarios registrados (simulación)
usuarios = {}

# Funciones de blockchain
def registrar_actividad(actividad):
    new_block = {'index': len(blockchain) + 1, 'data': actividad}
    blockchain.append(new_block)

# Funciones de registro y verificación
def registrar_usuario(username, password, wallet_id):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    usuarios[username] = {'password': hashed_password, 'wallet': wallet_id}

def verificar_credenciales(username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return usuarios.get(username, {}).get('password') == hashed_password

# Generar código temporal
def generar_codigo_temporal():
    return random.randint(100000, 999999)

# HTML, CSS y JavaScript
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
    <script>
        let codigoTemporal;
        let timer;

        function generarWallet() {
            const walletId = "bkmv" + Math.random().toString(36).substring(2, 10);
            document.getElementById('wallet').value = walletId;
            generarCodigoTemporal();
        }

        function generarCodigoTemporal() {
            clearInterval(timer);
            codigoTemporal = Math.floor(100000 + Math.random() * 900000);
            document.getElementById('codigo').value = codigoTemporal;
            timer = setInterval(generarCodigoTemporal, 30000);
        }

        async function registrarUsuario() {
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;
            const wallet = document.getElementById('wallet').value;
            const codigo = document.getElementById('codigo').value;
            if (codigo != codigoTemporal) {
                alert("Código temporal incorrecto");
                return;
            }
            const response = await fetch('/registro', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ username, password, wallet })
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

@app.route('/')
def index():
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True)
