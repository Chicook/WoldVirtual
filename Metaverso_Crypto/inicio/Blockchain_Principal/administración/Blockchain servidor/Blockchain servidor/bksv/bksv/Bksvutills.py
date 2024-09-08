import json
import time
import random
from blockchain import Blockchain

# Inicializar la blockchain
blockchain = Blockchain()

def log_action(data):
    new_block = blockchain.crear_bloque(len(blockchain.chain), data, blockchain.chain[-1]['hash_admin'] if blockchain.chain else "0")
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
    blockchain.agregar_bloque(data)
                                                
