# BK_1Blockchain.py
from BK_2Blockchain import GenesisBlock
from BK_3Blockchain import AddBlock
from BK_4Blockchain import ChainInfo
from BK_5Blockchain import ValidateChain

class Blockchain:
    def __init__(self):
            self.chain = []
                    self.crear_bloque_genesis()

                        def crear_bloque_genesis(self):
                                genesis_block = GenesisBlock()
                                        self.chain.append(genesis_block)

                                            def agregar_bloque(self, data):
                                                    new_block = AddBlock(self.chain, data)
                                                            self.chain.append(new_block)

                                                                def obtener_informacion_cadena(self):
                                                                        return ChainInfo(self.chain)

                                                                            def validar_cadena(self):
                                                                                    return ValidateChain(self.chain)

                                                                                    if __name__ == "__main__":
                                                                                        blockchain = Blockchain()
                                                                                            blockchain.agregar_bloque("transaccion_ejemplo")
                                                                                                print(blockchain.obtener_informacion_cadena())
                                                                                                    print("Cadena válida:", blockchain.validar_cadena())
                                                                                        