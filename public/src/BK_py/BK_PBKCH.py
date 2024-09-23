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
                                                        self.chain = []
                                                                self.create_genesis_block()

                                                                    def create_genesis_block(self):
                                                                            genesis_block = Block(0, "0", time.time(), "Genesis Block", self.calculate_hash(0, "0", time.time(), "Genesis Block"))
                                                                                    self.chain.append(genesis_block)

                                                                                        def calculate_hash(self, index, previous_hash, timestamp, data):
                                                                                                value = str(index) + previous_hash + str(timestamp) + data
                                                                                                        return hashlib.sha256(value.encode('utf-8')).hexdigest()

                                                                                                            def get_latest_block(self):
                                                                                                                    return self.chain[-1]

                                                                                                                        def add_block(self, data):
                                                                                                                                latest_block = self.get_latest_block()
                                                                                                                                        new_index = latest_block.index + 1
                                                                                                                                                new_timestamp = time.time()
                                                                                                                                                        new_hash = self.calculate_hash(new_index, latest_block.hash, new_timestamp, data)
                                                                                                                                                                new_block = Block(new_index, latest_block.hash, new_timestamp, data, new_hash)
                                                                                                                                                                        self.chain.append(new_block)

                                                                                                                                                                            def print_chain(self):
                                                                                                                                                                                    for block in self.chain:
                                                                                                                                                                                                print(f"Index: {block.index}")
                                                                                                                                                                                                            print(f"Previous Hash: {block.previous_hash}")
                                                                                                                                                                                                                        print(f"Timestamp: {block.timestamp}")
                                                                                                                                                                                                                                    print(f"Data: {block.data}")
                                                                                                                                                                                                                                                print(f"Hash: {block.hash}")
                                                                                                                                                                                                                                                            print("-" * 30)
                                                                                                                                                                                                