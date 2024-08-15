import tkinter as tk
import hashlib
from flask import Flask, render_template
from web3 import Web3
import datetime
# Importamos el módulo 'time' correctamente
import time
import json

# Definimos la clase 'Blockchain'
class Blockchain:
    # Esta es la función de inicialización de nuestra clase Blockchain
    def __init__(self):
        # Inicializamos nuestra cadena y la transacción actual
        self.chain = []
        self.current_transactions = []

    # Definimos la función para crear un nuevo bloque
    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]) if self.chain else "1",
        }
        self.current_transactions = []
        self.chain.append(block)
        return block

    # Definimos la función para añadir una nueva transacción
    def new_transaction(self, sender, recipient, amount):
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        return self.last_block['index'] + 1

    # Función para calcular el hash de un bloque
    def hash(self, block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    # Función para obtener el último bloque de la cadena
    @property
    def last_block(self):
        return self.chain[-1]

    # Función para validar la cadena
    def valid_chain(self, chain):
        last_block = chain[0]
        current_index = 1

        while current_index < len(chain):
            block = chain[current_index]
            if block['previous_hash'] != self.hash(last_block):
                return False
            last_block = block
            current_index += 1

        return True

# Aquí iría el resto del código...
