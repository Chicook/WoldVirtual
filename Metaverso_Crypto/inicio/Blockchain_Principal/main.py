from flask import Flask, redirect, url_for
from usuarios import registrar_usuario, generar_wallet, blockchain, log_action
from recursos import RecursosUsuario
# from database import conectar_base_datos  # Comentado para futuras implementaciones
from compresion import comprimir_y_guardar_datos
from servidor import app, socketio
from administración  import Bksvmain , 

# Cantidad total de tokens WCV
TOTAL_WCV = 30000000.000

def inicializar_recursos():
    recursos = RecursosUsuario(50, 50)  # Ejemplo de inicialización con 50% de CPU y ancho de banda
    log_action("Recursos inicializados: CPU=50%, Ancho de banda=50%")
    return recursos

# Función de conexión a la base de datos comentada para futuras implementaciones
# def conectar_bd():
#     db = conectar_base_datos()
#     log_action("Conexión a la base de datos establecida")
#     return db

def crear_usuario(nombre, contraseña):
    registrar_usuario(nombre, contraseña)
    log_action(f"Usuario creado: {nombre}")

def comprimir_datos(datos, archivo):
    comprimir_y_guardar_datos(datos, archivo)
    log_action(f"Datos comprimidos y guardados en {archivo}")

def procesar_transaccion(transaccion):
    blockchain.agregar_bloque(transaccion)
    log_action(f"Transacción procesada: {transaccion}")

def iniciar_servidor():
    log_action("Servidor iniciado")
    socketio.run(app, debug=True)

@app.route('/inicio')
def inicio():
    log_action("Sección de inicio cargada")
    return redirect(url_for('index'))

def main():
    """
    Función principal para inicializar recursos, conectar a la base de datos,
    registrar un usuario, comprimir y almacenar datos, procesar transacciones
    en la blockchain e iniciar el servidor.
    """
    recursos_usuario = inicializar_recursos()
    # db = conectar_bd()  # Comentado para futuras implementaciones

    # Confirmar que todos los módulos están funcionando correctamente
    blockchain.confirmar_conexion_modulos(['servidor', 'usuarios', 'recursos', 'compresion'])

    crear_usuario("nombre", "contraseña")

    datos_usuario = {"nombre": "nombre", "datos": "datos_ejemplo"}
    archivo_comprimido = "datos_comprimidos.gz"
    comprimir_datos(datos_usuario, archivo_comprimido)

    procesar_transaccion("transaccion_ejemplo")

    iniciar_servidor()

if __name__ == "__main__":
    main()
    
