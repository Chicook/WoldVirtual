from flask import Flask, render_template_string, request, jsonify
from flask_socketio import SocketIO
from blockchain import Blockchain
from usuarios import registrar_usuario, generar_wallet, enviar_wcv, generar_codigo_temporal, verificar_codigo_temporal, log_action

app = Flask(__name__)
socketio = SocketIO(app)

# Inicializar la blockchain
blockchain = Blockchain()

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registro de Usuario</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f9f9f9; }
        .header { background-color: #4CAF50; color: white; padding: 15px 0; text-align: center; }
        .container { margin: 20px auto; padding: 20px; max-width: 400px; background-color: #fff; border-radius: 8px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); }
        .form-group { margin-bottom: 15px; }
        label { display: block; margin-bottom: 5px; }
        input[type="text"], input[type="password"], input[type="number"] { width: 100%; padding: 8px; box-sizing: border-box; }
        .button { background-color: #4CAF50; border: none; color: white; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; border-radius: 4px; }
        .button:hover { background-color: #45a049; }
        .timer { font-size: 14px; color: red; }
    </style>
</head>
<body>
    <div class="header"><h1>Registro de Usuario</h1></div>
    <div class="container">
        <form method="POST" action="/register">
            <div class="form-group">
                <label for="wallet">Generar Wallet</label>
                <button type="button" class="button" onclick="generarWallet()">Generar Wallet</button>
                <input type="text" id="wallet" name="wallet" readonly>
            </div>
            <div class="form-group">
                <label for="username">Nombre de Usuario</label>
                <input type="text" id="username" name="username" required>
            </div>
            <div class="form-group">
                <label for="password">Contraseña</label>
                <input type="password" id="password" name="password" required>
            </div>
            <div class="form-group">
                <label for="codigo">Código Temporal de Verificación</label>
                <input type="text" id="codigo" name="codigo" required>
                <button type="button" class="button" onclick="generarCodigo()">Generar Código</button>
                <div class="timer" id="timer"></div>
            </div>
            <button type="submit" class="button">Registrar</button>
        </form>
    </div>
    <script>
        function generarWallet() {
            fetch('/generate_wallet').then(response => response.json()).then(data => {
                document.getElementById('wallet').value = data.wallet;
            });
        }

        function generarCodigo() {
            fetch('/generate_code').then(response => response.json()).then(data => {
                document.getElementById('codigo').value = data.codigo;
                startTimer();
            });
        }

        function startTimer() {
            var timer = document.getElementById('timer');
            var timeLeft = 30;
            var countdown = setInterval(function() {
                if (timeLeft <= 0) {
                    clearInterval(countdown);
                    timer.innerHTML = "Código expirado. Genera uno nuevo.";
                } else {
                    timer.innerHTML = "Tiempo restante: " + timeLeft + " segundos";
                }
                timeLeft -= 1;
            }, 1000);
        }
    </script>
</body>
</html>
"""

wallet_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Billetera WCV</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f9f9f9; }
        .header { background-color: #4CAF50; color: white; padding: 15px 0; text-align: center; }
        .container { margin: 20px auto; padding: 20px; max-width: 400px; background-color: #fff; border-radius: 8px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); }
        .info { font-size: 18px; }
    </style>
</head>
<body>
    <div class="header"><h1>Billetera WCV</h1></div>
    <div class="container">
        <div class="info">
            <p>Bienvenido a tu billetera WCV.</p>
            <p>Máximo total en circulación: 30,000,000.000 WCV</p>
            <p>Balance: 0 WCV</p>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    log_action("Página principal cargada")
    return render_template_string(html_template)

@app.route('/generate_wallet', methods=['GET'])
def generate_wallet():
    wallet = generar_wallet("usuario_temporal")
    return jsonify({'wallet': wallet})

@app.route('/generate_code', methods=['GET'])
def generate_code():
    codigo = generar_codigo_temporal()
    return jsonify({'codigo': codigo})

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    codigo = request.form['codigo']
    
    if verificar_codigo_temporal(codigo):
        try:
            registrar_usuario(username, password)
            wallet = generar_wallet(username)
            log_action(f"Usuario {username} registrado con wallet {wallet}")
            return render_template_string(wallet_template, balance=0)
        except ValueError as e:
            return str(e)
    return "Código de verificación inválido o expirado."

@app.route('/send_wcv', methods=['POST'])
def send_wcv():
    sender = "usuario1"  # Este debería ser el usuario autenticado
    receiver = request.form['receiver']
    amount = float(request.form['amount'])
    codigo = request.form['codigo']
    if verificar_codigo_temporal(codigo):
        try:
            enviar_wcv(sender, receiver, amount)
            return render_template_string(wallet_template, balance=balances[sender])
        except ValueError as e:
            return str(e)
    return "Código de verificación inválido o expirado."

if __name__ == '__main__':
    log_action("Servidor iniciado")
    socketio.run(app, debug=True)
            
