# BK_3Blockchain.py
from BK_5Blockchain import hash_block

def AddBlock(chain, data):
    previous_block = chain[-1]
        new_block = {
                'index': len(chain),
                        'timestamp': '2024-08-20 00:00:00',
                                'data': data,
                                        'previous_hash': hash_block(previous_block)
                                            }
                                                return new_block
