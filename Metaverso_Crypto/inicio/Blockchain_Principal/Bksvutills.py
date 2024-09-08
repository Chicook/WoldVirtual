import hashlib
import json
import os
import datetime
import time
import random
from flask import Flask, jsonify, request
from blockchain import Blockchain

# Inicializar la blockchain
blockchain = Blockchain()
codigos_temporales = {}

app = Flask(__name__)

def log_action(data):
    new_block = blockchain.new_block(len(blockchain.chain), data, blockchain.chain[-1]['previous_hash'] if blockchain.chain else "0")
    blockchain.chain.append(new_block)
    print(f"Acción registrada: {data}")

def generar_codigo_temporal():
    codigo = str(random.randint(100000, 999999))
    codigos_temporales[codigo] = time.time()
    return codigo

def verificar_codigo_temporal(codigo):
    return time.time() - codigos_temporales.get(codigo, 0) < 30

def confirmar_conexion_modulos(modulos):
    data = f"Conexión de módulos: {', '.join(modulos)}"
    blockchain.new_block(data)

@app.route('/mine', methods=['GET'])
def mine():
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    blockchain.new_transaction(
        sender="0",
        recipient="node_address",
        amount=1,
    )

    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)

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

@app.route('/generate_code', methods=['GET'])
def generate_code():
    code = generar_codigo_temporal()
    response = {'code': code}
    return jsonify(response), 200

@app.route('/verify_code', methods=['POST'])
def verify_code():
    values = request.get_json()
    code = values.get('code')
    if verificar_codigo_temporal(code):
        response = {'message': 'Code is valid'}
    else:
        response = {'message': 'Code is invalid or expired'}
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
