import Wold_Virtual.BK_Adm_prb.BK_Inicio.BK_Blockchain_Principal.Bk_Servidor.BK_RCS.BK_Admin_web.BK_Scr1.BK_Utils.BK_log.almacenamiento2 as almacenamiento2

def generate_new_block(data):
    """
    Genera un nuevo bloque en la blockchain con los datos proporcionados.
    
    Args:
        data (str): Datos a incluir en el nuevo bloque.
    """
    blockchain = almacenamiento2.Blockchain()
    new_block = almacenamiento2.Block(len(blockchain.chain), almacenamiento2.time.time(), data, blockchain.get_latest_block().hash)
    blockchain.add_block(new_block)
    print(f"Nuevo bloque generado: Índice: {new_block.index}, Hash: {new_block.hash}, Datos: {new_block.data}")

def validate_blockchain():
    """
    Valida la integridad de la blockchain verificando los hashes de cada bloque.
    
    Returns:
        bool: True si la blockchain es válida, False en caso contrario.
    """
    blockchain = almacenamiento2.Blockchain()
    for i in range(1, len(blockchain.chain)):
        current_block = blockchain.chain[i]
        previous_block = blockchain.chain[i - 1]
        
        # Verifica el hash del bloque actual
        if current_block.hash != current_block.calculate_hash():
            print(f"Error: El hash del bloque {current_block.index} no es válido.")
            return False
        
        # Verifica el hash del bloque anterior
        if current_block.previous_hash != previous_block.hash:
            print(f"Error: El hash del bloque anterior {current_block.index} no coincide.")
            return False
    
    print("La blockchain es válida.")
    return True

# Ejemplo de uso de las funciones adicionales
generate_new_block("Datos del nuevo bloque")
validate_blockchain()
