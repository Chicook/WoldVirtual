# main #

from usuarios import registrar_usuario
from recursos import RecursosUsuario
from database import (conectar_base_datos, insertar_bloque, obtener_transacciones, insertar_transaccion, cerrar_conexion)
from compresion import comprimir_y_guardar_datos, cargar_y_descomprimir_datos
from almacenamiento import listar_archivos
from servidor import app, socketio
from blockchain import Blockchain, Bloque
import time
import logging

# Configurar el registro
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def inicializar_recursos(cpu: int = 50, ancho_banda: int = 50):
    """
    Inicializa los recursos asignados a un usuario y devuelve los recursos asignados.
    """
    try:
        recursos_usuario = RecursosUsuario(cpu, ancho_banda)
        recursos_comunitarios = {'cpu': 100, 'ancho_banda': 100}
        recursos_asignados = recursos_usuario.asignar_recursos(recursos_comunitarios)
        return recursos_asignados
    except Exception as e:
        logging.error(f"Error al inicializar recursos: {e}")
        raise

def conectar_bd():
    """
    Conecta a la base de datos y devuelve la conexión.
    """
    try:
        return conectar_base_datos()
    except Exception as e:
        logging.error(f"Error al conectar a la base de datos: {e}")
        raise

def crear_usuario(nombre, contraseña):
    """
    Registra un nuevo usuario.
    """
    try:
        registrar_usuario(nombre, contraseña)
    except Exception as e:
        logging.error(f"Error al registrar usuario: {e}")
        raise

def comprimir_datos(datos, archivo):
    """
    Comprime y guarda los datos en un archivo.
    """
    try:
        comprimir_y_guardar_datos(datos, archivo)
    except Exception as e:
        logging.error(f"Error al comprimir datos: {e}")
        raise

def cargar_datos(archivo):
    """
    Carga y descomprime los datos de un archivo.
    """
    try:
        return cargar_y_descomprimir_datos(archivo)
    except FileNotFoundError:
        logging.error(f"El archivo {archivo} no existe.")
        raise
    except Exception as e:
        logging.error(f"Error al cargar datos: {e}")
        raise

def procesar_transaccion(blockchain, transaccion):
    """
    Procesa una transacción en la blockchain.
    """
    try:
        blockchain.agregar_bloque(transaccion)
    except Exception as e:
        logging.error(f"Error al procesar transacción: {e}")
        raise

def iniciar_servidor():
    """
    Inicia el servidor Flask con SocketIO.
    """
    try:
        socketio.run(app, debug=True)
    except Exception as e:
        logging.error(f"Error al iniciar el servidor: {e}")
        raise

def main():
    """
    Función principal para inicializar recursos, conectar a la base de datos,
    registrar un usuario, comprimir y almacenar datos, procesar transacciones
    en la blockchain e iniciar el servidor.
    """
    try:
        logging.info("Inicializando recursos...")
        recursos_asignados = inicializar_recursos()
        logging.info(f"Recursos asignados: {recursos_asignados}")

        logging.info("Conectando a la base de datos...")
        conexion = conectar_bd()
        logging.info("Conexión a la base de datos establecida.")

        logging.info("Registrando un nuevo usuario...")
        crear_usuario("nombre", "contraseña")
        logging.info("Usuario registrado exitosamente.")

        logging.info("Comprimiendo y almacenando datos...")
        datos_usuario = {"nombre": "nombre", "datos": "datos_ejemplo"}
        archivo_comprimido = "datos_comprimidos.gz"
        comprimir_datos(datos_usuario, archivo_comprimido)
        logging.info("Datos comprimidos y almacenados exitosamente.")
        
        logging.info("Listando archivos en el directorio actual...")
        listar_archivos('.')

        logging.info("Cargando y descomprimiendo datos...")
        datos_descomprimidos = cargar_datos(archivo_comprimido)
        logging.info("Datos descomprimidos exitosamente.")
        
        logging.info("Inicializando blockchain y agregando bloque...")
        blockchain = Blockchain()
        nuevo_bloque = Bloque(len(blockchain.cadena), time.time(), datos_usuario, blockchain.cadena[-1].hash)
        blockchain.agregar_bloque(nuevo_bloque)
        logging.info("Bloque agregado a la blockchain exitosamente.")

        logging.info("Guardando el bloque en la base de datos...")
        insertar_bloque(conexion, nuevo_bloque)
        logging.info("Bloque guardado en la base de datos exitosamente.")

        logging.info("Manejando transacciones...")
        insertar_transaccion(conexion, "Usuario1", "Usuario2", 100)
        transacciones = obtener_transacciones(conexion)
        logging.info(f"Transacciones almacenadas: {transacciones}")

        logging.info("Cerrando la conexión a la base de datos...")
        cerrar_conexion(conexion)
        logging.info("Conexión a la base de datos cerrada.")

        logging.info("Iniciando el servidor...")
        iniciar_servidor()

    except Exception as e:
        logging.error(f"Error durante la ejecución: {e}")

