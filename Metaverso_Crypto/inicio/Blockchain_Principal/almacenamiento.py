# modulo Almacenamiento #

import gzip
import shutil
import os
import hashlib

def comprimir_y_guardar_datos(datos, archivo_salida):
    """
    Comprime y guarda los datos en un archivo .gz.
    """
    try:
        with gzip.open(archivo_salida, 'wb') as archivo_comprimido:
            archivo_comprimido.write(str(datos).encode('utf-8'))
        print(f"Datos comprimidos y guardados en {archivo_salida}.")
    except Exception as e:
        print(f"Error al comprimir y guardar los datos: {e}")

def cargar_y_descomprimir_datos(archivo_comprimido):
    """
    Carga y descomprime los datos desde un archivo .gz.
    """
    try:
        with gzip.open(archivo_comprimido, 'rb') as archivo:
            datos = archivo.read().decode('utf-8')
            print(f"Datos descomprimidos desde {archivo_comprimido}.")
            return datos
    except Exception as e:
        print(f"Error al descomprimir los datos: {e}")
        return None

def eliminar_archivo(archivo):
    """
    Elimina un archivo del sistema de archivos.
    """
    try:
        if os.path.exists(archivo):
            os.remove(archivo)
            print(f"Archivo {archivo} eliminado.")
        else:
            print(f"El archivo {archivo} no existe.")
    except Exception as e:
        print(f"Error al eliminar el archivo: {e}")

def listar_archivos(directorio):
    """
    Lista todos los archivos en un directorio.
    """
    try:
        archivos = os.listdir(directorio)
        print(f"Archivos en {directorio}: {archivos}")
        return archivos
    except Exception as e:
        print(f"Error al listar los archivos: {e}")
        return []

def mover_archivo(origen, destino):
    """
    Mueve un archivo de una ubicación a otra.
    """
    try:
        shutil.move(origen, destino)
        print(f"Archivo movido de {origen} a {destino}.")
    except Exception as e:
        print(f"Error al mover el archivo: {e}")

def copiar_archivo(origen, destino):
    """
    Copia un archivo de una ubicación a otra.
    """
    try:
        shutil.copy(origen, destino)
        print(f"Archivo copiado de {origen} a {destino}.")
    except Exception as e:
        print(f"Error al copiar el archivo: {e}")

def verificar_integridad(archivo_original, archivo_copia):
    """
    Verifica la integridad de un archivo comparando su hash con una copia.
    """
    try:
        hash_original = calcular_hash_archivo(archivo_original)
        hash_copia = calcular_hash_archivo(archivo_copia)

        if hash_original == hash_copia:
            print(f"Integridad verificada: {archivo_original} y {archivo_copia} son iguales.")
            return True
        else:
            print(f"Integridad fallida: {archivo_original} y {archivo_copia} son diferentes.")
            return False
    except Exception as e:
        print(f"Error al verificar la integridad de los archivos: {e}")
        return False

