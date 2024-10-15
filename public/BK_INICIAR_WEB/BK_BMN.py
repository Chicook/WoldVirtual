# Boton de inicio del sistema 
# en desarrollo #

"""

import hashlib
import datetime
from BK_FN2 import *
from BK_FN3 import *

# Clase Block para manejar los bloques
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_data = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(block_data.encode()).hexdigest()

# Clase SimpleBlockchain
class SimpleBlockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, str(datetime.datetime.now()), "Genesis Block", "0")
        self.chain.append(genesis_block)

    def create_block_from_BK_FN2(self):
        # Ejecutar funciones del módulo 1
        function_results = []
        function_results.append(process_transaction())
        function_results.append(validate_user())
        function_results.append(generate_report())
        function_results.append(update_database())
        function_results.append(send_notification())

        # Crear y añadir el nuevo bloque con los resultados de las funciones
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), str(datetime.datetime.now()), function_results, previous_block.hash)
        self.chain.append(new_block)
        print("Nuevo bloque creado desde módulo 1 con funciones ejecutadas")

    def create_block_from_BK_FN3(self):
        # Ejecutar funciones del módulo 2
        function_results = []
        function_results.append(log_activity())
        function_results.append(send_alert())
        function_results.append(backup_data())
        function_results.append(clear_cache())
        function_results.append(sync_data())

        # Crear y añadir el nuevo bloque con los resultados de las funciones
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), str(datetime.datetime.now()), function_results, previous_block.hash)
        self.chain.append(new_block)
        print("Nuevo bloque creado desde módulo 2 con funciones ejecutadas")

    # Mostrar la cadena de bloques
    def show_chain(self):
        for block in self.chain:
            print(f"Índice: {block.index}, Data: {block.data}, Hash: {block.hash}")

# Ejecución
if __name__ == "__main__":
    blockchain = SimpleBlockchain()
    blockchain.create_block_from_BK_FN2()  # Llama a las funciones del módulo 1 y crea un bloque
    blockchain.create_block_from_BK_FN3()  # Llama a las funciones del módulo 2 y crea otro bloque
    blockchain.show_chain()  # Muestra la cadena de bloques

"""
