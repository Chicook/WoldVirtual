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
        pragma solidity ^0.8.26;

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
        abi = contract_interface['60806040526040518060400160405280600f81526020017f576f6c64436f696e5669727475616c00000000000000000000000000000000008152505f90816100479190610367565b506040518060400160405280600381526020017f57435600000000000000000000000000000000000000000000000000000000008152506001908161008c9190610367565b50600360025f6101000a81548160ff021916908360ff16021790555060025f9054906101000a900460ff1660ff16600a6100c69190610592565b6301c9c3806100d591906105dc565b6003553480156100e3575f80fd5b5060035460045f3373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f208190555061061d565b5f81519050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602260045260245ffd5b5f60028204905060018216806101a857607f821691505b6020821081036101bb576101ba610164565b5b50919050565b5f819050815f5260205f209050919050565b5f6020601f8301049050919050565b5f82821b905092915050565b5f6008830261021d7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff826101e2565b61022786836101e2565b95508019841693508086168417925050509392505050565b5f819050919050565b5f819050919050565b5f61026b6102666102618461023f565b610248565b61023f565b9050919050565b5f819050919050565b61028483610251565b61029861029082610272565b8484546101ee565b825550505050565b5f90565b6102ac6102a0565b6102b781848461027b565b505050565b5b818110156102da576102cf5f826102a4565b6001810190506102bd565b5050565b601f82111561031f576102f0816101c1565b6102f9846101d3565b81016020851015610308578190505b61031c610314856101d3565b8301826102bc565b50505b505050565b5f82821c905092915050565b5f61033f5f1984600802610324565b1980831691505092915050565b5f6103578383610330565b9150826002028217905092915050565b6103708261012d565b67ffffffffffffffff81111561038957610388610137565b5b6103938254610191565b61039e8282856102de565b5f60209050601f8311600181146103cf575f84156103bd578287015190505b6103c7858261034c565b86555061042e565b601f1984166103dd866101c1565b5f5b82811015610404578489015182556001820191506020850194506020810190506103df565b86831015610421578489015161041d601f891682610330565b8355505b6001600288020188555050505b505050505050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52601160045260245ffd5b5f8160011c9050919050565b5f808291508390505b60018511156104b85780860481111561049457610493610436565b5b60018516156104a35780820291505b80810290506104b185610463565b9450610478565b94509492505050565b5f826104d0576001905061058b565b816104dd575f905061058b565b81600181146104f357600281146104fd5761052c565b600191505061058b565b60ff84111561050f5761050e610436565b5b8360020a91508482111561052657610525610436565b5b5061058b565b5060208310610133831016604e8410600b84101617156105615782820a90508381111561055c5761055b610436565b5b61058b565b61056e848484600161046f565b9250905081840481111561058557610584610436565b5b81810290505b9392505050565b5f61059c8261023f565b91506105a78361023f565b92506105d47fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff84846104c1565b905092915050565b5f6105e68261023f565b91506105f18361023f565b92508282026105ff8161023f565b9150828204841483151761061657610615610436565b5b5092915050565b610d618061062a5f395ff3fe608060405234801561000f575f80fd5b5060043610610091575f3560e01c8063313ce56711610064578063313ce5671461013157806370a082311461014f57806395d89b411461017f578063a9059cbb1461019d578063dd62ed3e146101cd57610091565b806306fdde0314610095578063095ea7b3146100b357806318160ddd146100e357806323b872dd14610101575b5f80fd5b61009d6101fd565b6040516100aa9190610934565b60405180910390f35b6100cd60048036038101906100c891906109e5565b610288565b6040516100da9190610a3d565b60405180910390f35b6100eb610375565b6040516100f89190610a65565b60405180910390f35b61011b60048036038101906101169190610a7e565b61037b565b6040516101289190610a3d565b60405180910390f35b61013961065b565b6040516101469190610ae9565b60405180910390f35b61016960048036038101906101649190610b02565b61066d565b6040516101769190610a65565b60405180910390f35b610187610682565b6040516101949190610934565b60405180910390f35b6101b760048036038101906101b291906109e5565b61070e565b6040516101c49190610a3d565b60405180910390f35b6101e760048036038101906101e29190610b2d565b6108a4565b6040516101f49190610a65565b60405180910390f35b5f805461020990610b98565b80601f016020809104026020016040519081016040528092919081815260200182805461023590610b98565b80156102805780601f1061025757610100808354040283529160200191610280565b820191905f5260205f20905b81548152906001019060200180831161026357829003601f168201915b505050505081565b5f8160055f3373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f205f8573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f20819055508273ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff167f8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925846040516103639190610a65565b60405180910390a36001905092915050565b60035481565b5f60045f8573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f20548211156103fc576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016103f390610c12565b60405180910390fd5b60055f8573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f205f3373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f20548211156104b7576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016104ae90610c7a565b60405180910390fd5b8160045f8673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f205f8282546105039190610cc5565b925050819055508160045f8573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f205f8282546105569190610cf8565b925050819055508160055f8673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f205f3373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f205f8282546105e49190610cc5565b925050819055508273ffffffffffffffffffffffffffffffffffffffff168473ffffffffffffffffffffffffffffffffffffffff167fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef846040516106489190610a65565b60405180910390a3600190509392505050565b60025f9054906101000a900460ff1681565b6004602052805f5260405f205f915090505481565b6001805461068f90610b98565b80601f01602080910402602001604051908101604052809291908181526020018280546106bb90610b98565b80156107065780601f106106dd57610100808354040283529160200191610706565b820191905f5260205f20905b8154815290600101906020018083116106e957829003601f168201915b505050505081565b5f8160045f3373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f2054101561078f576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161078690610c12565b60405180910390fd5b8160045f3373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f205f8282546107db9190610cc5565b925050819055508160045f8573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f205f82825461082e9190610cf8565b925050819055508273ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff167fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef846040516108929190610a65565b60405180910390a36001905092915050565b6005602052815f5260405f20602052805f5260405f205f91509150505481565b5f81519050919050565b5f82825260208201905092915050565b8281835e5f83830152505050565b5f601f19601f8301169050919050565b5f610906826108c4565b61091081856108ce565b93506109208185602086016108de565b610929816108ec565b840191505092915050565b5f6020820190508181035f83015261094c81846108fc565b905092915050565b5f80fd5b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f61098182610958565b9050919050565b61099181610977565b811461099b575f80fd5b50565b5f813590506109ac81610988565b92915050565b5f819050919050565b6109c4816109b2565b81146109ce575f80fd5b50565b5f813590506109df816109bb565b92915050565b5f80604083850312156109fb576109fa610954565b5b5f610a088582860161099e565b9250506020610a19858286016109d1565b9150509250929050565b5f8115159050919050565b610a3781610a23565b82525050565b5f602082019050610a505f830184610a2e565b92915050565b610a5f816109b2565b82525050565b5f602082019050610a785f830184610a56565b92915050565b5f805f60608486031215610a9557610a94610954565b5b5f610aa28682870161099e565b9350506020610ab38682870161099e565b9250506040610ac4868287016109d1565b9150509250925092565b5f60ff82169050919050565b610ae381610ace565b82525050565b5f602082019050610afc5f830184610ada565b92915050565b5f60208284031215610b1757610b16610954565b5b5f610b248482850161099e565b91505092915050565b5f8060408385031215610b4357610b42610954565b5b5f610b508582860161099e565b9250506020610b618582860161099e565b9150509250929050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52602260045260245ffd5b5f6002820490506001821680610baf57607f821691505b602082108103610bc257610bc1610b6b565b5b50919050565b7f496e73756666696369656e742062616c616e63650000000000000000000000005f82015250565b5f610bfc6014836108ce565b9150610c0782610bc8565b602082019050919050565b5f6020820190508181035f830152610c2981610bf0565b9050919050565b7f416c6c6f77616e636520657863656564656400000000000000000000000000005f82015250565b5f610c646012836108ce565b9150610c6f82610c30565b602082019050919050565b5f6020820190508181035f830152610c9181610c58565b9050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52601160045260245ffd5b5f610ccf826109b2565b9150610cda836109b2565b9250828203905081811115610cf257610cf1610c98565b5b92915050565b5f610d02826109b2565b9150610d0d836109b2565b9250828201905080821115610d2557610d24610c98565b5b9291505056fea2646970667358221220c1004b811e293b8d6389ecb2f55e470b5f77fe123ea9536b3017e3a6fba5df1f64736f6c634300081a0033']
        bytecode = contract_interface['[
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "address",
				"name": "spender",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "value",
				"type": "uint256"
			}
		],
		"name": "Approval",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "from",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "value",
				"type": "uint256"
			}
		],
		"name": "Transfer",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"name": "allowance",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_spender",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "_value",
				"type": "uint256"
			}
		],
		"name": "approve",
		"outputs": [
			{
				"internalType": "bool",
				"name": "success",
				"type": "bool"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"name": "balanceOf",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "decimals",
		"outputs": [
			{
				"internalType": "uint8",
				"name": "",
				"type": "uint8"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "name",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "symbol",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "totalSupply",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_to",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "_value",
				"type": "uint256"
			}
		],
		"name": "transfer",
		"outputs": [
			{
				"internalType": "bool",
				"name": "success",
				"type": "bool"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_from",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "_to",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "_value",
				"type": "uint256"
			}
		],
		"name": "transferFrom",
		"outputs": [
			{
				"internalType": "bool",
				"name": "success",
				"type": "bool"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	}
        ]']

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
