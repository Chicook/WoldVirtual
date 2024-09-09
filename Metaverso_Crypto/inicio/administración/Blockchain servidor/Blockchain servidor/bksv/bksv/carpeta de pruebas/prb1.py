from prb2 import app, registrar_usuario, verificar_credenciales
from prb3 import manejar_accion
from prb4 import get_blockchain, add_block, get_block
import prb5

# Puedes agregar más rutas y lógica aquí
@app.route('/registro', methods=['POST'])
def registro():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if username and password:
        registrar_usuario(username, password)
        return jsonify({"message": "Usuario registrado exitosamente"}), 201
    return jsonify({"error": "Datos incompletos"}), 400

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if verificar_credenciales(username, password):
        return jsonify({"message": "Inicio de sesión exitoso"}), 200
    return jsonify({"error": "Credenciales incorrectas"}), 401

@app.route('/accion', methods=['POST'])
def accion():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    accion = data.get('accion')
    if verificar_credenciales(username, password):
        manejar_accion(username, accion)
        return jsonify({"message": "Acción realizada"}), 200
    return jsonify({"error": "Credenciales incorrectas"}), 401

if __name__ == '__main__':
    app.run(debug=True)

# Puedes agregar más rutas y lógica aquí
@app.route('/registro', methods=['POST'])
def registro():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if username and password:
        registrar_usuario(username, password)
        return jsonify({"message": "Usuario registrado exitosamente"}), 201
    return jsonify({"error": "Datos incompletos"}), 400

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if verificar_credenciales(username, password):
        return jsonify({"message": "Inicio de sesión exitoso"}), 200
    return jsonify({"error": "Credenciales incorrectas"}), 401

if __name__ == '__main__':
    app.run(debug=True)
