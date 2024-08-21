# blockchain.py

import hashlib
import datetime

class Blockchain:
    """
    Clase para gestionar una cadena de bloques (blockchain).
    """
    def __init__(self):
        self.chain = []
        self.crear_bloque_genesis()

    def crear_bloque_genesis(self):
        """
        Crea el bloque génesis y lo añade a la cadena.
        """
        genesis_block = {
            'index': 0,
            'timestamp': str(datetime.datetime.now()),
            'data': 'Bloque Génesis',
            'previous_hash': '0',
            'hash': self.hash_block(0, str(datetime.datetime.now()), 'Bloque Génesis', '0')
        }
        self.chain.append(genesis_block)

    def agregar_bloque(self, data):
        """
        Añade un nuevo bloque a la cadena.
        """
        previous_block = self.chain[-1]
        new_block = {
            'index': len(self.chain),
            'timestamp': str(datetime.datetime.now()),
            'data': data,
            'previous_hash': previous_block['hash'],
            'hash': self.hash_block(len(self.chain), str(datetime.datetime.now()), data, previous_block['hash'])
        }
        self.chain.append(new_block)

    def obtener_informacion_cadena(self):
        """
        Obtiene información sobre la cadena de bloques.
        """
        informacion = {
            'longitud': len(self.chain),
            'bloques': [block for block in self.chain],
        }
        return informacion

    def hash_block(self, index, timestamp, data, previous_hash):
        """
        Genera el hash para un bloque.
        """
        block_string = f"{index}{timestamp}{data}{previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def validar_cadena(self):
        """
        Valida la cadena de bloques.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            # Verificar que el hash del bloque anterior sea el mismo
            if current_block['previous_hash'] != previous_block['hash']:
                return False
            # Verificar que el hash del bloque actual sea válido
            if current_block['hash'] != self.hash_block(current_block['index'], current_block['timestamp'], current_block['data'], previous_block['hash']):
                return False
        return True

    def imprimir_cadena(self):
        """
        Imprime la cadena de bloques.
        """
        for block in self.chain:
            print(block)

# Ejemplo de uso en caso de ser ejecutado directamente
if __name__ == "__main__":
    blockchain = Blockchain()
    blockchain.agregar_bloque("Primer Bloque Después del Génesis")
    blockchain.agregar_bloque("Segundo Bloque Después del Génesis")
    blockchain.imprimir_cadena()
    print("Cadena válida:", blockchain.validar_cadena())
