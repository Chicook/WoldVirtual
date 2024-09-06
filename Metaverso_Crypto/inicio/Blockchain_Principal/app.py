# modulo app #

from flask import Flask, render_template_string
from flask_socketio import SocketIO
from blockchain import Blockchain
from usuarios import registrar_usuario
from recursos import RecursosUsuario, MonitoreoRecursos
from database import conectar_base_datos, insertar_bloque, insertar_transaccion
from compresion import comprimir_y_guardar_datos, cargar_y_descomprimir_datos
from almacenamiento import listar_archivos, eliminar_archivo
import time

# Inicializar la aplicación Flask y SocketIO
app = Flask(__name__)
socketio = SocketIO(app)

# Inicializar la cadena de bloques
blockchain = Blockchain()

# Plantilla HTML para la interfaz web
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Metaverso Crypto 3D</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f9f9f9; }
        .header { background-color: #4CAF50; color: white; padding: 15px 0; text-align: center; }
        .nav { display: flex; justify-content: center; background-color: #333; }
        .nav a { color: white; padding: 14px 20px; text-decoration: none; text-align: center; }
        .nav a:hover { background-color: #ddd; color: black; }
        .container { margin: 20px auto; padding: 20px; max-width: 800px; background-color: #fff; border-radius: 8px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); }
        .section { margin-bottom: 20px; }
        h1, h2 { margin-top: 0; }
        .button { background-color: #4CAF50; border: none; color: white; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; border-radius: 4px; }
        .button:hover { background-color: #45a049; }
    </style>
</head>
<body>
    <div class="header"><h1>Metaverso Crypto 3D</h1></div>
    <div class="nav">
        <a href="#home">Inicio</a>
        <a href="#usuarios">Usuarios</a>
        <a href="#recursos">Recursos</a>
        <a href="#blockchain">Blockchain</a>
        <a href="#database">Base de Datos</a>
        <a href="#compresion">Compresión</a>
        <a href="#servidor">Servidor</a>
    </div>
    <div class="container">
        <div id="home" class="section">
            <h2>Metaverso Crypto 3D descentralizado</h2>
            <p>Próximamente en esta página principal, se darán más detalles sobre el proyecto...</p>
            <button class="button">Más Información</button>
        </div>
    </div>
    <script src="https://cdn.socket.io/4.0.0/socket.io.min.js"></script>
    <script>
        const socket = io();
        document.getElementById('sendButton').addEventListener('click', () => {
            const audioData = document.getElementById('audioInput').value;
            socket.emit('audio_stream', audioData);
        });
        socket.on('audio_stream', (data) => {
            console.log('Received audio data:', data);
        });
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    """
    Renderiza la plantilla HTML para la página principal.
    """
    return render_template_string(html_template)

# Función para inicializar recursos
def inicializar_recursos(cpu=50, ancho_banda=50):
    """
    Inicializa y asigna los recursos a un usuario.
    """
    recursos_usuario = RecursosUsuario(cpu, ancho_banda)
    recursos_asignados = recursos_usuario.asignar_recursos({
        'cpu': 100,
        'ancho_banda': 100
    })
    print(f"Recursos asignados: {recursos_asignados}")
    return recursos_usuario

# Función para conectar a la base de datos
def conectar_bd():
    """
    Establece conexión con la base de datos.
    """
    return conectar_base_datos()

# Función para crear un nuevo usuario
def crear_usuario(nombre, contraseña):
    """
    Registra un nuevo usuario.
    """
    registrar_usuario(nombre, contraseña)
    print(f"Usuario {nombre} registrado exitosamente.")

# Función para comprimir los datos del usuario
def comprimir_datos(datos, archivo):
    """
    Comprime los datos del usuario y los guarda en un archivo.
    """
    comprimir_y_guardar_datos(datos, archivo)
    print(f"Datos comprimidos y guardados en {archivo}.")

# Función para descomprimir datos
def descomprimir_datos(archivo):
    """
    Carga y descomprime los datos de un archivo .gz.
    """
    datos = cargar_y_descomprimir_datos(archivo)
    print(f"Datos descomprimidos: {datos}")
    return datos

# Función para procesar transacción en la blockchain
def procesar_transaccion(blockchain, datos):
    """
    Procesa una transacción y agrega un bloque a la blockchain.
    """
    nuevo_bloque = blockchain.agregar_bloque(datos)
    print(f"Bloque añadido: {nuevo_bloque}")

# Función para gestionar almacenamiento de bloques y transacciones en la base de datos
def almacenar_bloque_transaccion(db_conn, bloque, remitente, destinatario, cantidad):
    """
    Almacena un bloque y una transacción en la base de datos.
    """
    insertar_bloque(db_conn, bloque)
    insertar_transaccion(db_conn, remitente, destinatario, cantidad)
    print(f"Bloque y transacción almacenados en la base de datos.")

# Función para iniciar el servidor
def iniciar_servidor():
    """
    Inicia el servidor con SocketIO y Flask.
    """
    socketio.run(app, debug=True)

def main():
    """
    Función principal para inicializar recursos, conectar a la base de datos,
    registrar un usuario, comprimir y almacenar datos, procesar transacciones
    en la blockchain, y ejecutar el servidor.
    """
    try:
        # Inicializar recursos
        recursos_usuario = inicializar_recursos()

        # Conectar a la base de datos
        db_conn = conectar_bd()

        # Crear un nuevo usuario
        crear_usuario("nombre_usuario", "contraseña_secreta")

        # Procesar compresión de datos
        datos_usuario = {"nombre": "nombre_usuario", "datos": "información_ejemplo"}
        archivo_comprimido = "datos_comprimidos.gz"
        comprimir_datos(datos_usuario, archivo_comprimido)

        # Descomprimir datos
        datos_descomprimidos = descomprimir_datos(archivo_comprimido)

        # Procesar transacción en la blockchain
        procesar_transaccion(blockchain, datos_descomprimidos)

        # Almacenar bloque y transacción en la base de datos
        almacenar_bloque_transaccion(db_conn, blockchain.cadena[-1], "Usuario1", "Usuario2", 100)

        # Iniciar servidor
        iniciar_servidor()

    except Exception as e:
        print(f"Error en la ejecución: {e}")

if __name__ == '__main__':
    main()

# modulo app #

# from flask import Flask, render_template_string
# from flask_socketio import SocketIO
# from blockchain import Blockchain

# Inicializar la aplicación Flask y SocketIO
# app = Flask(__name__)
# socketio = SocketIO(app)

# Inicializar la cadena de bloques
# blockchain = Blockchain()

# Plantilla HTML para la interfaz web
# html_template = """
# <!DOCTYPE html>
# <html lang="en">
# <head>
   # <meta charset="UTF-8">
   # <meta name="viewport" content="width=device-width, initial-scale=1.0">
   # <title>Metaverso Crypto 3D</title>
   # <style>
       # body { font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f9f9f9; }
       # .header { background-color: #4CAF50; color: white; padding: 15px 0; text-align: center; }
      #  .nav { display: flex; justify-content: center; background-color: #333; }
     #   .nav a { color: white; padding: 14px 20px; text-decoration: none; text-align: center; }
      #  .nav a:hover { background-color: #ddd; color: black; }
     #   .container { margin: 20px auto; padding: 20px; max-width: 800px; background-color: #fff; border-radius: 8px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); }
     #   .section { margin-bottom: 20px; }
      #  h1, h2 { margin-top: 0; }
      #  .button { background-color: #4CAF50; border: none; color: white; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; border-radius: 4px; }
      #  .button:hover { background-color: #45a049; }
   # </style>
# </head>
# <body>
  #  <div class="header"><h1>Metaverso Crypto 3D</h1></div>
 #   <div class="nav">
      #  <a href="#home">Inicio</a>
       # <a href="#usuarios">Usuarios</a>
      #  <a href="#recursos">Recursos</a>
      #  <a href="#blockchain">Blockchain</a>
      #  <a href="#database">Base de Datos</a>
      #  <a href="#compresion">Compresión</a>
      #  <a href="#servidor">Servidor</a>
  #  </div>
   # <div class="container">
       # <div id="home" class="section">
          #  <h2>Metaverso Crypto 3D descentralizado</h2>
          #  <p>Próximamente en esta página principal, se darán más detalles sobre el proyecto...</p>
          #  <button class="button">Más Información</button>
      #  </div>
     #   <!-- Secciones adicionales aquí -->
  #  </div>
  #  <script src="https://cdn.socket.io/4.0.0/socket.io.min.js"></script>
   # <script>
      #  const socket = io();
      #  document.getElementById('sendButton').addEventListener('click', () => {
         #   const audioData = document.getElementById('audioInput').value;
          #  socket.emit('audio_stream', audioData);
    #    });
      #  socket.on('audio_stream', (data) => {
          #  console.log('Received audio data:', data);
      #  });
   # </script>
# </body>
# </html>
# """

# @app.route('/')
# def index():
   # """
  #  Renderiza la plantilla HTML para la página principal.
  #  """
  #  return render_template_string(html_template)

# @socketio.on('audio_stream')
# def handle_audio(data):
#     """
#     Maneja el evento de transmisión de audio.
#     """
#     socketio.emit('audio_stream', data)

# if __name__ == '__main__':
    # Confirmar la conexión de los módulos
   # blockchain.confirmar_conexion_modulos(['usuarios', 'recursos', 'database', 'compresion', 'servidor'])
   # blockchain.imprimir_cadena()
  #  socketio.run(app, debug=True)

# modulo app #

# from usuarios import registrar_usuario
# from recursos import RecursosUsuario
# from blockchain import Blockchain
# from database import conectar_base_datos
# from compresion import comprimir_y_guardar_datos, cargar_y_descomprimir_datos
# from servidor import app, socketio

# def inicializar_recursos(cpu, ancho_banda):
   # return RecursosUsuario(cpu, ancho_banda)

# def conectar_bd():
   # return conectar_base_datos()

# def crear_usuario(nombre, contraseña):
    # registrar_usuario(nombre, contraseña)

# def comprimir_datos(datos, archivo):
    # comprimir_y_guardar_datos(datos, archivo)

# def descomprimir_datos(archivo):
   # return cargar_y_descomprimir_datos(archivo)

# def procesar_transaccion(blockchain, transaccion):
   # blockchain.agregar_bloque(transaccion)

# def iniciar_servidor():
   # socketio.run(app, debug=True)

# def main():
   # """
   # Función principal para inicializar recursos, conectar a la base de datos,
   # registrar un usuario, comprimir y almacenar datos, procesar transacciones
   # en la blockchain e iniciar el servidor.
   # """
   # recursos_usuario = inicializar_recursos(50, 50)
   # db = conectar_bd()
   # crear_usuario("nombre", "contraseña")

   # datos_usuario = {"nombre": "nombre", "datos": "datos_ejemplo"}
   # archivo_comprimido = "datos_comprimidos.gz"
    # comprimir_datos(datos_usuario, archivo_comprimido)

    # datos_descomprimidos = descomprimir_datos(archivo_comprimido)

   # blockchain = Blockchain()
  #  procesar_transaccion(blockchain, "transaccion_ejemplo")

   # iniciar_servidor()

# if __name__ == "__main__":
   # main()

# app.py
# from usuarios import registrar_usuario, verificar_credenciales, manejar_accion
# from recursos import RecursosUsuario, MonitoreoRecursos
# from blockchain import Blockchain
# from database import conectar_base_datos
# from compresion import comprimir_y_guardar_datos, cargar_y_descomprimir_datos
# from servidor import app, socketio
# from almacenamiento import compress_files, decompress_file

# def main():
   # """
   # Función principal para inicializar recursos, conectar a la base de datos,
    # registrar un usuario, comprimir y almacenar datos, procesar transacciones
   #  en la blockchain e iniciar el servidor.
  #   """
    # Inicializar recursos
   #  recursos_usuario = RecursosUsuario(50, 50)  # Ejemplo de inicialización con 50% de CPU y ancho de banda

    # Conectar a la base de datos
   #  db = conectar_base_datos()

    # Crear un nuevo usuario
    # registrar_usuario("nombre", "contraseña")

    # Ejecutar compresión de datos
   #  datos_usuario = {"nombre": "nombre", "datos": "datos_ejemplo"}
   #  archivo_comprimido = "datos_comprimidos.gz"
   #  comprimir_y_guardar_datos(datos_usuario, archivo_comprimido)

    # Almacenar los datos comprimidos en el sistema de almacenamiento
    # compress_files(["datos_comprimidos.gz"], "datos_comprimidos.tar.gz")

    # Cargar los datos desde el sistema de almacenamiento y descomprimirlos
    # decompress_file("datos_comprimidos.tar.gz")
    datos_descomprimidos = cargar_y_descomprimir_datos("datos_comprimidos.gz")

    # Procesar transacción en la blockchain
   #  blockchain = Blockchain()
   #  blockchain.agregar_bloque("transaccion_ejemplo")

    # Iniciar servidor
    # socketio.run(app, debug=True)

# if __name__ == "__main__":
   #  main()
