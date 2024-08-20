from web3 import Web3
from solcx import compile_standard, install_solc
import json

class Blockchain:
    def __init__(self):
        self.chain = []
        self.crear_bloque_genesis()
        self.web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
        self.contract = self.deploy_contract()

    def crear_bloque_genesis(self):
        genesis_block = {
            'index': 0,
            'timestamp': '2024-08-20 00:00:00',
            'data': 'Bloque Génesis',
            'previous_hash': '0'
        }
        self.chain.append(genesis_block)

    def agregar_bloque(self, data):
        previous_block = self.chain[-1]
        new_block = {
            'index': len(self.chain),
            'timestamp': '2024-08-20 00:00:00',
            'data': data,
            'previous_hash': self.hash(previous_block)
        }
        self.chain.append(new_block)

    def obtener_informacion_cadena(self):
        informacion = {
            'longitud': len(self.chain),
            'bloques': [block for block in self.chain],
        }
        return informacion

    def hash(self, block):
        return str(block)  # Esto es solo un ejemplo, usa una función de hash real

    def validar_cadena(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block['previous_hash'] != self.hash(previous_block):
                return False
        return True

    def deploy_contract(self):
        # Instalar la versión de Solidity
        install_solc("0.8.0")

        # Código del contrato inteligente
        contract_source_code = '''
        // SPDX-License-Identifier: MIT
        pragma solidity ^0.8.0;

        contract WoldCoinVirtual {
            string public name = "WoldCoinVirtual";
            string public symbol = "WCV";
            uint8 public decimals = 3;
            uint256 public totalSupply = 30000000 * 10 ** uint256(decimals);
            mapping(address => uint256) public balanceOf;
            mapping(address => mapping(address => uint256)) public allowance;

            event Transfer(address indexed from, address indexed to, uint256 value);
            event Approval(address indexed owner, address indexed spender, uint256 value);

            constructor() {
                balanceOf[msg.sender] = totalSupply;
            }

            function transfer(address _to, uint256 _value) public returns (bool success) {
                require(balanceOf[msg.sender] >= _value, "Insufficient balance");
                balanceOf[msg.sender] -= _value;
                balanceOf[_to] += _value;
                emit Transfer(msg.sender, _to, _value);
                return true;
            }

            function approve(address _spender, uint256 _value) public returns (bool success) {
                allowance[msg.sender][_spender] = _value;
                emit Approval(msg.sender, _spender, _value);
                return true;
            }

            function transferFrom(address _from, address _to, uint256 _value) public returns (bool success) {
                require(_value <= balanceOf[_from], "Insufficient balance");
                require(_value <= allowance[_from][msg.sender], "Allowance exceeded");
                balanceOf[_from] -= _value;
                balanceOf[_to] += _value;
                allowance[_from][msg.sender] -= _value;
                emit Transfer(_from, _to, _value);
                return true;
            }
        }
        '''

        # Compilar el contrato
        compiled_sol = compile_standard({
            "language": "Solidity",
            "sources": {
                "WoldCoinVirtual.sol": {
                    "content": contract_source_code
                }
            },
            "settings": {
                "outputSelection": {
                    "*": {
                        "*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]
                    }
                }
            }
        })

        # Obtener el bytecode y el ABI
        bytecode = compiled_sol['contracts']['WoldCoinVirtual.sol']['WoldCoinVirtual']['evm']['bytecode']['object']
        abi = json.loads(compiled_sol['contracts']['WoldCoinVirtual.sol']['WoldCoinVirtual']['metadata'])['output']['abi']

        # Desplegar el contrato
        WCV = self.web3.eth.contract(abi=abi, bytecode=bytecode)
        tx_hash = WCV.constructor().transact({'from': self.web3.eth.accounts[0], 'gas': 410000})
        tx_receipt = self.web3.eth.waitForTransactionReceipt(tx_hash)

        print(f"Contrato desplegado en la dirección: {tx_receipt.contractAddress}")
        return self.web3.eth.contract(address=tx_receipt.contractAddress, abi=abi)

    def obtener_balance(self, direccion):
        return self.contract.functions.balanceOf(direccion).call()

# Ejemplo de uso
blockchain = Blockchain()
print(blockchain.obtener_informacion_cadena())
print(f"Balance del creador del contrato: {blockchain.obtener_balance(blockchain.web3.eth.accounts[0])}")
