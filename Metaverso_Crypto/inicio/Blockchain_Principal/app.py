import os
import tarfile
import hashlib
import time
from usuarios import registrar_usuario
from recursos import RecursosUsuario
from database import conectar_base_datos
from servidor import app, socketio

# Ruta donde se almacenan los archivos comprimidos y descomprimidos
storage_path = '/workspaces/WoldVirtual.github.io/Metaverso_Crypto/inicio/Blockchain_Principal/Almacenamiento'

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
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, time.time(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
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
    new_block = Block(len(blockchain.chain), time.time(), data, blockchain.get_latest_block().hash)
    blockchain.add_block(new_block)
    print(f"Acción registrada: {data}")

def inicializar_recursos(cpu, ancho_banda):
    recursos = RecursosUsuario(cpu, ancho_banda)
    log_action(f"Inicializados recursos: CPU={cpu}, Ancho de banda={ancho_banda}")
    return recursos

def conectar_bd():
    db = conectar_base_datos()
    log_action("Conectada a la base de datos")
    return db

def crear_usuario(nombre, contraseña):
    registrar_usuario(nombre, contraseña)
    log_action(f"Usuario creado: {nombre}")

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

def iniciar_servidor():
    log_action("Servidor iniciado")
    socketio.run(app, debug=True)

def main():
    """
    Función principal para inicializar recursos, conectar a la base de datos,
    registrar un usuario, comprimir y almacenar datos, procesar transacciones
    en la blockchain e iniciar el servidor.
    """
    recursos_usuario = inicializar_recursos(50, 50)
    db = conectar_bd()
    crear_usuario("nombre", "contraseña")

    datos_usuario = ["file1.txt", "file2.txt"]
    archivo_comprimido = "datos_comprimidos.gz"
    comprimir_datos(datos_usuario, archivo_comprimido)

    descomprimir_datos(archivo_comprimido)

    procesar_transaccion("transaccion_ejemplo")

    iniciar_servidor()

if __name__ == "__main__":
    main()
