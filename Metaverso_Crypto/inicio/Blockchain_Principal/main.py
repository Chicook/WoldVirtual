# main.py

from w3D       import w3D
from usuarios import registrar_usuario
from recursos import RecursosUsuario
from database import conectar_base_datos
from compresion import comprimir_y_guardar_datos
from servidor import app, socketio
from blockchain import Blockchain

def inicializar_recursos():
    return RecursosUsuario(50, 50)  # Ejemplo de inicialización con 50% de CPU y ancho de banda

def conectar_bd():
    return conectar_base_datos()

def crear_usuario(nombre, contraseña):
    registrar_usuario(nombre, contraseña)

def comprimir_datos(datos, archivo):
    comprimir_y_guardar_datos(datos, archivo)

def procesar_transaccion(blockchain, transaccion):
    blockchain.agregar_bloque(transaccion)

def iniciar_servidor():
    socketio.run(app, debug=True)

def actualizar_recursos(recursos_usuario, nuevos_datos):
    """
    Actualiza los recursos inicializados con nuevos datos.

    Args:
        recursos_usuario (RecursosUsuario): Instancia de recursos del usuario.
        nuevos_datos (dict): Nuevos datos para actualizar los recursos.
    """
    if not isinstance(nuevos_datos, dict):
        print("Error: Los nuevos datos deben ser un diccionario.")
        return

    if 'porcentaje_cpu' in nuevos_datos:
        recursos_usuario.porcentaje_cpu = nuevos_datos['porcentaje_cpu']
    if 'porcentaje_ancho_banda' in nuevos_datos:
        recursos_usuario.porcentaje_ancho_banda = nuevos_datos['porcentaje_ancho_banda']

    print("Recursos actualizados:", recursos_usuario)

def main():
    """
    Función principal para inicializar recursos, conectar a la base de datos,
    registrar un usuario, comprimir y almacenar datos, procesar transacciones
    en la blockchain e iniciar el servidor.
    """
    recursos_usuario = inicializar_recursos()
    db = conectar_bd()
    crear_usuario("nombre", "contraseña")

    datos_usuario = {"nombre": "nombre", "datos": "datos_ejemplo"}
    archivo_comprimido = "datos_comprimidos.gz"
    comprimir_datos(datos_usuario, archivo_comprimido)

    blockchain = Blockchain()
    procesar_transaccion(blockchain, "transaccion_ejemplo")

    nuevos_datos = {"porcentaje_cpu": 60, "porcentaje_ancho_banda": 70}
    actualizar_recursos(recursos_usuario, nuevos_datos)

    iniciar_servidor()

if __name__ == "__main__":
    main()
