import json
import gzip

def comprimir_y_guardar_datos(datos, archivo_salida):
    """
    Comprime y guarda los datos en un archivo.

    Args:
        datos (dict): Datos a comprimir.
        archivo_salida (str): Ruta del archivo de salida.
    """
    try:
        # Serializar y comprimir los datos
        datos_serializados = json.dumps(datos).encode('utf-8')
        datos_comprimidos = gzip.compress(datos_serializados)
        
        # Guardar los datos comprimidos en el archivo
        with open(archivo_salida, 'wb') as archivo:
            archivo.write(datos_comprimidos)
        
        print(f"Datos comprimidos y guardados en {archivo_salida}")
    except Exception as e:
        print(f"Error al comprimir y guardar datos: {e}")

def cargar_y_descomprimir_datos(archivo_entrada):
    """
    Carga y descomprime los datos de un archivo.

    Args:
        archivo_entrada (str): Ruta del archivo de entrada.

    Returns:
        dict: Datos descomprimidos.
    """
    try:
        # Leer y descomprimir los datos del archivo
        with open(archivo_entrada, 'rb') as archivo:
            datos_comprimidos = archivo.read()
        datos_descomprimidos = gzip.decompress(datos_comprimidos)
        
        return json.loads(datos_descomprimidos)
    except Exception as e:
        print(f"Error al cargar y descomprimir datos: {e}")
        return None

def actualizar_datos_comprimidos(archivo_entrada, nuevos_datos):
    """
    Actualiza los datos comprimidos en un archivo con nuevos datos.

    Args:
        archivo_entrada (str): Ruta del archivo de entrada.
        nuevos_datos (dict): Nuevos datos para actualizar en el archivo.
    """
    try:
        # Cargar y descomprimir los datos existentes
        datos_existentes = cargar_y_descomprimir_datos(archivo_entrada)
        if datos_existentes is None:
            datos_existentes = {}

        # Validar los nuevos datos
        if not isinstance(nuevos_datos, dict):
            print("Error: Los nuevos datos deben ser un diccionario.")
            return

        # Actualizar los datos existentes con los nuevos datos
        datos_existentes.update(nuevos_datos)

        # Comprimir y guardar los datos actualizados
        comprimir_y_guardar_datos(datos_existentes, archivo_entrada)
        print(f"Datos actualizados en el archivo {archivo_entrada}")
    except Exception as e:
        print(f"Error al actualizar datos comprimidos: {e}")
