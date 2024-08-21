# almacenamiento.py

import os
import tarfile

# Ruta donde se almacenan los archivos comprimidos y descomprimidos
storage_path = '/workspaces/WoldVirtual.github.io/Metaverso_Crypto/inicio/Blockchain_Principal/Almacenamiento/almacenamiento.py"

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
