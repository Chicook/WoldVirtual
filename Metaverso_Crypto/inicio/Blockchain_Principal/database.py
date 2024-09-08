import hashlib
import datetime
import json
import gzip

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []

    def crear_bloque(self, index, data, previous_hash):
        timestamp = str(datetime.datetime.now())
        block = {
            'index': index,
            'timestamp': timestamp,
            'data': data,
            'previous_hash': previous_hash,
            'hash': self.hash_block(index, timestamp, data, previous_hash)
        }
        return block

    def agregar_bloque(self, data):
        previous_hash = self.chain[-1]['hash'] if self.chain else "0"
        new_block = self.crear_bloque(len(self.chain), data, previous_hash)
        self.chain.append(new_block)

    def confirmar_conexion_modulos(self, modulos):
        data = f"Conexión de módulos: {', '.join(modulos)}"
        self.agregar_bloque(data)

    def hash_block(self, index, timestamp, data, previous_hash):
        block_string = f"{index}{timestamp}{data}{previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()

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
    new_block = blockchain.crear_bloque(len(blockchain.chain), data, blockchain.chain[-1]['hash'] if blockchain.chain else "0")
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

# Ejemplo de uso
if __name__ == "__main__":
    # Confirmar conexión de módulos antes del registro
    blockchain.confirmar_conexion_modulos(['servidor', 'usuarios'])
    
    # Ejemplo de registro de usuario y generación de wallet
    wallet = blockchain.registrar_usuario("nombre", "contraseña")
    print(f"Wallet generada: {wallet}")
    
    # Confirmar conexión de módulos tras el registro
    blockchain.confirmar_conexion_modulos(['usuarios', 'recursos', 'database', 'compresion', 'servidor'])
    
    # Ejemplo de compresión y descompresión de datos
    datos = {"nombre": "ejemplo", "valor": 123}
    archivo = "datos_comprimidos.gz"
    
    comprimir_y_guardar_datos(datos, archivo)
    datos_descomprimidos = cargar_y_descomprimir_datos(archivo)
    
    # Mostrar la cadena de bloques
    blockchain.imprimir_cadena()
