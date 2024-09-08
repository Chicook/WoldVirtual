import json
import time
import random
from blockchain import Blockchain

# Inicializar la blockchain
blockchain = Blockchain()
codigos_temporales = {}

def log_action(data):
    new_block = blockchain.new_block(len(blockchain.chain), data, blockchain.chain[-1]['previous_hash'] if blockchain.chain else "0")
    blockchain.chain.append(new_block)
    print(f"Acción registrada: {data}")

def generar_codigo_temporal():
    codigo = str(random.randint(100000, 999999))
    codigos_temporales[codigo] = time.time()
    return codigo

def verificar_codigo_temporal(codigo):
    return time.time() - codigos_temporales.get(codigo, 0) < 30

def confirmar_conexion_modulos(modulos):
    data = f"Conexión de módulos: {', '.join(modulos)}"
    blockchain.new_block(data)
