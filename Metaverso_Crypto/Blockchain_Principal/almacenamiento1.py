import os
import tarfile
import hashlib
import time

# Ruta donde se almacenan los archivos comprimidos y descomprimidos
storage_path = '/workspaces/WoldVirtual.github.io/Metaverso_Crypto/inicio/Blockchain_Principal/Almacenamiento'

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, time.time(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

class User:
    def __init__(self, user_id, wallet):
        self.user_id = user_id
        self.wallet = wallet

    def send_wcv(self, amount, recipient_wallet):
        # Lógica para enviar WCV
        print(f"{self.user_id} envió {amount} WCV a {recipient_wallet}")

    def receive_wcv(self, amount, sender_wallet):
        # Lógica para recibir WCV
        print(f"{self.user_id} recibió {amount} WCV de {sender_wallet}")

# Inicializar la blockchain
blockchain = Blockchain()

def log_action(data):
    """
    Registra una acción en la blockchain.
    
    Args:
        data (str): Descripción de la acción a registrar.
    """
    new_block = Block(len(blockchain.chain), time.time(), data, blockchain.get_latest_block().hash)
    blockchain.add_block(new_block)
    print(f"Acción registrada: {data}")

def compress_files(files, output_filename):
    """
    Comprime una lista de archivos en un archivo tar.gz.
    
    Args:
        files (list): Lista de rutas de archivos a comprimir.
        output_filename (str): Nombre del archivo tar.gz de salida.
    """
    output_filepath = os.path.join(storage_path, output_filename)
    
    # Verifica que los archivos existan antes de intentar comprimirlos
    for file in files:
        if not os.path.isfile(file):
            print(f"Advertencia: El archivo {file} no existe y no será incluido en la compresión.")
    
    with tarfile.open(output_filepath, 'w:gz') as tar:
        for file in files:
            if os.path.isfile(file):  # Solo añade los archivos existentes
                tar.add(file, arcname=os.path.basename(file))
    
    print(f'Archivos comprimidos en {output_filename}, guardado en {output_filepath}')
    log_action(f"Comprimidos archivos en {output_filename}")

def decompress_file(input_filename):
    """
    Descomprime un archivo tar.gz en el directorio de almacenamiento.

    Args:
        input_filename (str): Nombre del archivo tar.gz a descomprimir.
    """
    input_filepath = os.path.join(storage_path, input_filename)
    
    # Verifica que el archivo de entrada exista antes de intentar descomprimirlo
    if not os.path.isfile(input_filepath):
        print(f"Error: El archivo {input_filepath} no existe.")
        return
    
    with tarfile.open(input_filepath, 'r:gz') as tar:
        tar.extractall(path=storage_path)
    
    print(f'Archivos descomprimidos en {storage_path}')
    log_action(f"Descomprimido archivo {input_filename}")

# Ejemplo de uso
user1 = User("user1", "wallet1")
user2 = User("user2", "wallet2")

# Simular una transacción
user1.send_wcv(100, user2.wallet)
log_action("User1 envió 100 WCV a User2")

# Mostrar la cadena de bloques
for block in blockchain.chain:
    print(f"Índice: {block.index}, Hash: {block.hash}, Datos: {block.data}")

# Ejemplo de compresión y descompresión
compress_files(['file1.txt', 'file2.txt'], 'output.tar.gz')
decompress_file('output.tar.gz')
