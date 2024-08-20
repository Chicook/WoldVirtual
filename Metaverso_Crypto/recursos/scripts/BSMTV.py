from flask import Flask, jsonify, request
import hashlib

app = Flask(__name__)

# Datos simulados de una blockchain (para fines de ejemplo)
blockchain = []

# Usuarios registrados (simulación)
usuarios = {}

def registrar_usuario(username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    usuarios[username] = hashed_password

def verificar_credenciales(username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return usuarios.get(username) == hashed_password

def manejar_accion(usuario, accion):
    if accion == "explorar":
        print(f"Bienvenido/a {usuario} al entorno de exploración.")
    elif accion == "intercambiar":
        print(f"Realizando intercambio para {usuario}.")
    else:
        print("Acción no reconocida.")

@app.route('/')
def index():
    return "El servidor está funcionando correctamente."

@app.route('/blockchain', methods=['GET'])
def get_blockchain():
    return jsonify({'blockchain': blockchain})

@app.route('/add_block', methods=['POST'])
def add_block():
    data = request.get_json()
    if 'data' in data:
        new_block = {'index': len(blockchain) + 1, 'data': data['data']}
        blockchain.append(new_block)
        return jsonify({'message': 'Bloque agregado correctamente', 'block': new_block})
    else:
        return jsonify({'error': 'Datos no proporcionados'})

@app.route('/block/<int:block_index>', methods=['GET'])
def get_block(block_index):
    if 0 < block_index <= len(blockchain):
        return jsonify({'block': blockchain[block_index - 1]})
    else:
        return jsonify({'error': 'Índice de bloque inválido'})

if __name__ == '__main__':
    # Ejemplo de registro de usuario
    registrar_usuario("usuario1", "contrasena_segura")

    # Ejemplo de verificación de credenciales y manejo de entorno virtual
    usuario_actual = "usuario1"
    contrasena_ingresada = "contrasena_segura"

    if verificar_credenciales(usuario_actual, contrasena_ingresada):
        print("Inicio de sesión exitoso")
        accion_usuario = "explorar"
        manejar_accion(usuario_actual, accion_usuario)
    else:
        print("Credenciales incorrectas")

    app.run(debug=True)
