import Metaverso_Crypto.inicio.Zona_depruebas.webadministrativa.Blockchain_Principal.Zona_de_pruebas.admin.pruebas2.Bk_Servidor.BK_dbts.src.BK_Scv.prb2 as prb2
import prb3
import prb4
import prb5

# Inicializar la blockchain
blockchain = prb2.Blockchain()

def log_action(data):
    """
    Registra una acción en la blockchain.
    
    Args:
        data (str): Descripción de la acción a registrar.
    """
    new_block = prb2.Block(len(blockchain.chain), prb2.time.time(), data, blockchain.get_latest_block().hash)
    blockchain.add_block(new_block)
    print(f"Acción registrada: {data}")

# Ejemplo de uso
user1 = prb3.User("user1", "wallet1")
user2 = prb3.User("user2", "wallet2")

# Simular una transacción
user1.send_wcv(100, user2.wallet)
log_action("User1 envió 100 WCV a User2")

# Mostrar la cadena de bloques
for block in blockchain.chain:
    print(f"Índice: {block.index}, Hash: {block.hash}, Datos: {block.data}")

# Ejemplo de compresión y descompresión
prb4.compress_files(['file1.txt', 'file2.txt'], 'output.tar.gz')
prb4.decompress_file('output.tar.gz')
