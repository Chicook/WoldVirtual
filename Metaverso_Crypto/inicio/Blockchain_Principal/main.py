import hashlib
import json
import os
import datetime
import time
import random
from flask import Flask, jsonify, request, redirect, url_for
from usuarios import registrar_usuario, generar_wallet, blockchain, log_action
from recursos import RecursosUsuario
# from database import conectar_base_datos  # Comentado para futuras implementaciones
from compresion import comprimir_y_guardar_datos
from servidor import app, socketio
from administración/Blockchain Servidor import Bksvmain

# Cantidad total de tokens WCV
TOTAL_WCV = 30000000.000

def inicializar_recursos():
    try:
        recursos = RecursosUsuario(50, 50)  # Ejemplo de inicialización con 50% de CPU y ancho de banda
        log_action("Recursos inicializados: CPU=50%, Ancho de banda=50%")
        return recursos
    except Exception as e:
        log_action(f"Error al inicializar recursos: {e}")
        raise

# Función de conexión a la base de datos comentada para futuras implementaciones
# def conectar_bd():
#     try:
#         db = conectar_base_datos()
#         log_action("Conexión a la base de datos establecida")
#         return db
#     except Exception as e:
#         log_action(f"Error al conectar a la base de datos: {e}")
#         raise

def crear_usuario(nombre, contraseña):
    try:
        registrar_usuario(nombre, contraseña)
        log_action(f"Usuario creado: {nombre}")
    except Exception as e:
        log_action(f"Error al crear usuario: {e}")
        raise

def comprimir_datos(datos, archivo):
    try:
        comprimir_y_guardar_datos(datos, archivo)
        log_action(f"Datos comprimidos y guardados en {archivo}")
    except Exception as e:
        log_action(f"Error al comprimir datos: {e}")
        raise

def procesar_transaccion(transaccion):
    try:
        blockchain.agregar_bloque(transaccion)
        log_action(f"Transacción procesada: {transaccion}")
    except Exception as e:
        log_action(f"Error al procesar transacción: {e}")
        raise

def iniciar_servidor():
    try:
        log_action("Servidor iniciado")
        socketio.run(app, debug=True)
    except Exception as e:
        log_action(f"Error al iniciar el servidor: {e}")
        raise

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
    try:
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
    except Exception as e:
        log_action(f"Error en la ejecución principal: {e}")
        raise

if __name__ == "__main__":
    main()
