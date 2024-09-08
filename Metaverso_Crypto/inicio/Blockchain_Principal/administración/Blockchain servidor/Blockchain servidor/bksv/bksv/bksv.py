import hashlib
import datetime

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

    def hash_block(self, index, timestamp, data, previous_hash, hash_type):
        block_string = f"{index}{timestamp}{data}{previous_hash}{hash_type}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def definir_tamano_bloque(self, data):
        data_size = len(json.dumps(data).encode('utf-8'))
        if data_size < 1 * 1024 * 1024:  # Menos de 1 MB
            return "1 MB"
        elif data_size > 1 * 1024 * 1024 and data_size < 1 * 1024 * 1024 * 1024:  # Entre 1 MB y 1 GB
            return "1 GB"
        else:
            return "Tamaño variable"
          
