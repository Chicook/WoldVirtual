import time
from Metaverso_Crypto.inicio.Zona_depruebas.webadministrativa.Blockchain_Principal.Zona_de_pruebas.admin.pruebas2.Bk_Servidor.BK_dbts.src.BK_mdsl.BK_app2 import Block, Blockchain

blockchain = Blockchain()

def log_action(data):
    new_block = Block(len(blockchain.chain), time.time(), data, blockchain.get_latest_block().hash if blockchain.chain else "0")
    blockchain.add_block(new_block)
    print(f"Acción registrada: {data}")
