from usuarios import registrar_usuario, verificar_credenciales, manejar_accion
from recursos import RecursosUsuario, MonitoreoRecursos
from blockchain import Blockchain
from database import conectar_base_datos
from compresion import comprimir_y_guardar_datos, cargar_y_descomprimir_datos
from servidor import app, socketio
                                       
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
