import hashlib
import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []

    def crear_bloque(self, index, data, previous_hash):
        timestamp = str(datetime.datetime.now())
        block = {
            'index': index,
            'timestamp': timestamp,
            'data': data,
            'previous_hash': previous_hash,
            'hash': self.hash_block(index, timestamp, data, previous_hash)
        }
        return block

    def agregar_bloque(self, data):
        previous_hash = self.chain[-1]['hash'] if self.chain else "0"
        new_block = self.crear_bloque(len(self.chain), data, previous_hash)
        self.chain.append(new_block)

    def confirmar_conexion_modulos(self, modulos):
        data = f"Conexión de módulos: {', '.join(modulos)}"
        self.agregar_bloque(data)

    def hash_block(self, index, timestamp, data, previous_hash):
        block_string = f"{index}{timestamp}{data}{previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def imprimir_cadena(self):
        for block in self.chain:
            print(block)

# Inicializar la blockchain
blockchain = Blockchain()

@app.route('/registrar', methods=['POST'])
def registrar():
    data = request.json
    nombre = data['nombre']
    contraseña = data['contraseña']
    blockchain.agregar_bloque(f"Usuario registrado: {nombre}")
    return jsonify({"mensaje": "Usuario registrado exitosamente", "wallet": "0.000 WCV", "usuario": nombre}), 201

@app.route('/verificar', methods=['POST'])
def verificar():
    data = request.json
    nombre = data['nombre']
    # Aquí iría la lógica para verificar el usuario
    blockchain.agregar_bloque(f"Usuario verificado: {nombre}")
    return jsonify({"mensaje": "Usuario verificado"}), 200

@app.route('/eliminar', methods=['DELETE'])
def eliminar():
    data = request.json
    nombre = data['nombre']
    # Aquí iría la lógica para eliminar el usuario
    blockchain.agregar_bloque(f"Usuario eliminado: {nombre}")
    return jsonify({"mensaje": "Usuario eliminado"}), 200

@app.route('/principal', methods=['GET'])
def principal():
    # Aquí iría la lógica para mostrar la página principal con la wallet y la información del usuario
    return jsonify({"mensaje": "Página principal", "wallet": "0.000 WCV", "usuario": "nombre_usuario"}), 200

def iniciar_servidor():
    blockchain.confirmar_conexion_modulos(['usuarios', 'servidor'])
    blockchain.imprimir_cadena()
    app.run(debug=True)

if __name__ == "__main__":
    iniciar_servidor()
