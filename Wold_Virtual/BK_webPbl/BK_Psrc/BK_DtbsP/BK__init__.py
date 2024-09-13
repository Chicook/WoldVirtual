# BK__init__.py
from .server import app as server_app
from .reflex_app import app as reflex_app
from .server import app as server_app
from .reflex_app import MyApp
import sys
import os

# Añadir el directorio BK_bkP1 al path
sys.path.append(os.path.join(os.path.dirname(__file__), '../BK_blockchain_project/BK_bkP1/BK_main.py', 'BK_bkP1'))

from main import app, blockchain, db

if __name__ == '__main__':
    # Añadir el bloque génesis a la base de datos interna
        db.add_block(blockchain.chain[0])

        
def start_app():
    my_app = MyApp()

        if __name__ == '__main__':
            start_app()

__all__ = ['server_app', 'reflex_app']

