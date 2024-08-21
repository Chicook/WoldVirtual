from usuarios import registrar_usuario, verificar_credenciales, manejar_accion
from recursos import RecursosUsuario, MonitoreoRecursos
from blockchain import Blockchain
from database import conectar_base_datos
from compresion import comprimir_y_guardar_datos, cargar_y_descomprimir_datos
from servidor import app, socketio,
from almacenamiento  import compress_files, decompress_file,

def main():
    # Inicializar recursos
    recursos_comunitarios = {'cpu': 100, 'ancho_banda': 1000}  # Valores de ejemplo
    usuario1 = RecursosUsuario(50, 50)  # Usuario usando 50% de recursos disponibles
    print("Recursos de usuario inicializados.")

    # Asignar recursos al usuario
    recursos_asignados = RecursosUsuario.asignar_recursos_a_usuario(usuario1, recursos_comunitarios)
    print(f"Recursos asignados: CPU: {recursos_asignados['cpu']}%, Ancho de banda: {recursos_asignados['ancho_banda']}kbps")

    # Monitoreo de recursos
    monitor = MonitoreoRecursos()
    monitor.actualizar_recursos("usuario1", 30, 500)
    print("Estado de recursos monitoreado:", monitor.obtener_informacion())

    # Conectar a la base de datos
    conectar_base_datos()

    # Crear un nuevo usuario
    try:
        registrar_usuario("nombre_usuario", "contraseña_segura")
    except ValueError as e:
        print(e)

    # Verificar credenciales del usuario
    if verificar_credenciales("nombre_usuario", "contraseña_segura"):
        print("Acceso concedido.")
        manejar_accion("nombre_usuario", "explorar")
    else:
        print("Credenciales incorrectas.")

    # Compresión y descompresión de datos
    datos = {"clave": "valor", "otro": [1, 2, 3]}
    comprimir_y_guardar_datos(datos, 'datos_comprimidos.gz')
    datos_cargados = cargar_y_descomprimir_datos('datos_comprimidos.gz')
    print("Datos descomprimidos:", datos_cargados)

    # Compresión y descompresión de archivos
    files_to_compress = ['archivo1.txt', 'archivo2.txt']  # Archivos de ejemplo
    compress_files(files_to_compress, 'archivos_comprimidos.tar.gz')
    decompress_file('archivos_comprimidos.tar.gz')

    # Iniciar el servidor Flask
    socketio.run(app, debug=True)

if __name__ == '__main__':
     main()
