from flask import Flask, render_template_string
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

# HTML, CSS y JavaScript incluidos en una plantilla de cadena
html_template = """

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

@app.route('/')
def index():
    return render_template_string(html_template)

@socketio.on('audio_stream')
def handle_audio(data):
    socketio.emit('audio_stream', data)

if __name__ == '__main__':
    socketio.run(app, debug=True)




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
