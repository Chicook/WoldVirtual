from flask import Flask, render_template_string, request, redirect, url_for
from flask_socketio import SocketIO, emit
import hashlib
import random
import string
import threading

app = Flask(__name__)
socketio = SocketIO(app)

# Simulación de base de datos en memoria
users_db = {}

# HTML, CSS y JavaScript incluidos en una plantilla de cadena
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registro de Usuario</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .form-container {
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            width: 300px;
        }
        .form-container h2 {
            margin-top: 0;
        }
        .form-container input {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        .form-container button {
            width: 100%;
            padding: 10px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        .form-container button:hover {
            background-color: #0056b3;
        }
        .timer {
            text-align: center;
            margin: 10px 0;
        }
        .hash-container {
            margin-top: 20px;
            background-color: #fff;
            padding: 10px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        table, th, td {
            border: 1px solid black;
        }
        th, td {
            padding: 8px;
            text-align: left;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h2>Registro de Usuario</h2>
        <form id="registrationForm">
            <input type="text" id="username" placeholder="Nombre de Usuario" required>
            <input type="password" id="password" placeholder="Contraseña" required>
            <button type="button" id="generateWallet">Generar Wallet</button>
            <input type="text" id="wallet" placeholder="Wallet" readonly>
            <div class="timer">
                <span id="timer">30</span> segundos restantes
            </div>
            <input type="text" id="tempCode" placeholder="Código Temporal" required>
            <button type="submit">Enviar</button>
        </form>
        <div class="hash-container" id="hashContainer">
            <!-- Aquí se mostrarán los hashes -->
        </div>
    </div>

    <script src="https://cdn.socket.io/4.0.0/socket.io.min.js"></script>
    <script>
        const socket = io();
        let timerInterval;
        let tempCode = generateTempCode();

        document.getElementById('generateWallet').addEventListener('click', () => {
            const wallet = 'bkwv' + Math.random().toString(36).substring(2, 15);
            document.getElementById('wallet').value = wallet;
        });

        document.getElementById('registrationForm').addEventListener('submit', (event) => {
            event.preventDefault();
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;
            const wallet = document.getElementById('wallet').value;
            const tempCodeInput = document.getElementById('tempCode').value;

            if (tempCodeInput !== tempCode) {
                alert('Código temporal incorrecto.');
                return;
            }

            socket.emit('register', { username, password, wallet });
        });

        socket.on('start_timer', () => {
            let timeLeft = 30;
            timerInterval = setInterval(() => {
                if (timeLeft <= 0) {
                    clearInterval(timerInterval);
                    tempCode = generateTempCode();
                    alert('Tiempo agotado. Se ha generado un nuevo código temporal.');
                } else {
                    document.getElementById('timer').textContent = timeLeft;
                    timeLeft--;
                }
            }, 1000);
        });

        socket.on('registration_success', (data) => {
            const hashContainer = document.getElementById('hashContainer');
            hashContainer.innerHTML = `
                <table>
                    <tr>
                        <th>Hash</th>
                        <th>Usuario</th>
                        <th>Hash de Contraseña y Wallet</th>
                    </tr>
                    ${data.users.map(user => `
                        <tr>
                            <td>${user.userHash}</td>
                            <td>${user.username}</td>
                            <td>${user.passwordWalletHash}</td>
                        </tr>
                    `).join('')}
                </table>
            `;
        });

        function generateTempCode() {
            const code = Math.random().toString(36).substring(2, 8).toUpperCase();
            document.getElementById('tempCode').value = code;
            return code;
        }

        socket.emit('start_timer');
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(html_template)

@app.route('/admin_panel')
def admin_panel():
    return "Bienvenido al panel de administración"

@socketio.on('register')
def handle_register(data):
    username = data['username']
    password = data['password']
    wallet = data['wallet']

    if username in users_db:
        emit('registration_failed', {'message': 'Usuario ya registrado'})
        return

    # Generar hashes
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    user_hash = hashlib.sha256((username + wallet).encode()).hexdigest()
    password_wallet_hash = hashlib.sha256((password + wallet).encode()).hexdigest()

    # Almacenar en la base de datos simulada
    users_db[username] = {
        'username': username,
        'wallet': wallet,
        'password_hash': password_hash,
        'user_hash': user_hash,
        'password_wallet_hash': password_wallet_hash
    }

    emit('registration_success', {'users': list(users_db.values())})

if __name__ == '__main__':
    socketio.run(app, debug=True)

















"""
from flask import Flask, render_template_string, request, redirect, url_for
from flask_socketio import SocketIO, emit
import hashlib
import time
import threading
import random
import string

app = Flask(__name__)
socketio = SocketIO(app)

# HTML, CSS y JavaScript incluidos en una plantilla de cadena
html_template = """
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registro de Usuario</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .form-container {
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            width: 300px;
        }
        .form-container h2 {
            margin-top: 0;
        }
        .form-container input {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        .form-container button {
            width: 100%;
            padding: 10px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        .form-container button:hover {
            background-color: #0056b3;
        }
        .timer {
            text-align: center;
            margin: 10px 0;
        }
        .hash-container {
            margin-top: 20px;
            background-color: #fff;
            padding: 10px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h2>Registro de Usuario</h2>
        <form id="registrationForm">
            <input type="text" id="username" placeholder="Nombre de Usuario" required>
            <input type="password" id="password" placeholder="Contraseña" required>
            <button type="button" id="generateWallet">Generar Wallet</button>
            <input type="text" id="wallet" placeholder="Wallet" readonly>
            <div class="timer">
                <span id="timer">30</span> segundos restantes
            </div>
            <input type="text" id="tempCode" placeholder="Código Temporal" required>
            <button type="submit">Enviar</button>
        </form>
        <div class="hash-container" id="hashContainer">
            <!-- Aquí se mostrarán los hashes -->
        </div>
    </div>

    <script src="https://cdn.socket.io/4.0.0/socket.io.min.js"></script>
    <script>
        const socket = io();
        let timerInterval;
        let tempCode = generateTempCode();

        document.getElementById('generateWallet').addEventListener('click', () => {
            const wallet = 'bkwv' + Math.random().toString(36).substring(2, 15);
            document.getElementById('wallet').value = wallet;
        });

        document.getElementById('registrationForm').addEventListener('submit', (event) => {
            event.preventDefault();
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;
            const wallet = document.getElementById('wallet').value;
            const tempCodeInput = document.getElementById('tempCode').value;

            if (tempCodeInput !== tempCode) {
                alert('Código temporal incorrecto.');
                return;
            }

            socket.emit('register', { username, password, wallet });
        });

        socket.on('start_timer', () => {
            let timeLeft = 30;
            timerInterval = setInterval(() => {
                if (timeLeft <= 0) {
                    clearInterval(timerInterval);
                    tempCode = generateTempCode();
                    alert('Tiempo agotado. Se ha generado un nuevo código temporal.');
                } else {
                    document.getElementById('timer').textContent = timeLeft;
                    timeLeft--;
                }
            }, 1000);
        });

        socket.on('registration_success', (data) => {
            const hashContainer = document.getElementById('hashContainer');
            hashContainer.innerHTML = `
                <p>Hash: ${data.userHash}</p>
                <p>Usuario: ${data.username}</p>
                <p>Hash de Contraseña y Wallet: ${data.passwordWalletHash}</p>
            `;
            window.location.href = '/admin_panel';
        });

        function generateTempCode() {
            const code = Math.random().toString(36).substring(2, 8).toUpperCase();
            document.getElementById('tempCode').value = code;
            return code;
        }

        socket.emit('start_timer');
    </script>
</body>
</html>
"""
"""
@app.route('/')
def index():
    return render_template_string(html_template)

@app.route('/admin_panel')
def admin_panel():
    return "Bienvenido al panel de administración"

@socketio.on('register')
def handle_register(data):
    username = data['username']
    password = data['password']
    wallet = data['wallet']

    # Generar hashes
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    user_hash = hashlib.sha256((username + wallet).encode()).hexdigest()
    password_wallet_hash = hashlib.sha256((password + wallet).encode()).hexdigest()

    # Simulación de almacenamiento en base de datos
    print(f"Usuario: {username}, Wallet: {wallet}, Password Hash: {password_hash}, User Hash: {user_hash}, Password Wallet Hash: {password_wallet_hash}")

    emit('registration_success', {
        'username': username,
        'userHash': user_hash,
        'passwordWalletHash': password_wallet_hash
    })

if __name__ == '__main__':
    socketio.run(app, debug=True)
    

from flask import Flask, render_template_string, request, redirect, url_for
from flask_socketio import SocketIO, emit
import hashlib
import time
import threading

app = Flask(__name__)
socketio = SocketIO(app)

# HTML, CSS y JavaScript incluidos en una plantilla de cadena
html_template = """
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registro de Usuario</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .form-container {
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            width: 300px;
        }
        .form-container h2 {
            margin-top: 0;
        }
        .form-container input {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        .form-container button {
            width: 100%;
            padding: 10px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        .form-container button:hover {
            background-color: #0056b3;
        }
        .timer {
            text-align: center;
            margin: 10px 0;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h2>Registro de Usuario</h2>
        <form id="registrationForm">
            <input type="text" id="username" placeholder="Nombre de Usuario" required>
            <input type="password" id="password" placeholder="Contraseña" required>
            <button type="button" id="generateWallet">Generar Wallet</button>
            <input type="text" id="wallet" placeholder="Wallet" readonly>
            <div class="timer">
                <span id="timer">30</span> segundos restantes
            </div>
            <input type="text" id="tempCode" placeholder="Código Temporal" required>
            <button type="submit">Enviar</button>
        </form>
    </div>

    <script src="https://cdn.socket.io/4.0.0/socket.io.min.js"></script>
    <script>
        const socket = io();
        let timerInterval;

        document.getElementById('generateWallet').addEventListener('click', () => {
            const wallet = 'bkwv' + Math.random().toString(36).substring(2, 15);
            document.getElementById('wallet').value = wallet;
        });

        document.getElementById('registrationForm').addEventListener('submit', (event) => {
            event.preventDefault();
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;
            const wallet = document.getElementById('wallet').value;
            const tempCode = document.getElementById('tempCode').value;

            socket.emit('register', { username, password, wallet, tempCode });
        });

        socket.on('start_timer', () => {
            let timeLeft = 30;
            timerInterval = setInterval(() => {
                if (timeLeft <= 0) {
                    clearInterval(timerInterval);
                    alert('Tiempo agotado para ingresar el código temporal.');
                } else {
                    document.getElementById('timer').textContent = timeLeft;
                    timeLeft--;
                }
            }, 1000);
        });

        socket.on('registration_success', () => {
            window.location.href = '/admin_panel';
        });
    </script>
</body>
</html>
"""
"""
@app.route('/')
def index():
    return render_template_string(html_template)

@app.route('/admin_panel')
def admin_panel():
    return "Bienvenido al panel de administración"

@socketio.on('register')
def handle_register(data):
    username = data['username']
    password = data['password']
    wallet = data['wallet']
    temp_code = data['tempCode']

    # Aquí puedes agregar la lógica para verificar el código temporal y manejar el registro del usuario
    # Por ejemplo, puedes generar un hash de la contraseña y almacenar los datos en la base de datos

    password_hash = hashlib.sha256(password.encode()).hexdigest()
    user_hash = hashlib.sha256((username + wallet).encode()).hexdigest()

    # Simulación de almacenamiento en base de datos
    print(f"Usuario: {username}, Wallet: {wallet}, Password Hash: {password_hash}, User Hash: {user_hash}")

    emit('registration_success')

if __name__ == '__main__':
    socketio.run(app, debug=True)

"""

"""
from flask import Flask, render_template_string
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

# HTML, CSS y JavaScript incluidos en una plantilla de cadena
html_template = """
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Metaverso Crypto 3D</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f0f0f0;
        }
        .header {
            background-color: #007bff;
            color: white;
            padding: 10px 0;
            text-align: center;
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 1000;
        }
        .nav {
            display: flex;
            justify-content: center;
            background-color: #0056b3;
            padding: 10px 0;
        }
        .nav a {
            color: white;
            padding: 10px 20px;
            text-decoration: none;
            font-weight: bold;
        }
        .nav a:hover {
            background-color: #003d80;
        }
        .container {
            margin-top: 100px;
            padding: 20px;
        }
        .section {
            background-color: #fff;
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1, h2 {
            margin-top: 0;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>Metaverso Crypto 3D</h1>
    </div>
    <div class="nav">
        <a href="./Metaverso_Crypto/inicio/Blockchain_Principal/secciones/inicio.html">Inicio</a>
        <a href="#usuarios">Usuarios</a>
        <a href="#recursos">Recursos</a>
        <a href="#blockchain">Blockchain</a>
        <a href="#database">Base de Datos</a>
        <a href="#compresion">Compresión</a>
        <a href="#servidor">Servidor</a>
    </div>
    <div class="container">
        <div id="home" class="section">
            <h2>Metaverso Crypto 3D descentralizado</h2>
            <p>Próximamente en esta página principal, se darán más detalles sobre el proyecto. Tenemos diferentes secciones que explicarán su función, dentro de cada módulo programado en Python.</p>
        </div>
        <div id="usuarios" class="section">
            <h2>Usuarios</h2>
            <p>El módulo de usuarios permite registrar nuevos usuarios, verificar credenciales y manejar acciones específicas para cada usuario.</p>
        </div>
        <div id="recursos" class="section">
            <h2>Recursos</h2>
            <p>El módulo de recursos gestiona la asignación de recursos como CPU y ancho de banda a los usuarios, y monitorea el uso de estos recursos.</p>
        </div>
        <div id="blockchain" class="section">
            <h2>Blockchain</h2>
            <p>El módulo de blockchain permite crear y gestionar una cadena de bloques, añadiendo transacciones y validando la integridad de la cadena.</p>
        </div>
        <div id="database" class="section">
            <h2>Base de Datos</h2>
            <p>El módulo de base de datos se encarga de conectar a una base de datos PostgreSQL, ejecutar consultas y manejar los resultados.</p>
        </div>
        <div id="compresion" class="section">
            <h2>Compresión</h2>
            <p>El módulo de compresión permite comprimir y guardar datos en archivos, así como cargar y descomprimir estos datos cuando sea necesario.</p>
        </div>
        <div id="servidor" class="section">
            <h2>Servidor</h2>
            <p>El módulo de servidor utiliza Flask y Socket.IO para manejar las rutas web y la transmisión de datos en tiempo real.</p>
        </div>
    </div>

    <script src="https://cdn.socket.io/4.0.0/socket.io.min.js"></script>
    <script>
        const socket = io();

        document.getElementById('sendButton').addEventListener('click', () => {
            const audioData = document.getElementById('audioInput').value;
            socket.emit('audio_stream', audioData);
        });

        socket.on('audio_stream', (data) => {
            console.log('Received audio data:', data);
        });
    </script>
</body>
</html>
"""
"""
@app.route('/')
def index():
    return render_template_string(html_template)

@socketio.on('audio_stream')
def handle_audio(data):
    socketio.emit('audio_stream', data)

if __name__ == '__main__':
    socketio.run(app, debug=True)
"""



"""
from flask import Flask, render_template_string
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

# HTML, CSS y JavaScript incluidos en una plantilla de cadena
html_template = """
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Metaverso Crypto 3D</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f0f0f0;
        }
        .header {
            background-color: #007bff;
            color: white;
            padding: 10px 0;
            text-align: center;
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 1000;
        }
        .nav {
            display: flex;
            justify-content: center;
            background-color: #0056b3;
            padding: 10px 0;
        }
        .nav a {
            color: white;
            padding: 10px 20px;
            text-decoration: none;
            font-weight: bold;
        }
        .nav a:hover {
            background-color: #003d80;
        }
        .container {
            margin-top: 100px;
            padding: 20px;
        }
        .section {
            background-color: #fff;
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1, h2 {
            margin-top: 0;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>Metaverso Crypto 3D</h1>
    </div>
    <div class="nav">
        <a href="./Metaverso_Crypto/inicio/Blockchain_Principal/secciones/inicio.html">Inicio</a>
        <a href="#usuarios">Usuarios</a>
        <a href="#recursos">Recursos</a>
        <a href="#blockchain">Blockchain</a>
        <a href="#database">Base de Datos</a>
        <a href="#compresion">Compresión</a>
        <a href="#servidor">Servidor</a>
    </div>
    <div class="container">
        <div id="home" class="section">
            <h2>Metaverso Crypto 3D descentralizado</h2>
            <p>Próximamente en esta página principal, se darán más detalles sobre el proyecto. Tenemos diferentes secciones que explicarán su función, dentro de cada módulo programado en Python.</p>
        </div>
        <div id="usuarios" class="section">
            <h2>Usuarios</h2>
            <p>El módulo de usuarios permite registrar nuevos usuarios, verificar credenciales y manejar acciones específicas para cada usuario.</p>
        </div>
        <div id="recursos" class="section">
            <h2>Recursos</h2>
            <p>El módulo de recursos gestiona la asignación de recursos como CPU y ancho de banda a los usuarios, y monitorea el uso de estos recursos.</p>
        </div>
        <div id="blockchain" class="section">
            <h2>Blockchain</h2>
            <p>El módulo de blockchain permite crear y gestionar una cadena de bloques, añadiendo transacciones y validando la integridad de la cadena.</p>
        </div>
        <div id="database" class="section">
            <h2>Base de Datos</h2>
            <p>El módulo de base de datos se encarga de conectar a una base de datos PostgreSQL, ejecutar consultas y manejar los resultados.</p>
        </div>
        <div id="compresion" class="section">
            <h2>Compresión</h2>
            <p>El módulo de compresión permite comprimir y guardar datos en archivos, así como cargar y descomprimir estos datos cuando sea necesario.</p>
        </div>
        <div id="servidor" class="section">
            <h2>Servidor</h2>
            <p>El módulo de servidor utiliza Flask y Socket.IO para manejar las rutas web y la transmisión de datos en tiempo real.</p>
        </div>
    </div>

    <script src="https://cdn.socket.io/4.0.0/socket.io.min.js"></script>
    <script>
        const socket = io();

        document.getElementById('sendButton').addEventListener('click', () => {
            const audioData = document.getElementById('audioInput').value;
            socket.emit('audio_stream', audioData);
        });

        socket.on('audio_stream', (data) => {
            console.log('Received audio data:', data);
        });
    </script>
</body>
</html>
"""
"""
@app.route('/')
def index():
    return render_template_string(html_template)

@socketio.on('audio_stream')
def handle_audio(data):
    socketio.emit('audio_stream', data)

if __name__ == '__main__':
    socketio.run(app, debug=True)

    """
