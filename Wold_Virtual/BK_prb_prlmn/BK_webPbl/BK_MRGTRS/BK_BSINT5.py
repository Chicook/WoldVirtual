import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

def calculate_hash(index, previous_hash, timestamp, data):
    value = str(index) + previous_hash + str(timestamp) + str(data)
    return hashlib.sha256(value.encode('utf-8')).hexdigest()

def create_block(index, previous_hash, data):
    timestamp = time.time()
    hash = calculate_hash(index, previous_hash, timestamp, data)
    return Block(index, previous_hash, timestamp, data, hash)

# Simulación de blockchain en memoria
blockchain = []

def add_block(data):
    if len(blockchain) == 0:
        previous_hash = "0"
        index = 0
    else:
        previous_hash = blockchain[-1].hash
        index = blockchain[-1].index + 1

    new_block = create_block(index, previous_hash, data)
    blockchain.append(new_block)
    return new_block
