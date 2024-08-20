from flask import Flask, request, jsonify
from usuarios import registrar_usuario, verificar_credenciales, manejar_accion
from recursos import RecursosUsuario, asignar_recursos_a_usuario, MonitoreoRecursos
from blockchain import Blockchain
from database import conectar_base_datos
from compresion import comprimir_y_guardar_datos, cargar_y_descomprimir_datos

app = Flask(__name__)

# Definir las rutas y conectarlas con las funciones correspondientes

if __name__ == '__main__':
    app.run(debug=True)
