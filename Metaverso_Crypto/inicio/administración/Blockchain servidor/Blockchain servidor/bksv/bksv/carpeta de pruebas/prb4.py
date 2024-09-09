import hashlib
import time
import json
import os

blockchain = []

def registrar_actividad_css(actividad):
    """
    Registra una actividad en la blockchain.
    """
    data = {
        'actividad': actividad,
        'timestamp': time.time()
    }
    add_block(data)

def add_block(data):
    """
    Añade un bloque a la blockchain.
    """
    previous_hash = blockchain[-1]['hash'] if blockchain else '0'
    block = {
        'index': len(blockchain) + 1,
        'timestamp': time.time(),
        'data': data,
        'previous_hash': previous_hash,
        'hash': hash_block(data, previous_hash)
    }
    blockchain.append(block)
    guardar_en_json()
    return block

def hash_block(data, previous_hash):
    """
    Genera el hash de un bloque.
    """
    block_string = f"{data}{previous_hash}{time.time()}"
    return hashlib.sha256(block_string.encode()).hexdigest()

def get_blockchain():
    """
    Devuelve la blockchain completa.
    """
    return blockchain

def get_block(index):
    """
    Devuelve un bloque específico de la blockchain.
    """
    if 0 <= index < len(blockchain):
        return blockchain[index]
    return None

def guardar_en_json():
    """
    Guarda la blockchain en una carpeta llamada blockchain_JSON en formato JSON.
    """
    if not os.path.exists('blockchain_JSON'):
        os.makedirs('blockchain_JSON')
    
    with open('blockchain_JSON/blockchain.json', 'w') as file:
        json.dump(blockchain, file, indent=4)
