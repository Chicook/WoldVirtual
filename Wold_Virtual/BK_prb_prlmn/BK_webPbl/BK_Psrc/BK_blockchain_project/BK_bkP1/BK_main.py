import time
from flask import Flask, jsonify, request

# Importar los módulos
from BK_bkP2.block import Block
from BK_bkP3.blockchain import Blockchain
from BK_bkP4.internal_db import InternalDB
from BK_bkP5.validator import BlockchainValidator
from BK_bkP6.network import Network
from BK_bkP7.security import Security

app = Flask(__name__)
blockchain = Blockchain()
db = InternalDB()

@app.route('/blocks', methods=['GET'])
def get_blocks():
    blocks = [block.__dict__ for block in db.get_all_blocks()]
        return jsonify(blocks)

        @app.route('/mine_block', methods=['POST'])
        def mine_block():
            data = request.json['data']
            new_block = Block(len(blockchain.chain), blockchain.get_latest_block().hash, time.time(), data, "")
            blockchain.add_block(new_block)
            db.add_block(new_block)
            return jsonify(new_block.__dict__), 201

            @app.route('/validate_chain', methods=['GET'])
            def validate_chain():
            is_valid = BlockchainValidator.is_chain_valid(blockchain)
            return jsonify({"is_valid": is_valid})

        if __name__ == '__main__':
        # Añadir el bloque génesis a la base de datos interna
        db.add_block(blockchain.chain[0])
        # Ejecutar la API
        app.run(debug=True)
                                            
