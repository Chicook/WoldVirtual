# prb1.py
from Metaverso_Crypto.inicio.Zona_depruebas.webadministrativa.Blockchain_Principal.Zona_de_pruebas.admin.pruebas2.Bk_Servidor.BK_dbts.src.BK_Scv.prb2 import Blockchain
from prb3 import User
from prb4 import hash_block
from prb5 import register_user

def main():
    blockchain = Blockchain()
    while True:
        username = input("Introduce el nombre de usuario: ")
        user = User(username)
        register_user(blockchain, user)
        print(f"Usuario {username} registrado con éxito.")
        print(f"Blockchain: {blockchain.chain}")

if __name__ == "__main__":
    main()

