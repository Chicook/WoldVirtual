from usuarios import registrar_usuario, verificar_credenciales, manejar_accion
from recursos import RecursosUsuario, MonitoreoRecursos
from blockchain import Blockchain
from database import conectar_base_datos
from compresion import comprimir_y_guardar_datos, cargar_y_descomprimir_datos
from servidor import app, socketio
import tarfile

# Definir la ruta de almacenamiento
storage_path = '/workspaces/WoldVirtual.github.io/Metaverso_Crypto/inicio/Blockchain_Principal/Almacenamiento'

# Función para comprimir archivos
def compress_files(files, output_filename):
    with tarfile.open(os.path.join(storage_path, output_filename), 'w:gz') as tar:
        for file in files:
            tar.add(file, arcname=os.path.basename(file))
    print(f'Archivos comprimidos en {output_filename}')

# Función para descomprimir archivos
def decompress_file(input_filename):
    with tarfile.open(os.path.join(storage_path, input_filename), 'r:gz') as tar:
        tar.extractall(path=storage_path)
    print(f'Archivos descomprimidos en {storage_path}')

# Ejemplo de uso
files_to_compress = ['/ruta/de/archivo1', '/ruta/de/archivo2']
compress_files(files_to_compress, 'archivo_comprimido.tar.gz')
decompress_file('archivo_comprimido.tar.gz')
                                        
def main():
    # Inicializar recursos
    recursos_usuario = RecursosUsuario(50, 50)  # Ejemplo de inicialización con 50% de CPU y ancho de banda
    print("Recursos de usuario inicializados.")

    # Conectar a la base de datos
    db = conectar_base_datos()
    print("Conexión a la base de datos establecida.")

    # Crear un nuevo usuario
    try:
        registrar_usuario("nombre", "contraseña")
        print("Usuario registrado con éxito.")
    except ValueError as e:
        print(e)

    # Verificar credenciales del usuario
    if verificar_credenciales("nombre", "contraseña"):
        print("Credenciales verificadas con éxito.")
    else:
        print("Credenciales incorrectas.")

    # Ejecutar compresión de datos
    datos_usuario = {"nombre": "nombre", "datos": "datos_ejemplo"}
    comprimir_y_guardar_datos(datos_usuario, "datos_comprimidos.gz")
    print("Datos comprimidos y guardados.")

    # Cargar y descomprimir datos
    datos_cargados = cargar_y_descomprimir_datos("datos_comprimidos.gz")
    print("Datos cargados y descomprimidos:", datos_cargados)

    # Procesar transacción en la blockchain
    blockchain = Blockchain()
    blockchain.agregar_bloque("transaccion_ejemplo")
    print("Transacción añadida a la blockchain.")

    # Iniciar servidor
    print("Iniciando servidor web...")
    socketio.run(app, debug=True)

if __name__ == "__main__":
    main()
