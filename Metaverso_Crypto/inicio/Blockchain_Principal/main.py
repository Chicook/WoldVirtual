from usuarios import registrar_usuario, verificar_credenciales, manejar_accion
from recursos import RecursosUsuario, asignar_recursos_a_usuario, MonitoreoRecursos,
from blockchain import Blockchain
from database import conectar_base_datos
from almacenamiento import compress_files, decompress_file
from servidor import app, socketio

def main():
    # Inicializar recursos
    recursos_usuario = RecursosUsuario (50, 50)  # Ejemplo de inicialización con 50% de CPU y ancho de banda

    # Conectar a la base de datos
    db = conectar_base_datos()

    # Crear un nuevo usuario
    registrar_usuario("nombre", "contraseña")

    # Ejecutar compresión de datos
    datos_usuario = ["file1.txt", "file2.txt"]
    compress_files(datos_usuario, "datos_comprimidos.tar.gz")

    # Procesar transacción en la blockchain
    blockchain = Blockchain()
    blockchain.agregar_bloque("transaccion_ejemplo")
    print("Cadena válida:", blockchain.validar_cadena())

    # Iniciar servidor
    socketio.run(app, debug=True)

if __name__ == "__main__":
    main()
