from flask import Flask
from app.blockchain.blockchain import Blockchain
from app.database import init_db
from app.users import users_blueprint
from app.wallet import wallet_blueprint
from app.admin import admin_blueprint
import reflex as rx
import threading

app = Flask(__name__)

# Inicializa la base de datos
init_db()

# Registra los Blueprints
app.register_blueprint(users_blueprint, url_prefix='/users')
app.register_blueprint(wallet_blueprint, url_prefix='/wallet')
app.register_blueprint(admin_blueprint, url_prefix='/admin')

# Inicia la blockchain en un hilo separado
blockchain = Blockchain()

@app.route('/')
def index():
    return "Bienvenido a la plataforma Blockchain"

    if __name__ == '__main__':
        # Ejecutar la Blockchain en un hilo separado
            blockchain_thread = threading.Thread(target=blockchain.run)
                blockchain_thread.start()

                    # Levantar Reflex en otro hilo
                        reflex_thread = threading.Thread(target=rx.run_app)
                            reflex_thread.start()

                                # Iniciar el servidor Flask
                                    app.run(debug=True)
            