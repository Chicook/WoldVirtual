# prb3.py
import time
from prb2 import Block, Blockchain

blockchain = Blockchain()

def log_action(data):
    new_block = Block(len(blockchain.chain), time.time(), data, blockchain.get_latest_block().hash if blockchain.chain else "0")
    blockchain.add_block(new_block)
    print(f"Acción registrada: {data}")
