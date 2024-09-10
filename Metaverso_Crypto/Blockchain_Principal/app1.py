import os
import tarfile
import hashlib
import time
from flask import Flask, request, jsonify
from flask_socketio import SocketIO

# Ruta donde se almacenan los archivos comprimidos y descomprimidos
storage_path = '/workspaces/WoldVirtual.github.io/Metaverso_Crypto/inicio/Blockchain_Principal/Almacenamiento'

app = Flask(__name__)
socketio = SocketIO(app)

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

    def get_latest_block(self):
        return self.chain[-1] if self.chain else None

    def add_block(self, new_block):
        if self.chain:
            new_block.previous_hash = self.get_latest_block().hash
        else:
            new_block.previous_hash = "0"
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

# Inicializar la blockchain
blockchain = Blockchain()

def log_action(data):
    """
    Registra una acción en la blockchain.
    
    Args:
        data (str): Descripción de la acción a registrar.
    """
    new_block = Block(len(blockchain.chain), time.time(), data, blockchain.get_latest_block().hash if blockchain.chain else "0")
    blockchain.add_block(new_block)
    print(f"Acción registrada: {data}")

def comprimir_datos(datos, archivo):
    output_filepath = os.path.join(storage_path, archivo)
    with tarfile.open(output_filepath, 'w:gz') as tar:
        for file in datos:
            if os.path.isfile(file):
                tar.add(file, arcname=os.path.basename(file))
    log_action(f"Datos comprimidos en {archivo}")

def descomprimir_datos(archivo):
    input_filepath = os.path.join(storage_path, archivo)
    with tarfile.open(input_filepath, 'r:gz') as tar:
        tar.extractall(path=storage_path)
    log_action(f"Datos descomprimidos de {archivo}")

def procesar_transaccion(transaccion):
    log_action(f"Procesada transacción: {transaccion}")

@app.route('/registrar', methods=['POST'])
def registrar():
    data = request.json
    nombre = data['nombre']
    contraseña = data['contraseña']
    log_action(f"Usuario registrado: {nombre}")
    return jsonify({"mensaje": "Usuario registrado exitosamente"}), 201

@app.route('/verificar', methods=['POST'])
def verificar():
    data = request.json
    nombre = data['nombre']
    # Aquí iría la lógica para verificar el usuario
    log_action(f"Usuario verificado: {nombre}")
    return jsonify({"mensaje": "Usuario verificado"}), 200

@app.route('/eliminar', methods=['DELETE'])
def eliminar():
    data = request.json
    nombre = data['nombre']
    # Aquí iría la lógica para eliminar el usuario
    log_action(f"Usuario eliminado: {nombre}")
    return jsonify({"mensaje": "Usuario eliminado"}), 200

def iniciar_servidor():
    log_action("Servidor iniciado")
    socketio.run(app, debug=True)

def main():
    """
    Función principal para registrar un usuario, comprimir y almacenar datos,
    procesar transacciones en la blockchain e iniciar el servidor.
    """
    datos_usuario = ["file1.txt", "file2.txt"]
    archivo_comprimido = "datos_comprimidos.gz"
    comprimir_datos(datos_usuario, archivo_comprimido)

    descomprimir_datos(archivo_comprimido)

    procesar_transaccion("transaccion_ejemplo")

    iniciar_servidor()

if __name__ == "__main__":
    main()
