# main.py

from usuarios import registrar_usuario, verificar_credenciales, manejar_accion
from recursos import RecursosUsuario, MonitoreoRecursos
from blockchain import Blockchain
from database import conectar_base_datos
from compresion import comprimir_y_guardar_datos, cargar_y_descomprimir_datos
from servidor import app, socketio
# from almacenamiento import compress_files, decompress_file

def main():
    """
    Función principal para inicializar recursos, conectar a la base de datos,
    registrar un usuario, comprimir y almacenar datos, procesar transacciones
    en la blockchain e iniciar el servidor.
    """
    # Inicializar recursos
    recursos_usuario = RecursosUsuario(50, 50)  # Ejemplo de inicialización con 50% de CPU y ancho de banda

    # Conectar a la base de datos
    db = conectar_base_datos()

    # Crear un nuevo usuario
    registrar_usuario("nombre", "contraseña")

    # Ejecutar compresión de datos
    datos_usuario = {"nombre": "nombre", "datos": "datos_ejemplo"}
    archivo_comprimido = "datos_comprimidos.gz"
    comprimir_y_guardar_datos(datos_usuario, archivo_comprimido)

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
    blockchain = Blockchain()
    blockchain.agregar_bloque("transaccion_ejemplo")

    # Iniciar servidor
    socketio.run(app, debug=True)

if __name__ == "__main__":
    main()
