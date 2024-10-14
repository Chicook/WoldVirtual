# app.py

from BK_BCHPM import BK_BCHPM
from BK_TRSC import BK_TRSC

def main():
    # Crear blockchain
        blockchain = Blockchain()

            # Crear algunas transacciones
                t1 = Transaction("Alice", "Bob", 10)
                    t2 = Transaction("Bob", "Charlie", 5)
                        t3 = Transaction("Charlie", "Dave", 7)

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
                                                                    
