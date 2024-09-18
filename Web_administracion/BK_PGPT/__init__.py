from flask import Flask
from app.blockchain.blockchain import Blockchain  # Importar la blockchain
from app.database import init_db                  # Inicializar la base de datos
from app.users import users_blueprint             # Blueprint de rutas de usuarios
from app.wallet import wallet_blueprint           # Blueprint de rutas de wallet
from app.admin import admin_blueprint             # Blueprint del panel de administración
import reflex as rx                               # Para la interfaz interactiva con Reflex
import threading                                  # Para correr la blockchain y Reflex en hilos separados

app = Flask(__name__)

# 1. Inicializa la base de datos SQLite
init_db()

# 2. Registrar los Blueprints para las diferentes funcionalidades
app.register_blueprint(users_blueprint, url_prefix='/users')
app.register_blueprint(wallet_blueprint, url_prefix='/wallet')
app.register_blueprint(admin_blueprint, url_prefix='/admin')

# 3. Inicia la blockchain en un hilo separado
blockchain = Blockchain()

@app.route('/')
def index():
    return "Bienvenido a la plataforma Blockchain"

    if __name__ == '__main__':
        # Ejecutar la Blockchain en un hilo separado
            blockchain_thread = threading.Thread(target=blockchain.run)
                blockchain_thread.start()

                    # Levantar Reflex en otro hilo para manejar la interfaz web interactiva
                        reflex_thread = threading.Thread(target=rx.run_app)
                            reflex_thread.start()

                                # 4. Iniciar el servidor Flask para manejar las rutas
                                    app.run(debug=True)
            