# modulo Blockchain #

import hashlib
import time
from database import insertar_bloque, insertar_transaccion

class Bloque:
    """
    Clase que representa un bloque en la cadena de bloques.
    """
    def __init__(self, index, timestamp, datos, hash_anterior):
        self.index = index
        self.timestamp = timestamp
        self.datos = datos
        self.hash_anterior = hash_anterior
        self.nonce = 0
        self.hash = self.generar_hash()

    def generar_hash(self):
        """
        Genera el hash del bloque usando SHA-256.
        """
        sha = hashlib.sha256()
        sha.update((str(self.index) + str(self.timestamp) + str(self.datos) + str(self.hash_anterior) + str(self.nonce)).encode())
        return sha.hexdigest()

    def proof_of_work(self, dificultad=4):
        """
        Realiza una prueba de trabajo (Proof of Work) para encontrar un hash válido con la dificultad indicada.
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
        Crea el bloque génesis (el primer bloque de la cadena).
        """
        bloque_genesis = Bloque(0, time.time(), "Bloque Génesis", "0")
        bloque_genesis.proof_of_work()
        return bloque_genesis

    def agregar_bloque(self, datos):
        """
        Agrega un nuevo bloque con los datos proporcionados a la cadena de bloques.
        """
        ultimo_bloque = self.cadena[-1]
        nuevo_bloque = Bloque(len(self.cadena), time.time(), datos, ultimo_bloque.hash)
        nuevo_bloque.proof_of_work(dificultad=4)  # Ajustar la dificultad si es necesario
        self.cadena.append(nuevo_bloque)
        return nuevo_bloque

    def validar_cadena(self):
        """
        Valida la integridad de la cadena de bloques.
        Comprueba que no se haya manipulado ningún bloque.
        """
        for i in range(1, len(self.cadena)):
            bloque_actual = self.cadena[i]
            bloque_anterior = self.cadena[i - 1]
            # Verificar la integridad de la referencia al hash anterior
            if bloque_actual.hash_anterior != bloque_anterior.hash:
                print(f"Error: El bloque {i} tiene un hash anterior incorrecto.")
                return False
            # Verificar que el hash actual sea correcto
            if bloque_actual.hash != bloque_actual.generar_hash():
                print(f"Error: El bloque {i} tiene un hash incorrecto.")
                return False
        return True

    def confirmar_conexion_modulos(self, modulos):
        """
        Confirma la conexión de los módulos y agrega un bloque con la información.
        
        Args:
            modulos (list): Lista de nombres de los módulos a confirmar.
        """
        data = f"Conexión de módulos confirmada: {', '.join(modulos)}"
        self.agregar_bloque(data)

    def imprimir_cadena(self):
        """
        Imprime la cadena de bloques completa.
        """
        for bloque in self.cadena:
            print(f"Bloque {bloque.index} - Hash: {bloque.hash}")
            print(f"Timestamp: {bloque.timestamp}")
            print(f"Datos: {bloque.datos}")
            print(f"Hash Anterior: {bloque.hash_anterior}\n")

    def obtener_informacion_cadena(self):
        """
        Obtiene información detallada de la cadena de bloques.
        Devuelve la longitud de la cadena y el contenido de los bloques.
        """
        informacion = {
            'longitud': len(self.cadena),
            'bloques': [{'index': bloque.index, 'timestamp': bloque.timestamp, 'hash': bloque.hash, 'hash_anterior': bloque.hash_anterior} for bloque in self.cadena]
        }
        return informacion

    def almacenar_bloque_en_base_datos(self, conexion, bloque):
        """
        Almacena un bloque en la base de datos.
        """
        insertar_bloque(conexion, bloque)

    def procesar_transaccion_y_almacenar(self, conexion, remitente, destinatario, cantidad, datos_bloque):
        """
        Procesa una transacción, agrega un bloque y almacena tanto el bloque como la transacción en la base de datos.
        """
        nuevo_bloque = self.agregar_bloque(datos_bloque)
        insertar_transaccion(conexion, remitente, destinatario, cantidad)
        self.almacenar_bloque_en_base_datos(conexion, nuevo_bloque)
        print(f"Transacción entre {remitente} y {destinatario} por {cantidad} procesada y almacenada en la base de datos.")
        
# modulo Blockchain #
