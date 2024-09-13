class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", time.time(), "Genesis Block", "0")

    def add_block(self, data):
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), previous_block.hash, time.time(), data, self.hash_block(data))
        self.chain.append(new_block)

    def hash_block(self, data):
        # Implementa la lógica de hash aquí
        pass
      
