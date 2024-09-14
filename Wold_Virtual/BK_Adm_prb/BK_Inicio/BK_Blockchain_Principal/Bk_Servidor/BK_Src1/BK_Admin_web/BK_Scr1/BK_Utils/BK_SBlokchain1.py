import hashlib
import datetime
import time
from Metaverso_Crypto.inicio.Zona_depruebas.webadministrativa.Blockchain_Principal.Zona_de_pruebas.admin.pruebas2.Bk_Servidor.BK_dbts.src.BK_mdsl.BK_SBlokchain2 import create_interface
from SBlokchain3  import app
from Wold_Virtual.BK_Adm_prb.BK_Inicio.BK_Blockchain_Principal.Bk_Servidor.BK_RCS.BK_Admin_web.BK_Scr1.BK_Utils.BK_log.SBlokchain4 import connect_to_web3
from Wold_Virtual.BK_Adm_prb.BK_Inicio.BK_Blockchain_Principal.Bk_Servidor.BK_RCS.BK_Admin_web.BK_Scr1.BK_Utils.BK_log.SBlokchain5 import get_current_time, sleep

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []

    def new_block(self):
        # Implementación para añadir un bloque a la cadena
        pass

    def new_transaction(self):
        # Implementación para añadir una transacción
        pass

    def hash_function(self, data):
        return hashlib.sha256(data.encode()).hexdigest()

if __name__ == '__main__':
    # Crear instancia de Blockchain
    blockchain = Blockchain()

    # Conectar a Web3
    connect_to_web3()

    # Crear interfaz gráfica
    create_interface()

    # Iniciar servidor web
    app.run(debug=True)

