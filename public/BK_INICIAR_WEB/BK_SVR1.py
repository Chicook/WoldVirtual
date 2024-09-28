"""

refactorizacion, para prevenir errores.

"""

"""

import socket
import hashlib
import json
from time import time
from flask import Flask, request, jsonify

# Clase Blockchain
class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.new_block(previous_hash='1', proof=100)  # Bloque génesis

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.current_transactions = []
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]

# Inicializar Flask y Blockchain
app = Flask(__name__)
blockchain = Blockchain()

# Rutas de la API
@app.route('/mine', methods=['GET'])
def mine():
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = proof_of_work(last_proof)

    blockchain.new_transaction(
        sender="0",
        recipient="your_address",
        amount=1,
    )

    block = blockchain.new_block(proof)

    response = {
        'message': "New Block Forged",
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()
    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return 'Missing values', 400

    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])
    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

def proof_of_work(last_proof):
    proof = 0
    while not valid_proof(last_proof, proof):
        proof += 1
    return proof

def valid_proof(last_proof, proof):
    guess = f'{last_proof}{proof}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    return guess_hash[:4] == "0000"

# Funcionalidad de Sockets
def start_socket_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 8080))
    server_socket.listen(1)

    print("Conectando Recurso...")
    client_socket, address = server_socket.accept()
    print(f"Conectado a {address}")

    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break
        print(f"Recibido: {data}")
        client_socket.send("Recurso conectado".encode())

    client_socket.close()
    server_socket.close()

@app.route('/mensaje', methods=['POST'])
def mensaje():
    data = request.json
    print(f"Recibido: {data}")
    return "recurso conectado", 200

if __name__ == '__main__':
    from threading import Thread
    # Iniciar el servidor de sockets en un hilo separado
    socket_thread = Thread(target=start_socket_server)
    socket_thread.start()
    # Iniciar el servidor Flask
    app.run(host='0.0.0.0', port=5000)

"""
