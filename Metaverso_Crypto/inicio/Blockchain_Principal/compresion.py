# compresion.py

import json
import gzip

def comprimir_y_guardar_datos(datos, archivo_salida):
    """
    Comprime los datos y los guarda en un archivo.
    """
    try:
        # Serializar los datos a formato JSON y codificarlos en UTF-8
        datos_serializados = json.dumps(datos).encode('utf-8')
        # Comprimir los datos serializados
        datos_comprimidos = gzip.compress(datos_serializados)
        # Guardar los datos comprimidos en un archivo
        with open(archivo_salida, 'wb') as archivo:
            archivo.write(datos_comprimidos)
        print(f"Datos comprimidos y guardados en {archivo_salida}")
    except Exception as e:
        print(f"Error al comprimir y guardar datos: {e}")

def cargar_y_descomprimir_datos(archivo_entrada):
    """
    Carga y descomprime los datos de un archivo.
    """
    try:
        # Leer los datos comprimidos del archivo
        with open(archivo_entrada, 'rb') as archivo:
            datos_comprimidos = archivo.read()
        # Descomprimir los datos
        datos_descomprimidos = gzip.decompress(datos_comprimidos)
        # Deserializar los datos de formato JSON
        return json.loads(datos_descomprimidos)
    except Exception as e:
        print(f"Error al cargar y descomprimir datos: {e}")
        return None
