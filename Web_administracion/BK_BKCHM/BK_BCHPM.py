# blockchain.py

from BK_BLK import BK_BLK

class Blockchain:
    difficulty = 2  # Dificultad de la prueba de trabajo

        def __init__(self):
                self.chain = []
                        self.create_genesis_block()

                            def create_genesis_block(self):
                                    """
                                            Crea el bloque génesis, que es el primer bloque de la blockchain.
                                                    """
                                                            genesis_block = Block(0, "0", "Genesis Block")
                                                                    self.chain.append(genesis_block)

                                                                        def get_last_block(self):
                                                                                return self.chain[-1]

                                                                                    def add_block(self, transactions):
                                                                                            """
                                                                                                    Añade un nuevo bloque con las transacciones especificadas a la blockchain.
                                                                                                            """
                                                                                                                    previous_block = self.get_last_block()
                                                                                                                            new_block = Block(index=previous_block.index + 1, previous_hash=previous_block.hash, transactions=transactions)
                                                                                                                                    new_block = self.proof_of_work(new_block)
                                                                                                                                            self.chain.append(new_block)
                                                                                                                                                    return new_block

                                                                                                                                                        def proof_of_work(self, block):
                                                                                                                                                                """
                                                                                                                                                                        Realiza la prueba de trabajo (PoW) ajustando el nonce hasta que se cumpla la condición de dificultad.
                                                                                                                                                                                """
                                                                                                                                                                                        while not block.hash.startswith('0' * Blockchain.difficulty):
                                                                                                                                                                                                    block.nonce += 1
                                                                                                                                                                                                                block.hash = block.compute_hash()
                                                                                                                                                                                                                        return block

                                                                                                                                                                                                                            def is_chain_valid(self):
                                                                                                                                                                                                                                    """
                                                                                                                                                                                                                                            Verifica la validez de la cadena de bloques completa.
                                                                                                                                                                                                                                                    """
                                                                                                                                                                                                                                                            for i in range(1, len(self.chain)):
                                                                                                                                                                                                                                                                        current_block = self.chain[i]
                                                                                                                                                                                                                                                                                    previous_block = self.chain[i - 1]

                                                                                                                                                                                                                                                                                                # Verificamos si el hash del bloque actual es válido
                                                                                                                                                                                                                                                                                                            if current_block.hash != current_block.compute_hash():
                                                                                                                                                                                                                                                                                                                            return False

                                                                                                                                                                                                                                                                                                                                        # Verificamos si el hash anterior coincide
                                                                                                                                                                                                                                                                                                                                                    if current_block.previous_hash != previous_block.hash:
                                                                                                                                                                                                                                                                                                                                                                    return False

                                                                                                                                                                                                                                                                                                                                                                            return True

                                                                                                                                                                                                                                                                                                                                                                                def __repr__(self):
                                                                                                                                                                                                                                                                                                                                                                                        return f"Blockchain(chain={self.chain})"
                                                                                                                                                                                                                                                                                                                                                                    
