import time
import random
import string
import prb4

def crear_wallet():
    """
    Crea una nueva wallet con un ID único.
    """
    wallet_id = "wbrs" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=12))
    wallet = {'id': wallet_id, 'timestamp': time.time()}
    prb4.add_block(wallet)
    return wallet

def validar_registro(forks):
    """
    Valida un registro basado en el número de forks.
    """
    valor = forks * 2  # Ejemplo de validación
    registro = {'forks': forks, 'valor': valor, 'timestamp': time.time()}
    prb4.add_block(registro)
    return valor

def guardar_en_json():
    """
    Guarda la blockchain en una carpeta llamada blockchain_JSON en formato JSON.
    """
    prb4.guardar_en_json()
