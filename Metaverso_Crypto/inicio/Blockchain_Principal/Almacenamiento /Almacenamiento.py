import os
import tarfile

storage_path = '/workspaces/WoldVirtual.github.io/Metaverso_Crypto/inicio/Blockchain_Principal/Almacenamiento'

def compress_files(files, output_filename):
    with tarfile.open(os.path.join(storage_path, output_filename), 'w:gz') as tar:
        for file in files:
            tar.add(file, arcname=os.path.basename(file))
    print(f'Archivos comprimidos en {output_filename}')

def decompress_file(input_filename):
    with tarfile.open(os.path.join(storage_path, input_filename), 'r:gz') as tar:
        tar.extractall(path=storage_path)
    print(f'Archivos descomprimidos en {storage_path}')
