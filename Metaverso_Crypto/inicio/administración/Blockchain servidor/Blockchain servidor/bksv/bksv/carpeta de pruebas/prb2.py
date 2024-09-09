import hashlib
import random

# Datos simulados de una blockchain (para fines de ejemplo)
blockchain = []

# Usuarios registrados (simulación)
usuarios = {}

# Funciones de blockchain
def registrar_actividad_css(actividad):
    new_block = {'index': len(blockchain) + 1, 'data': actividad, 'hash': hashlib.sha256(actividad.encode()).hexdigest()}
    blockchain.append(new_block)

# Funciones de registro y verificación
def registrar_usuario(username, password, wallet_id):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    usuarios[username] = {'password': hashed_password, 'wallet': wallet_id}
    registrar_actividad_css(f"Usuario registrado: {username}")

def verificar_credenciales(username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return usuarios.get(username, {}).get('password') == hashed_password

# Generar código temporal
def generar_codigo_temporal():
    return random.randint(100000, 999999)

# CSS
css_content = """
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
"""

@app.route('/static/style.css')
def style_css():
    return css_content
    
