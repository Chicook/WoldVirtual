import hashlib
import time
import random
from Metaverso_Crypto.inicio.Zona_depruebas.webadministrativa.Blockchain_Principal.Zona_de_pruebas.admin.pruebas2.Bk_Servidor.BK_dbts.src.BK_Scv.BK_Blockchain import Blockchain

# Inicializar la blockchain
blockchain = Blockchain()

# Diccionario para almacenar usuarios y contraseñas
usuarios = {}

# Diccionario para almacenar códigos temporales de verificación
codigos_temporales = {}

# Diccionario para almacenar balances de usuarios
balances = {"usuario1": 30000000.000}

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

def registrar_usuario(username, password):
    if username in usuarios:
        raise ValueError("El usuario ya existe.")
    usuarios[username] = hashlib.sha256(password.encode()).hexdigest()
    balances[username] = 0.000
    log_action(f"Usuario registrado: {username}")

def generar_wallet(username):
    wallet = f"bkvr{hashlib.sha256(username.encode()).hexdigest()[:8]}"
    log_action(f"Wallet generada para {username}: {wallet}")
    return wallet

def enviar_wcv(sender, receiver, amount):
    if balances[sender] < amount or receiver not in balances:
        raise ValueError("Balance insuficiente o receptor no existe.")
    balances[sender] -= amount
    balances[receiver] += amount
    log_action(f"{sender} envió {amount} WCV a {receiver}")
    
