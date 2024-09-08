from flask import Flask, render_template_string, request, redirect, url_for
from flask_socketio import SocketIO
import hashlib
import time
import random
from blockchain import Blockchain

app = Flask(__name__)
socketio = SocketIO(app)

# Inicializar la blockchain
blockchain = Blockchain()

# Diccionario para almacenar usuarios y contraseñas
usuarios = {}

# Diccionario para almacenar códigos temporales de verificación
codigos_temporales = {}

def log_action(data):
    """
    Registra una acción en la blockchain.
    
    Args:
        data (str): Descripción de la acción a registrar.
    """
    new_block = blockchain.crear_bloque(len(blockchain.chain), data, blockchain.chain[-1]['hash_admin'])
    blockchain.chain.append(new_block)
    print(f"Acción registrada: {data}")

def generar_codigo_temporal():
    """
    Genera un código temporal de verificación de 30 segundos de duración.
    
    Returns:
        str: Código temporal de verificación.
    """
    codigo = str(random.randint(100000, 999999))
    timestamp = time.time()
    codigos_temporales[codigo] = timestamp
    return codigo

def verificar_codigo_temporal(codigo):
    """
    Verifica si el código temporal es válido.
    
    Args:
        codigo (str): Código temporal de verificación.
    
    Returns:
        bool: True si el código es válido, False en caso contrario.
    """
    timestamp = codigos_temporales.get(codigo)
    if timestamp and time.time() - timestamp < 30:
        return True
    return False

def registrar_usuario(username, password):
    """
    Registra un nuevo usuario con una contraseña encriptada.

    Args:
        username (str): Nombre de usuario.
        password (str): Contraseña del usuario.

    Raises:
        ValueError: Si el usuario ya existe.
    """
    if username in usuarios:
        raise ValueError("El usuario ya existe.")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    usuarios[username] = hashed_password
    log_action(f"Usuario registrado: {username}")
    print(f"Usuario {username} registrado con éxito.")

def generar_wallet(username):
    """
    Genera una wallet para el usuario.

    Args:
        username (str): Nombre de usuario.

    Returns:
        str: Wallet generada.
    """
    wallet = f"bkvr{hashlib.sha256(username.encode()).hexdigest()[:8]}"
    log_action(f"Wallet generada para {username}: {wallet}")
    return wallet

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registro de Usuario</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f9f9f9; }
        .header { background-color: #4CAF50; color: white; padding: 15px 0; text-align: center; }
        .container { margin: 20px auto; padding: 20px; max-width: 400px; background-color: #fff; border-radius: 8px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); }
        .form-group { margin-bottom: 15px; }
        label { display: block; margin-bottom: 5px; }
        input[type="text"], input[type="password"] { width: 100%; padding: 8px; box-sizing: border-box; }
        .button { background-color: #4CAF50; border: none; color: white; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; border-radius: 4px; }
        .button:hover { background-color: #45a049; }
    </style>
</head>
<body>
    <div class="header"><h1>Registro de Usuario</h1></div>
    <div class="container">
        <form method="POST" action="/register">
            <div class="form-group">
                <label for="wallet">Generar Wallet</label>
                <button type="button" class="button" onclick="generarWallet()">Generar Wallet</button>
                <input type="text" id="wallet" name="wallet" readonly>
            </div>
            <div class="form-group">
                <label for="username">Nombre de Usuario</label>
                <input type="text" id="username" name="username" required>
            </div>
            <div class="form-group">
                <label for="password">Contraseña</label>
                <input type="password" id="password" name="password" required>
            </div>
            <div class="form-group">
                <label for="codigo">Código Temporal de Verificación</label>
                <input type="text" id="codigo" name="codigo" required>
                <button type="button" class="button" onclick="generarCodigo()">Generar Código</button>
            </div>
            <button type="submit" class="button">Registrar</button>
        </form>
    </div>
    <script>
        function generarWallet() {
            fetch('/generate_wallet')
                .then(response => response.json())
                .then(data => {
                    document.getElementById('wallet').value = data.wallet;
                });
        }

        function generarCodigo() {
            fetch('/generate_code')
                .then(response => response.json())
                .then(data => {
                    alert('Código generado: ' + data.codigo);
                });
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    log_action("Página principal cargada")
    return render_template_string(html_template)

@app.route('/generate_wallet', methods=['GET'])
def generate_wallet():
    wallet = generar_wallet("usuario_temporal")
    return {'wallet': wallet}

@app.route('/generate_code', methods=['GET'])
def generate_code():
    codigo = generar_codigo_temporal()
    return {'codigo': codigo}

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    codigo = request.form['codigo']
    
    if verificar_codigo_temporal(codigo):
        try:
            registrar_usuario(username, password)
            wallet = generar_wallet(username)
            log_action(f"Usuario {username} registrado con wallet {wallet}")
            return redirect(url_for('index'))
        except ValueError as e:
            return str(e)
    else:
        return "Código de verificación inválido o expirado."

if __name__ == '__main__':
    log_action("Servidor iniciado")
    socketio.run(app, debug=True)
