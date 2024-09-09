import random
import time

blockchain = []

def crear_wallet():
    wallet_id = f"wallet_{random.randint(1000, 9999)}"
    wallet = {'id': wallet_id, 'timestamp': time.time()}
    return wallet

def validar_registro(forks):
    # Código para validar el registro
    pass
