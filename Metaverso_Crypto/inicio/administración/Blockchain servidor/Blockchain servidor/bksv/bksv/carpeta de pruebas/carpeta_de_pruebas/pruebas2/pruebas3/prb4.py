# prb4.py
import hashlib

def hash_block(block):
    block_string = str(block).encode()
    return hashlib.sha256(block_string).hexdigest()
