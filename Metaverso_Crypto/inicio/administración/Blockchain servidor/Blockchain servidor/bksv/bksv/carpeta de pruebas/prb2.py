import hashlib
from prb5 import blockchain

# Usuarios registrados (simulación)
usuarios = {}

def registrar_usuario(username, password, wallet_id):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    usuarios[username] = {'password': hashed_password, 'wallet': wallet_id}
    registrar_actividad_css(f"Usuario registrado: {username}")

def verificar_credenciales(username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return usuarios.get(username, {}).get('password') == hashed_password

def registrar_actividad_css(actividad):
    new_block = {'index': len(blockchain) + 1, 'data': actividad, 'hash': hashlib.sha256(actividad.encode()).hexdigest()}
    blockchain.append(new_block)
