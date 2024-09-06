# modulo Blockchain #

import hashlib
import time
from usuarios import registrar_usuario, manejar_accion
from recursos import RecursosUsuario, MonitoreoRecursos
from database import conectar_base_datos
from compresion import comprimir_y_guardar_datos, cargar_y_descomprimir_datos
from servidor import app, socketio

class Bloque:
    """
    Clase que representa un bloque en la cadena de bloques.
    """
    def __init__(self, index, timestamp, datos, hash_anterior):
        self.index = index
        self.timestamp = timestamp
        self.datos = datos
        self.hash_anterior = hash_anterior
      #  self.hash = self.generar_hash()
        self.nonce = 0

    def generar_hash(self):
        """
        Genera el hash del bloque usando SHA-256.
        """
        sha = hashlib.sha256()
        sha.update((str(self.index) + str(self.timestamp) + str(self.datos) + str(self.hash_anterior) + str(self.nonce)).encode())
        return sha.hexdigest()

    def proof_of_work(self, dificultad):
        """
        Prueba de trabajo para encontrar un hash válido con la dificultad indicada.
        """
        while self.hash[:dificultad] != "0" * dificultad:
            self.nonce += 1
            self.hash = self.generar_hash()

class Blockchain:
    """
    Clase que representa una cadena de bloques.
    """
    def __init__(self):
        self.cadena = [self.crear_bloque_genesis()]
        self.transacciones_pendientes = []

    def crear_bloque_genesis(self):
        """
        Crea el bloque génesis de la cadena.
        """
        return Bloque(0, time.time(), "Bloque Génesis", "0")

    def agregar_bloque(self, datos):
        """
        Agrega un bloque con los datos proporcionados a la cadena.
        """
        ultimo_bloque = self.cadena[-1]
        nuevo_bloque = Bloque(len(self.cadena), time.time(), datos, ultimo_bloque.hash)
        nuevo_bloque.proof_of_work(dificultad=4)  # Ajusta la dificultad según tus necesidades
        self.cadena.append(nuevo_bloque)

    def validar_cadena(self):
        """
        Valida que la cadena de bloques no haya sido manipulada.
        """
        for i in range(1, len(self.cadena)):
            bloque_actual = self.cadena[i]
            bloque_anterior = self.cadena[i - 1]
            if bloque_actual.hash_anterior != bloque_anterior.hash or bloque_actual.hash != bloque_actual.generar_hash():
                return False
        return True

    def confirmar_conexion_modulos(self, modulos):
        """
        Confirma la conexión de los módulos y agrega un bloque con la información.
        
        Args:
            modulos (list): Lista de nombres de los módulos a confirmar.
        """
        data = f"Conexión de módulos: {', '.join(modulos)}"
        self.agregar_bloque(data)

    def imprimir_cadena(self):
        """
        Imprime la cadena de bloques.
        """
        for bloque in self.cadena:
            print(bloque)

def inicializar_recursos(cpu: int = 50, ancho_banda: int = 50):
    """
    Inicializa los recursos asignados a un usuario y devuelve los recursos asignados.
    """
    recursos_usuario = RecursosUsuario(cpu, ancho_banda)
    recursos_comunitarios = {'cpu': 100, 'ancho_banda': 100}
    recursos_asignados = recursos_usuario.asignar_recursos(recursos_comunitarios)
    return recursos_asignados

def procesar_transacciones(datos_usuario, blockchain):
    """
    Procesa las transacciones de usuario en la cadena de bloques.
    """
    blockchain.agregar_bloque(datos_usuario)

def gestionar_compresion(datos_usuario, archivo_comprimido):
    """
    Comprime y descomprime los datos del usuario para su almacenamiento.
    """
    comprimir_y_guardar_datos(datos_usuario, archivo_comprimido)
    datos_descomprimidos = cargar_y_descomprimir_datos(archivo_comprimido)
    return datos_descomprimidos

def main():
    """
    Función principal para ejecutar la aplicación.
    """
    try:
        # Inicialización de recursos
        recursos_asignados = inicializar_recursos()

        # Conexión a la base de datos
        conectar_base_datos()

        # Registro de un nuevo usuario
        registrar_usuario("nombre", "contraseña")

        # Compresión y almacenamiento de datos
        datos_usuario = {"nombre": "nombre", "datos": "datos_ejemplo"}
        archivo_comprimido = "datos_comprimidos.gz"
        datos_descomprimidos = gestionar_compresion(datos_usuario, archivo_comprimido)

        # Procesamiento de transacciones en la blockchain
        blockchain = Blockchain()
        procesar_transacciones("transaccion_ejemplo", blockchain)

        # Iniciar el servidor con Flask y SocketIO
        socketio.run(app, debug=True)

    except Exception as e:
        print(f"Error durante la ejecución: {e}")

