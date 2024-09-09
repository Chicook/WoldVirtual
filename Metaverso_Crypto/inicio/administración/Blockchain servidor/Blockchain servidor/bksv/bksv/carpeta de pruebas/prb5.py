import hashlib
import json

def validar_datos():
    # Código para validar datos con JavaScript
    pass

def generar_hash(datos):
    return hashlib.sha256(json.dumps(datos, sort_keys=True).encode()).hexdigest()

def crear_bloque(datos, bloque_anterior):
    bloque = {
        'datos': datos,
        'hash_anterior': bloque_anterior['hash'],
        'hash': generar_hash(datos)
    }
    return bloque

def guardar_bloque(bloque, ruta):
    with open(ruta, 'w') as archivo:
        json.dump(bloque, archivo)
