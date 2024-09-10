# prb2.py
import hashlib
import time

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

    def get_latest_block(self):
        return self.chain[-1] if self.chain else None

    def add_block(self, new_block):
        if self.chain:
            new_block.previous_hash = self.get_latest_block().hash
        else:
            new_block.previous_hash = "0"
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

blockchain = Blockchain()

def log_action(data):
    new_block = Block(len(blockchain.chain), time.time(), data, blockchain.get_latest_block().hash if blockchain.chain else "0")
    blockchain.add_block(new_block)
    print(f"Acción registrada: {data}")
    
