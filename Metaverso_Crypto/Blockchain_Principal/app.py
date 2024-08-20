from flask import Flask, request, jsonify
from usuarios import registrar_usuario, verificar_credenciales, manejar_accion
from recursos import RecursosUsuario, asignar_recursos_a_usuario, MonitoreoRecursos
from blockchain import Blockchain
from database import conectar_base_datos
from compresion import comprimir_y_guardar_datos, cargar_y_descomprimir_datos

app = Flask(__name__)

# Ruta para registrar un usuario
@app.route('/registrar', methods=['POST'])
def registrar():
    datos = request.get_json()
    try:
        resultado = registrar_usuario(datos)
        return jsonify({'status': 'success', 'data': resultado}), 201
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

# Aquí puedes añadir más rutas según sea necesario

if __name__ == '__main__':
    app.run(debug=True)

# (Dejar para mas adelante o para modificar código.)

# from flask import Flask, request, jsonify
# from usuarios import registrar_usuario, verificar_credenciales, manejar_accion
# from recursos import RecursosUsuario, asignar_recursos_a_usuario, MonitoreoRecursos
# from blockchain import Blockchain
# from database import conectar_base_datos
# from compresion import comprimir_y_guardar_datos, cargar_y_descomprimir_datos

# app = Flask(__name__)

# Definir las rutas y conectarlas con las funciones correspondientes

# if __name__ == 'main':
   # app.run(debug=True)
