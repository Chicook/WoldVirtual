import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", time.time(), "Genesis Block", self.hash_block(0, "0", time.time(), "Genesis Block"))

    def hash_block(self, index, previous_hash, timestamp, data):
        block_string = f"{index}{previous_hash}{timestamp}{data}".encode()
        return hashlib.sha256(block_string).hexdigest()

    def get_last_block(self):
        return self.chain[-1]

    def add_block(self, data):
        last_block = self.get_last_block()
        new_index = last_block.index + 1
        new_timestamp = time.time()
        new_hash = self.hash_block(new_index, last_block.hash, new_timestamp, data)
        new_block = Block(new_index, last_block.hash, new_timestamp, data, new_hash)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != self.hash_block(current_block.index, current_block.previous_hash, current_block.timestamp, current_block.data):
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    def obtener_informacion_cadena(self):
        informacion = {
            'longitud': len(self.chain),
            'bloques': [block.__dict__ for block in self.chain],
        }
        return informacion