def calcular_hash_archivo(archivo):
    """
    Calcula el hash SHA-256 de un archivo para verificar su integridad.
    """
    try:
        sha256_hash = hashlib.sha256()
        with open(archivo, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except Exception as e:
        print(f"Error al calcular el hash del archivo: {e}")
        return None

def crear_directorio(directorio):
    """
    Crea un directorio si no existe.
    """
    try:
        os.makedirs(directorio, exist_ok=True)
        print(f"Directorio {directorio} creado o ya existía.")
    except Exception as e:
        print(f"Error al crear el directorio {directorio}: {e}")

def comprimir_directorio(directorio, archivo_salida):
    """
    Comprime un directorio completo en un archivo .tar.gz.
    """
    try:
        shutil.make_archive(archivo_salida.replace('.tar.gz', ''), 'gztar', directorio)
        print(f"Directorio {directorio} comprimido en {archivo_salida}.")
    except Exception as e:
        print(f"Error al comprimir el directorio: {e}")

def descomprimir_archivo(archivo_comprimido, directorio_destino):
    """
    Descomprime un archivo .tar.gz en el directorio de destino.
    """
    try:
        shutil.unpack_archive(archivo_comprimido, directorio_destino)
        print(f"Archivo {archivo_comprimido} descomprimido en {directorio_destino}.")
    except Exception as e:
        print(f"Error al descomprimir el archivo: {e}")

# modulo almacenamiento #

# import gzip
# import shutil
# import os

# def comprimir_y_guardar_datos(datos, archivo_salida):
   #  """
   # Comprime y guarda los datos en un archivo .gz.

  #  Args:
       # datos (dict): Datos a comprimir.
      #  archivo_salida (str): Ruta del archivo de salida.
  #  """
  #  try:
     #   with gzip.open(archivo_salida, 'wb') as archivo_comprimido:
            # archivo_comprimido.write(str(datos).encode('utf-8'))
      #  print(f"Datos comprimidos y guardados en {archivo_salida}.")
   # except Exception as e:
       # print(f"Error al comprimir y guardar los datos: {e}")

# def cargar_y_descomprimir_datos(archivo_comprimido):
   # """
   # Carga y descomprime los datos desde un archivo .gz.

 #   Args:
       # archivo_comprimido (str): Ruta del archivo comprimido.

  #  Returns:
       # str: Datos descomprimidos.
 #   """
  #  try:
      #  with gzip.open(archivo_comprimido, 'rb') as archivo:
           # datos = archivo.read().decode('utf-8')
           # print(f"Datos descomprimidos desde {archivo_comprimido}.")
         #   return datos
   # except Exception as e:
       # print(f"Error al descomprimir los datos: {e}")
       # return None

# def eliminar_archivo(archivo):
  #  """
   # Elimina un archivo del sistema de archivos.

   # Args:
     #   archivo (str): Ruta del archivo a eliminar.
  #  """
  #  try:
      #  if os.path.exists(archivo):
         #   os.remove(archivo)
          #  print(f"Archivo {archivo} eliminado.")
     #   else:
         #   print(f"El archivo {archivo} no existe.")
 #   except Exception as e:
      #  print(f"Error al eliminar el archivo: {e}")

# def listar_archivos(directorio):
   # """
   # Lista todos los archivos en un directorio.

   # Args:
       # directorio (str): Ruta del directorio.

  #  Returns:
       # list: Lista de archivos en el directorio.
 #   """
   # try:
     #   archivos = os.listdir(directorio)
      #  print(f"Archivos en {directorio}: {archivos}")
     #   return archivos
 #   except Exception as e:
      #  print(f"Error al listar los archivos: {e}")
      #  return []

# def mover_archivo(origen, destino):
  #  """
 #   Mueve un archivo de una ubicación a otra.

  #  Args:
      #  origen (str): Ruta del archivo de origen.
       # destino (str): Ruta del archivo de destino.
 #   """
   # try:
      #  shutil.move(origen, destino)
      #  print(f"Archivo movido de {origen} a {destino}.")
  #  except Exception as e:
      #  print(f"Error al mover el archivo: {e}")

# import os
# import tarfile

# Ruta donde se almacenan los archivos comprimidos y descomprimidos
# storage_path = '/workspaces/WoldVirtual/Metaverso_Crypto/inicio/Blockchain_Principal/Almacenamiento'

# def compress_files(files, output_filename):
   # """
  #  Comprime una lista de archivos en un archivo tar.gz.
    
   # Args:
       # files (list): Lista de rutas de archivos a comprimir.
      #  output_filename (str): Nombre del archivo tar.gz de salida.
  #  """
   # output_filepath = os.path.join(storage_path, output_filename)
    
    # Verifica que los archivos existan antes de intentar comprimirlos
   # for file in files:
        # if not os.path.isfile(file):
         #   print(f"Advertencia: El archivo {file} no existe y no será incluido en la compresión.")
    
  #  with tarfile.open(output_filepath, 'w:gz') as tar:
       # for file in files:
           # if os.path.isfile(file):  # Solo añade los archivos existentes
              #  tar.add(file, arcname=os.path.basename(file))
    
 #   print(f'Archivos comprimidos en {output_filename}, guardado en {output_filepath}')

# def decompress_file(input_filename):
   # """
  #  Descomprime un archivo tar.gz en el directorio de almacenamiento.

  #  Args:
       # input_filename (str): Nombre del archivo tar.gz a descomprimir.
  #  """
  #  input_filepath = os.path.join(storage_path, input_filename)
    
    # Verifica que el archivo de entrada exista antes de intentar descomprimirlo
   # if not os.path.isfile(input_filepath):
       # print(f"Error: El archivo {input_filepath} no existe.")
      #  return
    
   # with tarfile.open(input_filepath, 'r:gz') as tar:
      #  tar.extractall(path=storage_path)
    
 #   print(f'Archivos descomprimidos en {storage_path}')

# import os
# import tarfile

# Ruta donde se almacenan los archivos comprimidos y descomprimidos
# storage_path = '/workspaces/WoldVirtual.github.io/Metaverso_Crypto/inicio/Blockchain_Principal/Almacenamiento'

# def compress_files(files, output_filename):
   # """
  #  Comprime una lista de archivos en un archivo tar.gz.
    
   # Args:
       # files (list): Lista de rutas de archivos a comprimir.
       # output_filename (str): Nombre del archivo tar.gz de salida.
  #  """
   # output_filepath = os.path.join(storage_path, output_filename)
    
    # Verifica que los archivos existan antes de intentar comprimirlos
  #  for file in files:
       # if not os.path.isfile(file):
          #  print(f"Advertencia: El archivo {file} no existe y no será incluido en la compresión.")
    
  #  with tarfile.open(output_filepath, 'w:gz') as tar:
       # for file in files:
            # if os.path.isfile(file):  # Solo añade los archivos existentes
              #  tar.add(file, arcname=os.path.basename(file))
    
  #  print(f'Archivos comprimidos en {output_filename}, guardado en {output_filepath}')

# def decompress_file(input_filename):
  #  """
   # Descomprime un archivo tar.gz en el directorio de almacenamiento.

   # Args:
      #  input_filename (str): Nombre del archivo tar.gz a descomprimir.
 #   """
    # input_filepath = os.path.join(storage_path, input_filename)
    
    # Verifica que el archivo de entrada exista antes de intentar descomprimirlo
   # if not os.path.isfile(input_filepath):
      #  print(f"Error: El archivo {input_filepath} no existe.")
      #  return
    
   # with tarfile.open(input_filepath, 'r:gz') as tar:
     #   tar.extractall(path=storage_path)
    
  #  print(f'Archivos descomprimidos en {storage_path}')

# almacenamiento.py

# import os
# import tarfile

# Ruta donde se almacenan los archivos comprimidos y descomprimidos
# storage_path = '/workspaces/WoldVirtual.github.io/Metaverso_Crypto/inicio/Blockchain_Principal/Almacenamiento'

# def compress_files(files, output_filename):
    # """
   #  Comprime una lista de archivos en un archivo tar.gz.
    
    # Args:
        # files (list): Lista de rutas de archivos a comprimir.
       #  output_filename (str): Nombre del archivo tar.gz de salida.
   # """
    #output_filepath = os.path.join(storage_path, output_filename)
    
    # Verifica que los archivos existan antes de intentar comprimirlos
   # for file in files:
        # if not os.path.isfile(file):
            # print(f"Advertencia: El archivo {file} no existe y no será incluido en la compresión.")
    
    # with tarfile.open(output_filepath, 'w:gz') as tar:
        # for file in files:
            # if os.path.isfile(file):  # Solo añade los archivos existentes
                # tar.add(file, arcname=os.path.basename(file))
    
    # print(f'Archivos comprimidos en {output_filename}, guardado en {output_filepath}')

# def decompress_file(input_filename):
    #"""
   #  Descomprime un archivo tar.gz en el directorio de almacenamiento.

   # Args:
       # input_filename (str): Nombre del archivo tar.gz a descomprimir.
    #"""
    # input_filepath = os.path.join(storage_path, input_filename)
    
    # Verifica que el archivo de entrada exista antes de intentar descomprimirlo
   # if not os.path.isfile(input_filepath):
       # print(f"Error: El archivo {input_filepath} no existe.")
        # return
    
   # with tarfile.open(input_filepath, 'r:gz') as tar:
       # tar.extractall(path=storage_path)
    
   # print(f'Archivos descomprimidos en {storage_path}')
