# app.py

from usuarios import registrar_usuario, verificar_credenciales, manejar_accion
from recursos import RecursosUsuario, asignar_recursos_a_usuario, MonitoreoRecursos
from blockchain import Blockchain
from database import conectar_base_datos
from compresion import comprimir_y_guardar_datos, cargar_y_descomprimir_datos
from servidor import app, socketio
from almacenamiento import guardar_datos, cargar_datos  # Nuevo módulo de Almacenamiento

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
    guardar_datos(archivo_comprimido, "/workspaces/WoldVirtual.github.io/Metaverso_Crypto/inicio/Blockchain_Principal/Almacenamiento/almacenamiento.py")   # Se debe definir la ruta de almacenamiento

    # Cargar los datos desde el sistema de almacenamiento y descomprimirlos
    archivo_cargado = cargar_datos("/workspaces/WoldVirtual.github.io/Metaverso_Crypto/inicio/Blockchain_Principal/Almacenamiento/almacenamiento.py" archivo_comprimido)
    datos_descomprimidos = cargar_y_descomprimir_datos(archivo_cargado)

    # Procesar transacción en la blockchain
    blockchain = Blockchain()
    blockchain.agregar_bloque("transaccion_ejemplo")

    # Iniciar servidor
    socketio.run(app, debug=True)

if __name__ == "__main__":
    main()
