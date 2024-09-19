# BK_5Blockchain.py
def hash_block(block):
    return str(block)  # Esto es solo un ejemplo, usa una función de hash real

    def ValidateChain(chain):
        for i in range(1, len(chain)):
                current_block = chain[i]
                        previous_block = chain[i - 1]
                                if current_block['previous_hash'] != hash_block(previous_block):
                                            return False
                                                return True
                