if __name__ == "__main__":
    main()
    
# modulo Blockchain #

# import hashlib
# import datetime

# class Blockchain:
   # def __init__(self):
        # self.chain = []
        # self.crear_bloque_genesis()

   #  def crear_bloque_genesis(self):
       # genesis_block = self.crear_bloque(0, 'Bloque Génesis', '0')
       # self.chain.append(genesis_block)

   # def crear_bloque(self, index, data, previous_hash):
       # timestamp = str(datetime.datetime.now())
      #  block = {
          #  'index': index,
         #   'timestamp': timestamp,
         #   'data': data,
          #  'previous_hash': previous_hash,
          #  'hash': self.hash_block(index, timestamp, data, previous_hash)
      #  }
       # return block

   # def agregar_bloque(self, data):
      #  previous_block = self.chain[-1]
      #  new_block = self.crear_bloque(len(self.chain), data, previous_block['hash'])
       # self.chain.append(new_block)

   # def confirmar_conexion_modulos(self, modulos):
       # """
       # Confirma la conexión de los módulos y agrega un bloque con la información.
        
       # Args:
          #  modulos (list): Lista de nombres de los módulos a confirmar.
     #   """
      #  data = f"Conexión de módulos: {', '.join(modulos)}"
      #  self.agregar_bloque(data)

  #  def obtener_informacion_cadena(self):
      #  informacion = {
         #   'longitud': len(self.chain),
          #  'bloques': [block for block in self.chain],
     #   }
      #  return informacion

  #  def hash_block(self, index, timestamp, data, previous_hash):
      #  block_string = f"{index}{timestamp}{data}{previous_hash}"
       # return hashlib.sha256(block_string.encode()).hexdigest()

  #  def validar_cadena(self):
      #  for i in range(1, len(self.chain)):
           # current_block = self.chain[i]
         #   previous_block = self.chain[i - 1]
          #  if current_block['previous_hash'] != previous_block['hash']:
              #  return False
           # if current_block['hash'] != self.hash_block(current_block['index'], current_block['timestamp'], current_block['data'], previous_block['hash']):
               # return False
      #  return True

    # def imprimir_cadena(self):
       # for block in self.chain:
          #  print(block)

# Ejemplo de uso
# if __name__ == "__main__":
  #  blockchain = Blockchain()
  #  blockchain.confirmar_conexion_modulos(['usuarios', 'recursos', 'database', 'compresion', 'servidor'])
 #   blockchain.imprimir_cadena()

# blockchain.py

# import hashlib
# import datetime

# class Blockchain:
   # def __init__(self):
       # self.chain = []
       # self.crear_bloque_genesis()

   # def crear_bloque_genesis(self):
       # genesis_block = {
          #  'index': 0,
          #  'timestamp': str(datetime.datetime.now()),
           # 'data': 'Bloque Génesis',
           # 'previous_hash': '0',
           # 'hash': self.hash_block(0, str(datetime.datetime.now()), 'Bloque Génesis', '0')
      #  }
      #  self.chain.append(genesis_block)

   # def agregar_bloque(self, data):
       # previous_block = self.chain[-1]
       # new_block = {
            #'index': len(self.chain),
           # 'timestamp': str(datetime.datetime.now()),
           # 'data': data,
          #  'previous_hash': previous_block['hash'],
          #  'hash': self.hash_block(len(self.chain), str(datetime.datetime.now()), data, previous_block['hash'])
      #  }
        # self.chain.append(new_block)

    # def obtener_informacion_cadena(self):
      #  informacion = {
           # 'longitud': len(self.chain),
          #  'bloques': [block for block in self.chain],
       # }
       # return informacion

   # def hash_block(self, index, timestamp, data, previous_hash):
       # block_string = f"{index}{timestamp}{data}{previous_hash}"
       # return hashlib.sha256(block_string.encode()).hexdigest()

   # def validar_cadena(self):
        # for i in range(1, len(self.chain)):
            # current_block = self.chain[i]
           #  previous_block = self.chain[i - 1]
           # if current_block['previous_hash'] != previous_block['hash']:
               # return False
           # if current_block['hash'] != self.hash_block(current_block['index'], current_block['timestamp'], current_block['data'], previous_block['hash']):
                # return False
        # return True

    # def imprimir_cadena(self):
       #  for block in self.chain:
           #  print(block)
    
