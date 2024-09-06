# main.py

from usuarios import registrar_usuario
from recursos import RecursosUsuario
from database import conectar_base_datos, insertar_bloque, obtener_transacciones, insertar_transaccion, cerrar_conexion
from compresion import comprimir_y_guardar_datos, cargar_y_descomprimir_datos
from almacenamiento import listar_archivos
from servidor import app, socketio
from blockchain import Blockchain, Bloque
import time

def inicializar_recursos(cpu: int = 50, ancho_banda: int = 50):
    """
    Inicializa los recursos asignados a un usuario y devuelve los recursos asignados.
    """
    recursos_usuario = RecursosUsuario(cpu, ancho_banda)
    recursos_comunitarios = {'cpu': 100, 'ancho_banda': 100}
    recursos_asignados = recursos_usuario.asignar_recursos(recursos_comunitarios)
    return recursos_asignados

def conectar_bd():
    """
    Conecta a la base de datos y devuelve la conexión.
    """
    return conectar_base_datos()

def crear_usuario(nombre, contraseña):
    """
    Registra un nuevo usuario.
    """
    registrar_usuario(nombre, contraseña)

def comprimir_datos(datos, archivo):
    """
    Comprime y guarda los datos en un archivo.
    """
    comprimir_y_guardar_datos(datos, archivo)

def procesar_transaccion(blockchain, transaccion):
    """
    Procesa una transacción en la blockchain.
    """
    blockchain.agregar_bloque(transaccion)

def iniciar_servidor():
    """
    Inicia el servidor Flask con SocketIO.
    """
    socketio.run(app, debug=True)

def main():
    """
    Función principal para inicializar recursos, conectar a la base de datos,
    registrar un usuario, comprimir y almacenar datos, procesar transacciones
    en la blockchain e iniciar el servidor.
    """
    try:
        # Inicializar recursos
        recursos_asignados = inicializar_recursos()

        # Conectar a la base de datos
        conexion = conectar_bd()

        # Registrar un nuevo usuario
        crear_usuario("nombre", "contraseña")

        # Proceso de compresión y almacenamiento
        datos_usuario = {"nombre": "nombre", "datos": "datos_ejemplo"}
        archivo_comprimido = "datos_comprimidos.gz"
        comprimir_datos(datos_usuario, archivo_comprimido)
        
        # Listar archivos en el directorio actual
        listar_archivos('.')

        # Cargar y descomprimir datos
        datos_descomprimidos = cargar_y_descomprimir_datos(archivo_comprimido)
        
        # Inicializar blockchain y agregar bloque
        blockchain = Blockchain()
        nuevo_bloque = Bloque(len(blockchain.cadena), time.time(), datos_usuario, blockchain.cadena[-1].hash)
        blockchain.agregar_bloque(nuevo_bloque)

        # Guardar el bloque en la base de datos
        insertar_bloque(conexion, nuevo_bloque)

        # Manejo de transacciones
        insertar_transaccion(conexion, "Usuario1", "Usuario2", 100)
        transacciones = obtener_transacciones(conexion)
        print(f"Transacciones almacenadas: {transacciones}")

        # Cerrar la conexión a la base de datos
        cerrar_conexion(conexion)

        # Iniciar el servidor
        iniciar_servidor()

    except Exception as e:
        print(f"Error durante la ejecución: {e}")

if __name__ == "__main__":
    main()

# main.py

# from usuarios import registrar_usuario
# from recursos import RecursosUsuario
# from database import conectar_base_datos
# from compresion import comprimir_y_guardar_datos
# from servidor import app, socketio
# from blockchain import Blockchain

# def inicializar_recursos():
   # return RecursosUsuario(50, 50)  # Ejemplo de inicialización con 50% de CPU y ancho de banda

# def conectar_bd():
   # return conectar_base_datos()

# def crear_usuario(nombre, contraseña):
   # registrar_usuario(nombre, contraseña)

# def comprimir_datos(datos, archivo):
   # comprimir_y_guardar_datos(datos, archivo)

# def  procesar_transaccion(blockchain, transaccion):
   # blockchain.agregar_bloque(transaccion)

# def iniciar_servidor():
   # socketio.run(app, debug=True)

# def main():
  #  """
  #  Función principal para inicializar recursos, conectar a la base de datos,
  #  registrar un usuario, comprimir y almacenar datos, procesar transacciones
  #  en la blockchain e iniciar el servidor.
 #   """
   # recursos_usuario = inicializar_recursos()
  #  db = conectar_bd()
  #  crear_usuario("nombre", "contraseña")

   # datos_usuario = {"nombre": "nombre", "datos": "datos_ejemplo"}
  #  archivo_comprimido = "datos_comprimidos.gz"
   # comprimir_datos(datos_usuario, archivo_comprimido)

  #  blockchain = Blockchain()
  #  procesar_transaccion(blockchain, "transaccion_ejemplo")

  #  iniciar_servidor()

# if __name__ == "__main__":
   # main()

# main.py

# from usuarios import registrar_usuario, verificar_credenciales, manejar_accion
# from recursos import RecursosUsuario, MonitoreoRecursos
# from blockchain import Blockchain
# from database import conectar_base_datos
# from compresion import comprimir_y_guardar_datos, cargar_y_descomprimir_datos
# from servidor import app, socketio
# from almacenamiento import compress_files, decompress_file

# def main():

   #  if __name__ == "__main__":
          
        # blockchain = Blockchain()  # Crear una instancia de Blockchain
        # blockchain.agregar_bloque("Primer Bloque Después del Génesis")
        # blockchain.agregar_bloque("Segundo Bloque Después del Génesis")
        # blockchain.imprimir_cadena()
    
    # print("Cadena válida:", blockchain.validar_cadena())
    
  #  """
   # Función principal para inicializar recursos, conectar a la base de datos,
    # registrar un usuario, comprimir y almacenar datos, procesar transacciones
   # en la blockchain e iniciar el servidor.
   # """
    # Inicializar recursos
   # recursos_usuario = RecursosUsuario(50, 50)  # Ejemplo de inicialización con 50% de CPU y ancho de banda

    # Conectar a la base de datos
  #  db = conectar_base_datos()

    # Crear un nuevo usuario
    # registrar_usuario("nombre", "contraseña")

    # Ejecutar compresión de datos
  #  datos_usuario = {"nombre": "nombre", "datos": "datos_ejemplo"}
   # archivo_comprimido = "datos_comprimidos.gz"
    # comprimir_y_guardar_datos(datos_usuario, archivo_comprimido)

    # Almacenar los datos comprimidos en el sistema de almacenamiento
   #  compress_files([archivo_comprimido], "datos_comprimidos.tar.gz")

    # Verificar que el archivo comprimido existe antes de descomprimirlo
   # if os.path.isfile("/workspaces/WoldVirtual.github.io/Metaverso_Crypto/inicio/Blockchain_Principal/Almacenamiento/datos_comprimidos.tar.gz"):
        # Cargar los datos desde el sistema de almacenamiento y descomprimirlos
       # decompress_file("datos_comprimidos.tar.gz")
       # datos_descomprimidos = cargar_y_descomprimir_datos(archivo_comprimido)
   # else:
        # print("El archivo datos_comprimidos.tar.gz no existe en la ruta especificada.")

    # Procesar transacción en la blockchain
   # blockchain = Blockchain()
    # blockchain.agregar_bloque("transaccion_ejemplo")

    # Iniciar servidor
   # socketio.run(app, debug=True)

# if __name__ == "__main__": #
#   main() #
