from web3 import Web3

def connect_to_web3():
    web3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
    if web3.isConnected():
        print("Connected to Ethereum node")
    else:
        print("Failed to connect")
