import hashlib

class Bloque:
    def __init__(self, index, previous_hash, data, proof, stake):
            self.index = index
                    self.previous_hash = previous_hash
                            self.data = data
                                    self.proof = proof  # Prueba de trabajo
                                            self.stake = stake  # Prueba de participación

                                            def proof_of_work(last_proof, data, difficulty):
                                                proof = 0
                                                    while not is_valid_proof(last_proof, data, proof, difficulty):
                                                            proof += 1
                                                                return proof

                                                                def is_valid_proof(last_proof, data, proof, difficulty):
                                                                    guess = f'{last_proof}{data}{proof}'.encode()
                                                                        guess_hash = hashlib.sha256(guess).hexdigest()
                                                                            return guess_hash[:difficulty] == '0' * difficulty

                                                                            def propose_block(data, stake, blockchain):
                                                                                last_block = blockchain[-1]
                                                                                    new_block_index = last_block.index + 1
                                                                                        last_proof = last_block.proof
                                                                                            new_proof = proof_of_work(last_proof, data, difficulty)
                                                                                                new_block = Bloque(new_block_index, last_block.hash(), data, new_proof, stake)
                                                                                                    blockchain.append(new_block)

                                                                                                    difficulty = 4  # Dificultad PoW
                                                                                                    genesis_block = Bloque(0, "0", "Datos del bloque génesis", proof_of_work(0, "Datos del bloque génesis", difficulty), 100)  # Stake inicial de 100
                                                                                                    blockchain = [genesis_block]

                                                                                                    # Agregar más bloques a la cadena usando PoW y PoS
                                                                                                    propose_block("Nuevos datos", 50, blockchain)

                                                                                                    # Imprimir la cadena de bloques
                                                                                                    for block in blockchain:
                                                                                                        print(f"Índice: {block.index}")
                                                                                                            print(f"Hash anterior: {block.previous_hash}")
                                                                                                                print(f"Datos: {block.data}")
                                                                                                                    print(f"Prueba de trabajo: {block.proof}")
                                                                                                                        print(f"Prueba de participación: {block.stake}")
                                                                                                                            print("\n")
                                                                                                                            