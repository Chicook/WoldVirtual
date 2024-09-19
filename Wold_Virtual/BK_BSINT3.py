import hashlib
import time
from BK_BSINT4 import users_db
from BK_BSINT5 import add_block
from flask_socketio import emit

def handle_register(data):
    username = data['username']
    password = data['password']
    wallet = data['wallet']

    if username in users_db:
        emit('registration_failed', {'message': 'Usuario ya registrado'})
        return

    # Generar hashes
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    user_hash = hashlib.sha256((username + wallet).encode()).hexdigest()
    password_wallet_hash = hashlib.sha256((password + wallet).encode()).hexdigest()

    # Almacenar en la base de datos simulada
    users_db[username] = {
        'username': username,
        'wallet': wallet,
        'password_hash': password_hash,
        'user_hash': user_hash,
        'password_wallet_hash': password_wallet_hash
    }

    # Crear un nuevo bloque en la blockchain
    block_data = {
        'user_hash': user_hash,
        'password_wallet_hash': password_wallet_hash,
        'timestamp': time.time()
    }
    add_block(block_data)

    emit('registration_success')

def handle_delete_user(data):
    username = data['username']
    if username in users_db:
        del users_db[username]
        emit('user_deleted')