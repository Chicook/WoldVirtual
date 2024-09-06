# modulo compresion # 

import json
import gzip
import os

def comprimir_y_guardar_datos(datos, archivo_salida, carpeta_destino='almacenamiento'):
    """
    Comprime y guarda los datos en un archivo en la carpeta de destino.

    Args:
        datos (dict): Datos a comprimir.
        archivo_salida (str): Nombre del archivo comprimido (sin ruta).
        carpeta_destino (str): Carpeta donde se guardará el archivo.
    """
    try:
        # Crear la carpeta de destino si no existe
        if not os.path.exists(carpeta_destino):
            os.makedirs(carpeta_destino)

        # Serializar y comprimir los datos
        datos_serializados = json.dumps(datos).encode('utf-8')
        datos_comprimidos = gzip.compress(datos_serializados)

        # Crear la ruta completa del archivo de salida
        ruta_archivo = os.path.join(carpeta_destino, archivo_salida)

        # Guardar los datos comprimidos en el archivo
        with open(ruta_archivo, 'wb') as archivo:
            archivo.write(datos_comprimidos)

        print(f"Datos comprimidos y guardados en {ruta_archivo}")
        return ruta_archivo  # Retorna la ruta del archivo comprimido

    except Exception as e:
        print(f"Error al comprimir y guardar datos: {e}")
        return None

def cargar_y_descomprimir_datos(archivo_entrada):
    """
    Carga y descomprime los datos de un archivo.

    Args:
        archivo_entrada (str): Ruta del archivo comprimido.

    Returns:
        dict: Datos descomprimidos, o None en caso de error.
    """
    try:
        # Verificar si el archivo existe
        if not os.path.exists(archivo_entrada):
            raise FileNotFoundError(f"El archivo {archivo_entrada} no existe.")

        # Leer y descomprimir los datos del archivo
        with open(archivo_entrada, 'rb') as archivo:
            datos_comprimidos = archivo.read()

        datos_descomprimidos = gzip.decompress(datos_comprimidos)
        return json.loads(datos_descomprimidos)

    except FileNotFoundError as fnf_error:
        print(fnf_error)
        return None
    except Exception as e:
        print(f"Error al cargar y descomprimir datos: {e}")
        return None

def eliminar_archivo(archivo):
    """
    Elimina un archivo del sistema.

    Args:
        archivo (str): Ruta del archivo a eliminar.
    """
    try:
        if os.path.exists(archivo):
            os.remove(archivo)
            print(f"Archivo {archivo} eliminado correctamente.")
        else:
            print(f"El archivo {archivo} no existe.")
    except Exception as e:
        print(f"Error al eliminar el archivo {archivo}: {e}")

def listar_archivos(carpeta):
    """
    Lista todos los archivos en una carpeta.

    Args:
        carpeta (str): Ruta de la carpeta donde listar archivos.

    Returns:
        list: Lista de archivos en la carpeta.
    """
    try:
        if os.path.exists(carpeta):
            archivos = os.listdir(carpeta)
            print(f"Archivos en la carpeta {carpeta}: {archivos}")
            return archivos
        else:
            print(f"La carpeta {carpeta} no existe.")
            return []
    except Exception as e:
        print(f"Error al listar archivos en la carpeta {carpeta}: {e}")
        return []

def mover_archivo(origen, destino):
    """
    Mueve un archivo de una ubicación a otra.

    Args:
        origen (str): Ruta de origen del archivo.
        destino (str): Ruta de destino del archivo.
    """
    try:
        shutil.move(origen, destino)
        print(f"Archivo movido de {origen} a {destino}.")
    except Exception as e:
        print(f"Error al mover el archivo {origen} a {destino}: {e}")
            
# modulo compresion #

# import json
# import gzip

# def comprimir_y_guardar_datos(datos, archivo_salida):
   # """
  #  Comprime y guarda los datos en un archivo.

    # Args:
       # datos (dict): Datos a comprimir.
       # archivo_salida (str): Ruta del archivo de salida.
  #  """
    # try:
        # Serializar y comprimir los datos
       # datos_serializados = json.dumps(datos).encode('utf-8')
       # datos_comprimidos = gzip.compress(datos_serializados)
        
        # Guardar los datos comprimidos en el archivo
       # with open(archivo_salida, 'wb') as archivo:
          #  archivo.write(datos_comprimidos)
        
       # print(f"Datos comprimidos y guardados en {archivo_salida}")
    #  except Exception as e:
       # print(f"Error al comprimir y guardar datos: {e}")

# def cargar_y_descomprimir_datos(archivo_entrada):
   # """
  #  Carga y descomprime los datos de un archivo.

   # Args:
      #  archivo_entrada (str): Ruta del archivo de entrada.

  #  Returns:
       # dict: Datos descomprimidos.
  #  """
   # try:
        # Leer y descomprimir los datos del archivo
       # with open(archivo_entrada, 'rb') as archivo:
           # datos_comprimidos = archivo.read()
     #   datos_descomprimidos = gzip.decompress(datos_comprimidos)
        
       # return json.loads(datos_descomprimidos)
#    except Exception as e:
       # print(f"Error al cargar y descomprimir datos: {e}")
      #  return None

# compresion.py

# import json
# import gzip

# def comprimir_y_guardar_datos(datos, archivo_salida):
    # try:
       # datos_serializados = json.dumps(datos).encode('utf-8')
       # datos_comprimidos = gzip.compress(datos_serializados)
        # with open(archivo_salida, 'wb') as archivo:
           # archivo.write(datos_comprimidos)
        # print(f"Datos comprimidos y guardados en {archivo_salida}")
    # except Exception as e:
       #  print(f"Error al comprimir y guardar datos: {e}")

# def cargar_y_descomprimir_datos(archivo_entrada):
    # try:
       #  with open(archivo_entrada, 'rb') as archivo:
           # datos_comprimidos = archivo.read()
      #  datos_descomprimidos = gzip.decompress(datos_comprimidos)
      #  return json.loads(datos_descomprimidos)
   # except Exception as e:
       # print(f"Error al cargar y descomprimir datos: {e}")
        # return None
