from flask import render_template_string
from Wold_Virtual.BK_webPbl.BK_MRGTRS.BK_BSINT4 import users_db

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
            window.location.href = '/user_table';
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

user_table_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tabla de Usuarios</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .table-container {
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            width: 80%;
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
        .delete-button {
            background-color: #ff4d4d;
            color: white;
            border: none;
            padding: 5px 10px;
            cursor: pointer;
            border-radius: 4px;
        }
        .delete-button:hover {
            background-color: #cc0000;
        }
    </style>
</head>
<body>
    <div class="table-container">
        <h2>Usuarios Registrados</h2>
        <table>
            <tr>
                <th>Hash</th>
                <th>Usuario</th>
                <th>Hash de Contraseña y Wallet</th>
                <th>Acciones</th>
            </tr>
            {% for user in users %}
            <tr>
                <td>{{ user.user_hash }}</td>
                <td>{{ user.username }}</td>
                <td>{{ user.password_wallet_hash }}</td>
                <td><button class="delete-button" onclick="deleteUser('{{ user.username }}')">Eliminar</button></td>
            </tr>
            {% endfor %}
        </table>
    </div>

    <script src="https://cdn.socket.io/4.0.0/socket.io.min.js"></script>
    <script>
        const socket = io();

        function deleteUser(username) {
            socket.emit('delete_user', { username });
        }

        socket.on('user_deleted', (data) => {
            window.location.reload();
        });
    </script>
</body>
</html>
"""

def register_routes(app, socketio):
    @app.route('/')
    def index():
        return render_template_string(html_template)

    @app.route('/user_table')
    def user_table():
        return render_template_string(user_table_template, users=list(users_db.values()))

    @socketio.on('register')
    def handle_register_event(data):
        handle_register(data)

    @socketio.on('delete_user')
    def handle_delete_user_event(data):
        handle_delete_user(data)
