from prb2 import TokenICO
from prb3 import PixlNFT
from prb4 import WoldcoinVirtual
from prb5 import Blockchain, Block
import time

def main():
    # Inicializar blockchain
    blockchain = Blockchain()

    # Ejemplo de uso de TokenICO
    ico = TokenICO(1000)
    ico.purchase_tokens("buyer_address", 10, 10)
    ico.withdraw_funds()
    blockchain.add_block(Block(1, blockchain.get_latest_block_hash(), "TokenICO Transactions", time.time()))

    # Ejemplo de uso de PixlNFT
    nft = PixlNFT()
    nft.create_token("creator_address", "token_uri_example", 1)
    blockchain.add_block(Block(2, blockchain.get_latest_block_hash(), "PixlNFT Transactions", time.time()))

    # Ejemplo de uso de WoldcoinVirtual
    wcv = WoldcoinVirtual()
    wcv.transfer("owner_address", "recipient_address", 1000)
    wcv.stake("owner_address", 500)
    wcv.unstake("owner_address", 500)
    blockchain.add_block(Block(3, blockchain.get_latest_block_hash(), "WoldcoinVirtual Transactions", time.time()))

    # Verificar la validez de la blockchain
    print("Blockchain válida:", blockchain.is_chain_valid())
    for block in blockchain.chain:
        print(f"Index: {block.index}, Hash: {block.hash}, Previous Hash: {block.previous_hash}, Transactions: {block.transactions}")

if __name__ == "__main__":
    main()