if __name__ == "__main__":
    main()
    
# main.py

# from usuarios import registrar_usuario
# from recursos import RecursosUsuario
# from database import conectar_base_datos, insertar_bloque, obtener_transacciones, insertar_transaccion, cerrar_conexion
# from compresion import comprimir_y_guardar_datos, cargar_y_descomprimir_datos
# from almacenamiento import listar_archivos
# from servidor import app, socketio
# from blockchain import Blockchain, Bloque
# import time
# import logging

# Configurar el registro
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# def inicializar_recursos(cpu: int = 50, ancho_banda: int = 50):
   #  """
   # Inicializa los recursos asignados a un usuario y devuelve los recursos asignados.
    # """
    # recursos_usuario = RecursosUsuario(cpu, ancho_banda)
   # recursos_comunitarios = {'cpu': 100, 'ancho_banda': 100}
   # recursos_asignados = recursos_usuario.asignar_recursos(recursos_comunitarios)
   # return recursos_asignados

# def conectar_bd():
   # """
    # Conecta a la base de datos y devuelve la conexión.
   # """
   # return conectar_base_datos()

# def crear_usuario(nombre, contraseña):
   # """
  #  Registra un nuevo usuario.
   # """
    # registrar_usuario(nombre, contraseña)

# def comprimir_datos(datos, archivo):
  #  """
   # Comprime y guarda los datos en un archivo.
  #  """
   # comprimir_y_guardar_datos(datos, archivo)

# def procesar_transaccion(blockchain, transaccion):
    # """
   # Procesa una transacción en la blockchain.
   # """
   # blockchain.agregar_bloque(transaccion)

# def iniciar_servidor():
    # """
  #  Inicia el servidor Flask con SocketIO.
  #  """
   # socketio.run(app, debug=True)

# def main():
   # """
  #  Función principal para inicializar recursos, conectar a la base de datos,
   # registrar un usuario, comprimir y almacenar datos, procesar transacciones
  #  en la blockchain e iniciar el servidor.
   # """
  #  try:
      #  logging.info("Inicializando recursos...")
     #   recursos_asignados = inicializar_recursos()
    #    logging.info(f"Recursos asignados: {recursos_asignados}")

      #  logging.info("Conectando a la base de datos...")
       # conexion = conectar_bd()
     #   logging.info("Conexión a la base de datos establecida.")

       # logging.info("Registrando un nuevo usuario...")
     #   crear_usuario("nombre", "contraseña")
      #  logging.info("Usuario registrado exitosamente.")

      #  logging.info("Comprimiendo y almacenando datos...")
       # datos_usuario = {"nombre": "nombre", "datos": "datos_ejemplo"}
     #   archivo_comprimido = "datos_comprimidos.gz"
      #  comprimir_datos(datos_usuario, archivo_comprimido)
      #  logging.info("Datos comprimidos y almacenados exitosamente.")
        
      #  logging.info("Listando archivos en el directorio actual...")
      #  listar_archivos('.')

        # logging.info("Cargando y descomprimiendo datos...")
      #  datos_descomprimidos = cargar_y_descomprimir_datos(archivo_comprimido)
       # logging.info("Datos descomprimidos exitosamente.")
        
      #  logging.info("Inicializando blockchain y agregando bloque...")
      #  blockchain = Blockchain()
      #  nuevo_bloque = Bloque(len(blockchain.cadena), time.time(), datos_usuario, blockchain.cadena[-1].hash)
      #  blockchain.agregar_bloque(nuevo_bloque)
     #   logging.info("Bloque agregado a la blockchain exitosamente.")

       # logging.info("Guardando el bloque en la base de datos...")
      #  insertar_bloque(conexion, nuevo_bloque)
      #  logging.info("Bloque guardado en la base de datos exitosamente.")

       # logging.info("Manejando transacciones...")
       # insertar_transaccion(conexion, "Usuario1", "Usuario2", 100)
      #  transacciones = obtener_transacciones(conexion)
      #  logging.info(f"Transacciones almacenadas: {transacciones}")

      #  logging.info("Cerrando la conexión a la base de datos...")
      #  cerrar_conexion(conexion)
       # logging.info("Conexión a la base de datos cerrada.")

      #  logging.info("Iniciando el servidor...")
      #  iniciar_servidor()

  #  except Exception as e:
        # logging.error(f"Error durante la ejecución: {e}")

# if __name__ == "__main__":
  #  main()
