import hashlib
import time

class Blockchain:
    def __init__(self):
            self.chain = []
                    self.pending_transactions = []

                        def create_block(self, transactions):
                                previous_block = self.chain[-1] if self.chain else None
                                        previous_hash = previous_block['hash'] if previous_block else '0'
                                                block = {
                                                            'index': len(self.chain) + 1,
                                                                        'timestamp': time.time(),
                                                                                    'transactions': transactions,
                                                                                                'previous_hash': previous_hash,
                                                                                                            'nonce': 0,
                                                                                                                        'hash': self.calculate_hash(transactions, previous_hash)
                                                                                                                                }
                                                                                                                                        self.chain.append(block)
                                                                                                                                                return block

                                                                                                                                                    def calculate_hash(self, transactions, previous_hash):
                                                                                                                                                            block_string = f"{transactions}{previous_hash}"
                                                                                                                                                                    return hashlib.sha256(block_string.encode()).hexdigest()

                                                                                                                                                                        def add_transaction(self, transaction):
                                                                                                                                                                                self.pending_transactions.append(transaction)
                                                                                                                                                                                