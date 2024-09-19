# Simulación de base de datos en memoria
users_db = {}

def add_user(username, wallet, password_hash, user_hash, password_wallet_hash):
    users_db[username] = {
        'username': username,
        'wallet': wallet,
        'password_hash': password_hash,
        'user_hash': user_hash,
        'password_wallet_hash': password_wallet_hash
    }

def delete_user(username):
    if username in users_db:
        del users_db[username]

def get_all_users():
    return list(users_db.values())
