import hashlib
import datetime
import json
import gzip
from usuarios import registrar_usuario
from recursos import RecursosUsuario
# from database import conectar_base_datos  # Comentado para futuras implementaciones
from servidor import app, socketio

class Blockchain:
    def __init__(self):
        self.chain = []
        if not self.chain:
            self.crear_bloque_genesis()

    def crear_bloque_genesis(self):
        genesis_block = self.crear_bloque(0, 'Bloque Génesis', '0')
        self.chain.append(genesis_block)

    def crear_bloque(self, index, data, previous_hash):
        timestamp = str(datetime.datetime.now())
        block = {
            'index': index,
            'timestamp': timestamp,
            'data': data,
            'previous_hash': previous_hash,
            'hash_admin': self.hash_block(index, timestamp, data, previous_hash, 'admin'),
            'hash_internal': self.hash_block(index, timestamp, data, previous_hash, 'internal')
        }
        return block

    def agregar_bloque(self, data):
        previous_block = self.chain[-1]
        new_block = self.crear_bloque(len(self.chain), data, previous_block['hash_admin'])
        self.chain.append(new_block)

    def confirmar_conexion_modulos(self, modulos):
        data = f"Conexión de módulos: {', '.join(modulos)}"
        self.agregar_bloque(data)

    def obtener_informacion_cadena(self):
        informacion = {
            'longitud': len(self.chain),
            'bloques': [block for block in self.chain],
        }
        return informacion

    def hash_block(self, index, timestamp, data, previous_hash, hash_type):
        block_string = f"{index}{timestamp}{data}{previous_hash}{hash_type}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def validar_cadena(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block['previous_hash'] != previous_block['hash_admin']:
                return False
            if current_block['hash_admin'] != self.hash_block(current_block['index'], current_block['timestamp'], current_block['data'], previous_block['hash_admin'], 'admin'):
                return False
            if current_block['hash_internal'] != self.hash_block(current_block['index'], current_block['timestamp'], current_block['data'], previous_block['hash_admin'], 'internal'):
                return False
        return True

    def imprimir_cadena(self):
        for block in self.chain:
            print(block)

    def generar_wallet(self, usuario):
        wallet = f"bkvr{hashlib.sha256(usuario.encode()).hexdigest()[:8]}"
        self.agregar_bloque(f"Generada wallet para {usuario}: {wallet}")
        return wallet

    def registrar_usuario(self, nombre, contraseña):
        self.agregar_bloque(f"Usuario registrado: {nombre}")
        return self.generar_wallet(nombre)

# Funciones de compresión y descompresión
def log_action(data):
    """
    Registra una acción en la blockchain.
    
    Args:
        data (str): Descripción de la acción a registrar.
    """
    new_block = blockchain.crear_bloque(len(blockchain.chain), data, blockchain.chain[-1]['hash_admin'])
    blockchain.chain.append(new_block)
    print(f"Acción registrada: {data}")

def comprimir_y_guardar_datos(datos, archivo_salida):
    """
    Comprime y guarda los datos en un archivo.

    Args:
        datos (dict): Datos a comprimir.
        archivo_salida (str): Ruta del archivo de salida.
    """
    try:
        # Serializar y comprimir los datos
        datos_serializados = json.dumps(datos).encode('utf-8')
        datos_comprimidos = gzip.compress(datos_serializados)
        
        # Guardar los datos comprimidos en el archivo
        with open(archivo_salida, 'wb') as archivo:
            archivo.write(datos_comprimidos)
        
        print(f"Datos comprimidos y guardados en {archivo_salida}")
        log_action(f"Datos comprimidos y guardados en {archivo_salida}")
    except Exception as e:
        print(f"Error al comprimir y guardar datos: {e}")

def cargar_y_descomprimir_datos(archivo_entrada):
    """
    Carga y descomprime los datos de un archivo.

    Args:
        archivo_entrada (str): Ruta del archivo de entrada.

    Returns:
        dict: Datos descomprimidos.
    """
    try:
        # Leer y descomprimir los datos del archivo
        with open(archivo_entrada, 'rb') as archivo:
            datos_comprimidos = archivo.read()
        datos_descomprimidos = gzip.decompress(datos_comprimidos)
        
        log_action(f"Datos descomprimidos de {archivo_entrada}")
        return json.loads(datos_descomprimidos)
    except Exception as e:
        print(f"Error al cargar y descomprimir datos: {e}")
        return None

# Inicializar la blockchain
blockchain = Blockchain()

def inicializar_recursos():
    recursos = RecursosUsuario(50, 50)  # Ejemplo de inicialización con 50% de CPU y ancho de banda
    log_action("Recursos inicializados: CPU=50%, Ancho de banda=50%")
    return recursos

# Función de conexión a la base de datos comentada para futuras implementaciones
# def conectar_bd():
#     db = conectar_base_datos()
#     log_action("Conexión a la base de datos establecida")
#     return db

def crear_usuario(nombre, contraseña):
    registrar_usuario(nombre, contraseña)
    log_action(f"Usuario creado: {nombre}")

def comprimir_datos(datos, archivo):
    comprimir_y_guardar_datos(datos, archivo)
    log_action(f"Datos comprimidos y guardados en {archivo}")

def procesar_transaccion(transaccion):
    blockchain.agregar_bloque(transaccion)
    log_action(f"Transacción procesada: {transaccion}")

def iniciar_servidor():
    log_action("Servidor iniciado")
    socketio.run(app, debug=True)

def main():
    """
    Función principal para inicializar recursos, conectar a la base de datos,
    registrar un usuario, comprimir y almacenar datos, procesar transacciones
    en la blockchain e iniciar el servidor.
    """
    recursos_usuario = inicializar_recursos()
    # db = conectar_bd()  # Comentado para futuras implementaciones
    crear_usuario("nombre", "contraseña")

    datos_usuario = {"nombre": "nombre", "datos": "datos_ejemplo"}
    archivo_comprimido = "datos_comprimidos.gz"
    comprimir_datos(datos_usuario, archivo_comprimido)

    procesar_transaccion("transaccion_ejemplo")

    iniciar_servidor()

if __name__ == "__main__":
    main()
