import hashlib
import datetime
import json
import gzip

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
            'hash_admin': self.hash_block(index, timestamp, data, previous_hash, 'admin'),
            'hash_internal': self.hash_block(index, timestamp, data, previous_hash, 'internal'),
            'size': self.definir_tamano_bloque(data)
        }
        return block

    def agregar_bloque(self, data):
        previous_hash = self.chain[-1]['hash_admin'] if self.chain else "0"
        new_block = self.crear_bloque(len(self.chain), data, previous_hash)
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

    def definir_tamano_bloque(self, data):
        """
        Define el tamaño del bloque basado en la cantidad de datos.
        """
        data_size = len(json.dumps(data).encode('utf-8'))
        if data_size < 1 * 1024 * 1024:  # Menos de 1 MB
            return "1 MB"
        elif data_size > 1 * 1024 * 1024 and data_size < 1 * 1024 * 1024 * 1024:  # Entre 1 MB y 1 GB
            return "1 GB"
        else:
            return "Tamaño variable"

class RecursosUsuario:
    def __init__(self, porcentaje_cpu, porcentaje_ancho_banda):
        self.porcentaje_cpu = porcentaje_cpu
        self.porcentaje_ancho_banda = porcentaje_ancho_banda

    def asignar_recursos(self, recursos_comunitarios):
        """
        Asigna recursos a un usuario basado en los recursos comunitarios.

        Args:
            recursos_comunitarios (dict): Recursos disponibles en la comunidad.

        Returns:
            dict: Recursos asignados al usuario.
        """
        recursos_asignados = {
            'cpu': recursos_comunitarios['cpu'] * (self.porcentaje_cpu / 100),
            'ancho_banda': recursos_comunitarios['ancho_banda'] * (self.porcentaje_ancho_banda / 100),
        }
        log_action(f"Recursos asignados: {recursos_asignados}")
        return recursos_asignados

class MonitoreoRecursos:
    def __init__(self):
        self.recursos_usuarios = {}

    def actualizar_recursos(self, nombre_usuario, uso_cpu, uso_ancho_banda):
        """
        Actualiza el uso de recursos de un usuario.

        Args:
            nombre_usuario (str): Nombre del usuario.
            uso_cpu (float): Porcentaje de uso de CPU.
            uso_ancho_banda (float): Porcentaje de uso de ancho de banda.
        """
        self.recursos_usuarios[nombre_usuario] = {
            'uso_cpu': uso_cpu,
            'uso_ancho_banda': uso_ancho_banda
        }
        log_action(f"Recursos actualizados para {nombre_usuario}: CPU={uso_cpu}%, Ancho de banda={uso_ancho_banda}%")

    def obtener_informacion(self):
        """
        Obtiene la información de uso de recursos de todos los usuarios.

        Returns:
            dict: Información de uso de recursos.
        """
        return self.recursos_usuarios

    @staticmethod
    def inicializar():
        """
        Inicializa los recursos.
        """
        log_action("Recursos inicializados")
        print("Recursos inicializados")

# Funciones de compresión y descompresión
def log_action(data):
    """
    Registra una acción en la blockchain.
    
    Args:
        data (str): Descripción de la acción a registrar.
    """
    new_block = blockchain.crear_bloque(len(blockchain.chain), data, blockchain.chain[-1]['hash_admin'] if blockchain.chain else "0")
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
    recursos_comunitarios = {'cpu': 100, 'ancho_banda': 1000}
    usuario = RecursosUsuario(50, 50)
    recursos_asignados = usuario.asignar_recursos(recursos_comunitarios)
    print(f"Recursos asignados: {recursos_asignados}")

    monitoreo = MonitoreoRecursos()
    monitoreo.actualizar_recursos("usuario1", 30, 200)
    print(f"Información de recursos: {monitoreo.obtener_informacion()}")
    MonitoreoRecursos.inicializar()

    # Confirmar conexión de módulos antes de abrir la plataforma web
    blockchain.confirmar_conexion_modulos(['usuarios', 'recursos', 'database', 'compresion', 'servidor'])
    
    # Ejemplo de registro de usuario y generación de wallet
    wallet = blockchain.registrar_usuario("nombre", "contraseña")
    print(f"Wallet generada: {wallet}")
    
    # Ejemplo de compresión y descompresión de datos
    datos = {"nombre": "ejemplo", "valor": 123}
    archivo = "datos_comprimidos.gz"
    
    comprimir_y_guardar_datos(datos, archivo)
    datos_descomprimidos = cargar_y_descomprimir_datos(archivo)
    
    # Mostrar la cadena de bloques
    blockchain.imprimir_cadena()
    
