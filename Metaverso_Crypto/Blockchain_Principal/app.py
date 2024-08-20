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
        resultado = registrar_usuario(datos['username'], datos['password'])
        return jsonify({'status': 'success', 'data': resultado}), 201
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

# Ruta para verificar credenciales de usuario
@app.route('/verificar', methods=['POST'])
def verificar():
    datos = request.get_json()
    if verificar_credenciales(datos['username'], datos['password']):
        return jsonify({'status': 'success', 'message': 'Credenciales válidas'}), 200
    else:
        return jsonify({'status': 'error', 'message': 'Credenciales inválidas'}), 401

# Ruta para asignar recursos a un usuario
@app.route('/asignar_recursos', methods=['POST'])
def asignar_recursos():
    datos = request.get_json()
    usuario = RecursosUsuario(datos['porcentaje_cpu'], datos['porcentaje_ancho_banda'])
    recursos_comunitarios = {'cpu': 100, 'ancho_banda': 100}  # Ejemplo de recursos comunitarios
    recursos_asignados = asignar_recursos_a_usuario(usuario, recursos_comunitarios)
    return jsonify({'status': 'success', 'recursos_asignados': recursos_asignados}), 200

if __name__ == '__main__':
    app.run(debug=True)
