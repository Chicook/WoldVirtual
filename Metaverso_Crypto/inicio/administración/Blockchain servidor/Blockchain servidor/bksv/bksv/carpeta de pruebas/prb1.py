from flask import Flask, jsonify, request, render_template_string
import prb2
import prb3
import prb4
import prb5

app = Flask(__name__)

@app.route('/registro', methods=['POST'])
def registro():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    wallet = data.get('wallet')
    if username and password and wallet:
        prb2.registrar_usuario(username, password, wallet)
        prb4.registrar_actividad_css(f"Usuario registrado: {username}")
        prb5.guardar_en_json()
        return jsonify({"message": "Usuario registrado exitosamente"}), 201
    return jsonify({"error": "Datos incompletos"}), 400

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if prb2.verificar_credenciales(username, password):
        prb4.registrar_actividad_css(f"Inicio de sesión: {username}")
        return jsonify({"message": "Inicio de sesión exitoso"}), 200
    return jsonify({"error": "Credenciales incorrectas"}), 401

@app.route('/accion', methods=['POST'])
def accion():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    accion = data.get('accion')
    if prb2.verificar_credenciales(username, password):
        prb3.manejar_accion(username, accion)
        prb4.registrar_actividad_css(f"Acción realizada: {accion} por {username}")
        return jsonify({"message": "Acción realizada"}), 200
    return jsonify({"error": "Credenciales incorrectas"}), 401

@app.route('/blockchain', methods=['GET'])
def blockchain_route():
    return jsonify({'blockchain': prb5.get_blockchain()})

@app.route('/add_block', methods=['POST'])
def add_block_route():
    return prb4.add_block()

@app.route('/block/<int:block_index>', methods=['GET'])
def block_route(block_index):
    return prb4.get_block(block_index)

@app.route('/crear_wallet', methods=['POST'])
def crear_wallet_route():
    wallet = prb5.crear_wallet()
    prb4.registrar_actividad_css(f"Wallet creada: {wallet['id']}")
    prb5.guardar_en_json()
    return jsonify({"message": "Wallet creada", "wallet": wallet}), 201

@app.route('/validar_registro', methods=['POST'])
def validar_registro_route():
    data = request.get_json()
    forks = data.get('forks')
    valor = prb5.validar_registro(forks)
    prb4.registrar_actividad_css(f"Registro validado: forks={forks}, valor={valor}")
    prb5.guardar_en_json()
    return jsonify({"message": "Registro validado", "valor": valor}), 200

@app.route('/')
def index():
    html_content = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Ejemplo de Aplicación</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <h1>Ejemplo de Aplicación</h1>
        <div id="content">
            <h2>Registro de Usuario</h2>
            <button onclick="generarWallet()">Generar Wallet</button>
            <input type="text" id="wallet" placeholder="Wallet ID" readonly>
            <input type="text" id="username" placeholder="Nombre de usuario">
            <input type="password" id="password" placeholder="Contraseña">
            <input type="text" id="codigo" placeholder="Código Temporal" readonly>
            <button onclick="registrarUsuario()">Registrar</button>

            <h2>Inicio de Sesión</h2>
            <input type="text" id="loginUsername" placeholder="Nombre de usuario">
            <input type="password" id="loginPassword" placeholder="Contraseña">
            <button onclick="iniciarSesion()">Iniciar Sesión</button>

            <h2>Acción de Usuario</h2>
            <input type="text" id="accion" placeholder="Acción (explorar/intercambiar)">
            <button onclick="realizarAccion()">Realizar Acción</button>

            <h2>Blockchain</h2>
            <button onclick="verBlockchain()">Ver Blockchain</button>

            <h2>Crear Wallet</h2>
            <button onclick="crearWallet()">Crear Wallet</button>

            <h2>Validar Registro</h2>
            <input type="number" id="forks" placeholder="Número de forks">
            <button onclick="validarRegistro()">Validar Registro</button>
        </div>
        <script src="/static/script.js"></script>
    </body>
    </html>
    """
    return render_template_string(html_content)

@app.route('/static/script.js')
def script_js():
    js_content = """
    let codigoTemporal;
    let timer;

    function generarWallet() {
        const walletId = "bkmv" + Math.random().toString(36).substring(2, 10);
        document.getElementById('wallet').value = walletId;
        generarCodigoTemporal();
    }

    function generarCodigoTemporal() {
        clearInterval(timer);
        codigoTemporal = Math.floor(100000 + Math.random() * 900000);
        document.getElementById('codigo').value = codigoTemporal;
        timer = setInterval(generarCodigoTemporal, 30000);
    }

    async function registrarUsuario() {
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;
        const wallet = document.getElementById('wallet').value;
        const codigo = document.getElementById('codigo').value;
        if (codigo != codigoTemporal) {
            alert("Código temporal incorrecto");
            return;
        }
        const response = await fetch('/registro', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, password, wallet })
        });
        const data = await response.json();
        alert(data.message);
    }

    async function iniciarSesion() {
        const username = document.getElementById('loginUsername').value;
        const password = document.getElementById('loginPassword').value;
        const response = await fetch('/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, password })
        });
        const data = await response.json();
        alert(data.message);
    }

    async function realizarAccion() {
        const username = document.getElementById('loginUsername').value;
        const password = document.getElementById('loginPassword').value;
        const accion = document.getElementById('accion').value;
        const response = await fetch('/accion', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, password, accion })
        });
        const data = await response.json();
        alert(data.message);
    }

    async function verBlockchain() {
        const response = await fetch('/blockchain');
        const data = await response.json();
        alert(JSON.stringify(data.blockchain, null, 2));
    }

    async function crearWallet() {
        const response = await fetch('/crear_wallet', {
            method: 'POST'
        });
        const data = await response.json();
        alert(data.message);
    }

    async function validarRegistro() {
        const forks = document.getElementById('forks').value;
        const response = await fetch('/validar_registro', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ forks })
        });
        const data = await response.json();
        alert(data.message);
    }
    """
    return js_content

if __name__ == "__main__":
    app.run(debug=True)
