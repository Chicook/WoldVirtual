from flask import Flask, jsonify, request
from prb2 import verificar_credenciales, registrar_actividad_css

app = Flask(__name__)

def manejar_accion(usuario, accion):
    if accion == "explorar":
        print(f"Bienvenido/a {usuario} al entorno de exploración.")
    elif accion == "intercambiar":
        print(f"Realizando intercambio para {usuario}.")
    else:
        print("Acción no reconocida.")
    registrar_actividad_css(f"Acción realizada: {accion} por {usuario}")

# Ejemplo de verificación de credenciales y manejo de entorno virtual
usuario_actual = "usuario1"
contrasena_ingresada = "contrasena_segura"

if verificar_credenciales(usuario_actual, contrasena_ingresada):
    print("Inicio de sesión exitoso")
    accion_usuario = "explorar"
    manejar_accion(usuario_actual, accion_usuario)
else:
    print("Credenciales incorrectas")

# JavaScript
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

@app.route('/static/script.js')
def script_js():
    return js_content

if __name__ == '__main__':
    app.run(debug=True)
