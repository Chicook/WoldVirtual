# app.py

from BK_BCHPM import BK_BCHPM
from BK_TRSC import BK_TRSC

def main():
    # Crear blockchain
        blockchain = BK_BCHPM()

            # Crear algunas transacciones
                t1 = BK_TRSC("Alice", "Bob", 10)
                    t2 = BK_TRSC("Bob", "Charlie", 5)
                        t3 = BK_TRSC("Charlie", "Dave", 7)

                            # Añadir bloques con transacciones
                                blockchain.add_block([t1, t2])
                                    blockchain.add_block([t3])

                                        # Imprimir la blockchain
                                            print("Blockchain:")
                                                for block in blockchain.chain:
                                                        print(block)

                                                            # Verificar la validez de la cadena
                                                                print("¿Es válida la cadena?", blockchain.is_chain_valid())

                                                                if __name__ == "__main__":
                                                                    main()
                                                                    
