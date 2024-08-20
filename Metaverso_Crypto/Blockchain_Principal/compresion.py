import json
import gzip

def comprimir_y_guardar_datos(datos, archivo_salida):
    datos_serializados = json.dumps(datos).encode('utf-8')
    datos_comprimidos = gzip.compress(datos_serializados)
    with open(archivo_salida, 'wb') as archivo:
    archivo.write(datos_comprimidos)

def cargar_y_descomprimir_datos(archivo_entrada):
    with open(archivo_entrada, 'rb') as archivo:
    datos_comprimidos = archivo.read()
    datos_descomprimidos = gzip.decompress(datos_comprimidos)
    return json.loads(datos_descomprimidos)
