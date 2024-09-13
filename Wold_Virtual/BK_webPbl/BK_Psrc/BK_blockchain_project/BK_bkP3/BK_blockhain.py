import time
from BK_bkP2.block import Block

class Blockchain:
    def __init__(self):
            self.chain = [self.create_genesis_block()]

                def create_genesis_block(self):
                        return Block(0, "0", time.time(), "Genesis Block", Block.calculate_hash(0, "0", time.time(), "Genesis Block"))

                            def get_latest_block(self):
                                    return self.chain[-1]

                                        def add_block(self, new_block):
                                                new_block.previous_hash = self.get_latest_block().hash
                                                        new_block.hash = Block.calculate_hash(new_block.index, new_block.previous_hash, new_block.timestamp, new_block.data)
                                                                self.chain.append(new_block)
                                                