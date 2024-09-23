import os
import tarfile
from avatarbs2 import log_action

storage_path = '/workspaces/WoldVirtual.github.io/Metaverso_Crypto/inicio/Blockchain_Principal/Almacenamiento'

def comprimir_datos(datos, archivo):
    output_filepath = os.path.join(storage_path, archivo)
    with tarfile.open(output_filepath, 'w:gz') as tar:
        for file in datos:
            if os.path.isfile(file):
                tar.add(file, arcname=os.path.basename(file))
    log_action(f"Datos comprimidos en {archivo}")

def descomprimir_datos(archivo):
    input_filepath = os.path.join(storage_path, archivo)
    with tarfile.open(input_filepath, 'r:gz') as tar:
        tar.extractall(path=storage_path)
    log_action(f"Datos descomprimidos de {archivo}")
    
