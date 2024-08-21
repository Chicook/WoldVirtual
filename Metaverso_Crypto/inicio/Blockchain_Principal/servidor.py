# servidor 

from flask import Flask, render_template_string
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Metaverso Crypto 3D</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f0f0f0; }
        .header { background-color: #007bff; color: white; padding: 10px 0; text-align: center; position: fixed; width: 100%; top: 0; z-index: 1000; }
        .nav { display: flex; justify-content: center; background-color: #0056b3; padding: 10px 0; }
        .nav a { color: white; padding: 10px 20px; text-decoration: none; font-weight: bold; }
        .nav a:hover { background-color: #003d80; }
        .container { margin-top: 100px; padding: 20px; }
        .section { background-color: #fff; padding: 20px; margin-bottom: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); }
        h1, h2 { margin-top: 0; }
    </style>
</head>
<body>
    <div class="header"><h1>Metaverso Crypto 3D</h1></div>
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
            <p>Próximamente en esta página principal, se darán más detalles sobre el proyecto...</p>
        </div>
        <!-- Secciones adicionales aquí -->
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
