import hashlib
import json
import os
import time
import random

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.reward = 0.001  # Recompensa en WCV
        self.data_dir = 'blockchain_principal'
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
        self.new_block(previous_hash='1', proof=100)

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
            'size': self.definir_tamano_bloque(self.current_transactions),
            'confirmations': self.definir_confirmaciones()
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

    def proof_of_work(self, last_proof):
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    def create_user_json(self, username):
        user_hash = hashlib.sha256(username.encode()).hexdigest()
        user_data = {
            'username': username,
            'hash': user_hash
        }
        self.new_transaction(sender="0", recipient=user_hash, amount=self.reward)
        proof = self.proof_of_work(self.last_block['proof'])
        self.new_block(proof)
        file_path = os.path.join(self.data_dir, f'{username}.json')
        with open(file_path, 'w') as json_file:
            json.dump(user_data, json_file)
        return user_data

    def definir_tamano_bloque(self, data):
        data_size = len(json.dumps(data).encode('utf-8'))
        if data_size < 1 * 1024 * 1024:  # Menos de 1 MB
            return "1 MB"
        elif data_size < 1 * 1024 * 1024 * 1024:  # Entre 1 MB y 1 GB
            return "1 GB"
        else:
            return "Tamaño variable"

    def definir_confirmaciones(self):
        # Aquí puedes implementar la lógica para determinar el número de confirmaciones
        # según el número de usuarios en línea. Por simplicidad, usaremos un valor fijo.
        usuarios_en_linea = 3  # Este valor debería ser dinámico
        if usuarios_en_linea == 1:
            return "1/3 confirmaciones"
        elif usuarios_en_linea == 2:
            return "2/3 confirmaciones"
        else:
            return "3/3 confirmaciones"

    def hash_confirmacion(self, actividad):
        actividad_string = json.dumps(actividad, sort_keys=True).encode()
        return hashlib.sha256(actividad_string).hexdigest()

    def registrar_actividad(self, actividad):
        hash_actividad = self.hash_confirmacion(actividad)
        self.log_action(f"Actividad registrada: {actividad} con hash {hash_actividad}")
        return hash_actividad

    def verificar_sistema(self):
        for block in self.chain:
            if not self.valid_proof(block['proof'], block['proof']):
                return False
        return True

    def log_action(self, data):
        new_block = self.new_block(len(self.chain), data, self.chain[-1]['previous_hash'] if self.chain else "0")
        self.chain.append(new_block)
        print(f"Acción registrada: {data}")

    def generar_codigo_temporal(self):
        codigo = str(random.randint(100000, 999999))
        codigos_temporales[codigo] = time.time()
        return codigo

    def verificar_codigo_temporal(self, codigo):
        return time.time() - codigos_temporales.get(codigo, 0) < 30

    def confirmar_conexion_modulos(self, modulos):
        data = f"Conexión de módulos: {', '.join(modulos)}"
        self.new_block(data)
