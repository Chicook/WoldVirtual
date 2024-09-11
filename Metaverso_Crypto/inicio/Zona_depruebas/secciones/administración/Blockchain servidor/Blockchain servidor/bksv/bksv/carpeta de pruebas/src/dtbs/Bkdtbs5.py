# prb5.py
from prb4 import hash_block

def register_user(blockchain, user):
    block = {
        'username': user.username,
        'previous_hash': hash_block(blockchain.chain[-1]) if blockchain.chain else '0'
    }
    block['hash'] = hash_block(block)
    blockchain.add_block(block)

