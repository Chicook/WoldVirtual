import json
import hashlib

def crear_wallet():
    wallet_id = "bkmv" + hashlib.sha256().hexdigest()[:8]
    wallet = {'id': wallet_id, 'balance': 0}
    with open(f'{wallet_id}.json', 'w') as f:
        json.dump(wallet, f)
    registrar_actividad(f"Wallet creada: {wallet_id}")
    return wallet

def validar_registro(forks):
    if forks == 4:
        valor = 30000000.000
    else:
        valor = 0.001
    registrar_actividad(f"Registro validado: forks={forks}, valor={valor}")
    return valor

def registrar_actividad(actividad):
    new_block = {'index': len(blockchain) + 1, 'data': actividad}
    blockchain.append(new_block)
