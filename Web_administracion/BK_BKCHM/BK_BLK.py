# block.py

import time
import hashlib

class Block:
    def __init__(self, index, previous_hash, transactions, timestamp=None):
            self.index = index
                    self.previous_hash = previous_hash
                            self.timestamp = timestamp or time.time()
                                    self.transactions = transactions
                                            self.nonce = 0
                                                    self.hash = self.compute_hash()

                                                        def compute_hash(self):
                                                                """
                                                                        Calcula el hash del bloque combinando la información del bloque en una cadena y luego la encripta.
                                                                                """
                                                                                        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.transactions}{self.nonce}"
                                                                                                return hashlib.sha256(block_string.encode()).hexdigest()

                                                                                                    def __repr__(self):
                                                                                                            return f"Block(index={self.index}, hash={self.hash}, prev_hash={self.previous_hash}, transactions={self.transactions})"
                                                                