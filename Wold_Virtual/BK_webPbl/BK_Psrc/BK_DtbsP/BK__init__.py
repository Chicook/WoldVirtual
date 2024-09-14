import sys
import os

# Importar aplicaciones del servidor y Reflex
from .server import app as server_app
from .reflex_app import app as reflex_app
from .reflex_app import MyApp

# Añadir el directorio BK_bkP1 al path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'BK_blockchain_project', 'BK_bkP1'))

from main import app, blockchain, db

# Función para iniciar la aplicación
def start_app():
    my_app = MyApp()
    my_app.run()

if __name__ == '__main__':
    # Añadir el bloque génesis a la base de datos interna
    db.add_block(blockchain.chain[0])
    # Ejecutar la API
    app.run(debug=True)

__all__ = ['server_app', 'reflex_app']
