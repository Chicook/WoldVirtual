import json
import gzip
import logging

# Configurar el registro
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def comprimir_y_guardar_datos(datos, archivo_salida):
    """
    Comprime los datos y los guarda en un archivo.
    
    :param datos: Datos a comprimir (dict).
    :param archivo_salida: Nombre del archivo de salida (str).
    """
    try:
        datos_serializados = json.dumps(datos).encode('utf-8')
        datos_comprimidos = gzip.compress(datos_serializados)
        with open(archivo_salida, 'wb') as archivo:
            archivo.write(datos_comprimidos)
        logging.info(f"Datos comprimidos y guardados en {archivo_salida}")
    except Exception as e:
        logging.error(f"Error al comprimir y guardar datos: {e}")

def cargar_y_descomprimir_datos(archivo_entrada):
    """
    Carga y descomprime los datos de un archivo.
    
    :param archivo_entrada: Nombre del archivo de entrada (str).
    :return: Datos descomprimidos (dict).
    """
    try:
        with open(archivo_entrada, 'rb') as archivo:
            datos_comprimidos = archivo.read()
        datos_descomprimidos = gzip.decompress(datos_comprimidos)
        logging.info(f"Datos cargados y descomprimidos de {archivo_entrada}")
        return json.loads(datos_descomprimidos)
    except Exception as e:
        logging.error(f"Error al cargar y descomprimir datos: {e}")
        return None
