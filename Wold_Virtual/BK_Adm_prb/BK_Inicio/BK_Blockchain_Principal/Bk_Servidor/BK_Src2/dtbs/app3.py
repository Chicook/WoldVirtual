import time
from Wold_Virtual.BK_Adm_prb.BK_Inicio.BK_Blockchain_Principal.Bk_Servidor.BK_RCS.BK_Admin_web.BK_Scr1.BK_Utils.app2 import Block, Blockchain

blockchain = Blockchain()

def log_action(data):
    new_block = Block(len(blockchain.chain), time.time(), data, blockchain.get_latest_block().hash if blockchain.chain else "0")
    blockchain.add_block(new_block)
    print(f"Acción registrada: {data}")
