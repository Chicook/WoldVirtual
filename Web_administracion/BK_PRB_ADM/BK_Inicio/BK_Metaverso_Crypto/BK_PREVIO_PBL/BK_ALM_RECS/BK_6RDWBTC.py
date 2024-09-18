from bitcoinlib.wallets import Wallet
from bitcoinlib.services.services import Service

class BitcoinNetwork:
    def __init__(self):
        self.service = Service(network='bitcoin')

    def create_wallet(self, wallet_name):
        wallet = Wallet.create(wallet_name, network='bitcoin')
        return wallet

    def get_balance(self, wallet_name):
        wallet = Wallet(wallet_name)
        return wallet.balance()

    def send_bitcoins(self, wallet_name, address, amount):
        wallet = Wallet(wallet_name)
        tx = wallet.send_to(address, amount)
        return tx.txid

    def check_transaction(self, txid):
        tx_info = self.service.gettransaction(txid)
        return tx_info

# Ejemplo de uso
if __name__ == "__main__":
    bitcoin_network = BitcoinNetwork()
    wallet_name = 'MiWallet'
    
    # Crear una nueva wallet
    wallet = bitcoin_network.create_wallet(wallet_name)
    print(f"Nueva wallet creada: {wallet.name}")

    # Obtener el balance de la wallet
    balance = bitcoin_network.get_balance(wallet_name)
    print(f"Balance de la wallet: {balance} BTC")

    # Enviar bitcoins
    address = 'DIRECCIÓN_DE_DESTINO'
    amount = 1000  # En satoshis (0.00001 BTC)
    txid = bitcoin_network.send_bitcoins(wallet_name, address, amount)
    print(f"Transacción enviada: {txid}")

    # Verificar el estado de la transacción
    tx_info = bitcoin_network.check_transaction(txid)
    print(f"Información de la transacción: {tx_info}")
      
