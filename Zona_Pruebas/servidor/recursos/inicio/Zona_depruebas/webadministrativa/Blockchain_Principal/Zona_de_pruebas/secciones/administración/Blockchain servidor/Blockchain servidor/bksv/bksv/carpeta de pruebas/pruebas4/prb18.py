import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

def calculate_hash(index, previous_hash, timestamp, data):
    value = str(index) + str(previous_hash) + str(timestamp) + str(data)
    return hashlib.sha256(value.encode('utf-8')).hexdigest()

def create_block(index, previous_hash, data):
    timestamp = int(time.time())
    hash = calculate_hash(index, previous_hash, timestamp, data)
    return Block(index, previous_hash, timestamp, data, hash)

def explain_prb2():
    print("Sección prb2: Creación de Bloques")
    print("Funciones:")
    print("1. Block: Clase que representa un bloque en la blockchain.")
    print("2. calculate_hash: Función para calcular el hash de un bloque.")
    print("3. create_block: Función para crear un nuevo bloque.")
    input("Presione Enter para volver al menú principal...")
    
