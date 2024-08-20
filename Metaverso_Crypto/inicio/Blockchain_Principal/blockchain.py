from web3 import Web3
import json
from solcx import compile_source

class Blockchain:
    def __init__(self):
        self.cadena = []
        self.web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
        self.web3.eth.default_account = self.web3.eth.accounts[0]
        self.crear_bloque_genesis()
        self.contract_address, self.contract_instance = self.deploy_contract()

    def crear_bloque_genesis(self):
        bloque_genesis = {
            'indice': 0,
            'timestamp': self.web3.eth.getBlock('latest').timestamp,
            'datos': "Bloque Génesis",
            'hash_previo': "0"
        }
        self.cadena.append(bloque_genesis)

    def agregar_bloque(self, datos):
        bloque_anterior = self.cadena[-1]
        nuevo_bloque = {
            'indice': len(self.cadena),
            'timestamp': self.web3.eth.getBlock('latest').timestamp,
            'datos': datos,
            'hash_previo': self.hash(bloque_anterior)
        }
        self.cadena.append(nuevo_bloque)

    def obtener_informacion_cadena(self):
        return {
            'longitud': len(self.cadena),
            'cadena': self.cadena
        }

    def hash(self, bloque):
        return str(bloque)  # Reemplazar con una función de hash real como SHA-256

    def validar_cadena(self):
        for i in range(1, len(self.cadena)):
            bloque_actual = self.cadena[i]
            bloque_anterior = self.cadena[i-1]
            if bloque_actual['hash_previo'] != self.hash(bloque_anterior):
                return False
        return True

    def deploy_contract(self):
        # Código fuente del contrato inteligente en Solidity
        contract_source_code = '''
        pragma solidity ^0.8.0;

        contract WoldCoinVirtual {
            string public name = "WoldCoinVirtual";
            string public symbol = "WCV";
            uint8 public decimals = 3;
            uint256 public totalSupply = 30000000 * (10 ** uint256(decimals));
            mapping(address => uint256) public balanceOf;
            mapping(address => mapping(address => uint256)) public allowance;

            constructor() {
                balanceOf[msg.sender] = totalSupply;
            }

            function transfer(address to, uint256 value) public returns (bool success) {
                require(balanceOf[msg.sender] >= value, "Saldo insuficiente.");
                balanceOf[msg.sender] -= value;
                balanceOf[to] += value;
                return true;
            }

            function approve(address spender, uint256 value) public returns (bool success) {
                allowance[msg.sender][spender] = value;
                return true;
            }

            function transferFrom(address from, address to, uint256 value) public returns (bool success) {
                require(value <= balanceOf[from], "Saldo insuficiente.");
                require(value <= allowance[from][msg.sender], "Allowance insuficiente.");
                balanceOf[from] -= value;
                balanceOf[to] += value;
                allowance[from][msg.sender] -= value;
                return true;
            }
        }
        '''

        # Compilar el contrato inteligente
        compiled_sol = compile_source(contract_source_code, output_values=['abi', 'bin'])
        contract_interface = compiled_sol['<stdin>:WoldCoinVirtual']

        # ABI y bytecode
        abi = contract_interface['abi']
        bytecode = contract_interface['bin']

        # Desplegar el contrato en la red
        Contract = self.web3.eth.contract(abi=abi, bytecode=bytecode)
        tx_hash = Contract.constructor().transact()
        tx_receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)

        # Retornar la dirección del contrato y la instancia del contrato
        return tx_receipt.contractAddress, self.web3.eth.contract(
            address=tx_receipt.contractAddress,
            abi=abi
        )

# Ejemplo de uso
blockchain = Blockchain()
blockchain.agregar_bloque("Datos del primer bloque")
blockchain.agregar_bloque("Datos del segundo bloque")
print(blockchain.obtener_informacion_cadena())
print(f"Dirección del contrato: {blockchain.contract_address}")
