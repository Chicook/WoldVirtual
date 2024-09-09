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

@app.route('/')
def index():
    return "El servidor está funcionando correctamente."

if __name__ == '__main__':
    # Ejemplo de registro de usuario
    registrar_usuario("usuario1", "contrasena_segura")
    app.run(debug=True)
