import hashlib
import datetime

class Blockchain:
    def __init__(self):
        self.chain = []
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
        """
        Confirma la conexión de los módulos y agrega un bloque con la información.
        
        Args:
            modulos (list): Lista de nombres de los módulos a confirmar.
        """
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

# Ejemplo de uso
if __name__ == "__main__":
    blockchain = Blockchain()
    blockchain.confirmar_conexion_modulos(['usuarios', 'recursos', 'database', 'compresion', 'servidor'])
    blockchain.imprimir_cadena()
