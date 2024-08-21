import hashlib
import datetime

class Blockchain:
    def __init__(self):
        # Inicializa la cadena de bloques
        self.chain = []
        # Crea el bloque génesis (el primer bloque de la cadena)
        self.crear_bloque_genesis()

    def crear_bloque_genesis(self):
        # Define el bloque génesis con un índice de 0 y un hash previo de '0'
        genesis_block = {
            'index': 0,
            'timestamp': str(datetime.datetime.now()),  # Fecha y hora actuales
            'data': 'Bloque Génesis',  # Datos arbitrarios para el bloque génesis
            'previous_hash': '0',  # El bloque génesis no tiene un bloque previo
            'hash': self.hash_block(0, str(datetime.datetime.now()), 'Bloque Génesis', '0')  # Calcula el hash del bloque génesis
        }
        # Agrega el bloque génesis a la cadena
        self.chain.append(genesis_block)

    def agregar_bloque(self, data):
        # Obtiene el último bloque de la cadena
        previous_block = self.chain[-1]
        # Crea un nuevo bloque
        new_block = {
            'index': len(self.chain),  # El índice es la longitud actual de la cadena
            'timestamp': str(datetime.datetime.now()),  # Fecha y hora actuales
            'data': data,  # Los datos proporcionados al agregar el bloque
            'previous_hash': previous_block['hash'],  # El hash del bloque anterior
            'hash': self.hash_block(len(self.chain), str(datetime.datetime.now()), data, previous_block['hash'])  # Calcula el hash del nuevo bloque
        }
        # Agrega el nuevo bloque a la cadena
        self.chain.append(new_block)

    def obtener_informacion_cadena(self):
        # Devuelve la longitud de la cadena y los bloques en ella
        informacion = {
            'longitud': len(self.chain),  # Número de bloques en la cadena
            'bloques': [block for block in self.chain],  # Lista de bloques
        }
        return informacion

    def hash_block(self, index, timestamp, data, previous_hash):
        # Genera un hash SHA-256 para el bloque basado en su índice, marca de tiempo, datos y hash previo
        block_string = f"{index}{timestamp}{data}{previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def validar_cadena(self):
        # Verifica la integridad de la cadena de bloques
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            # Verifica que el hash previo en el bloque actual coincide con el hash del bloque anterior
            if current_block['previous_hash'] != previous_block['hash']:
                return False
            # Verifica que el hash del bloque actual es correcto
            recalculated_hash = self.hash_block(
                current_block['index'], 
                current_block['timestamp'], 
                current_block['data'], 
                current_block['previous_hash']
            )
            if current_block['hash'] != recalculated_hash:
                return False
        return True
