import sys
import os

# Añadir el directorio BK_bkP1 al path
sys.path.append(os.path.dirname(__file__))

from main import app, blockchain, db

if __name__ == '__main__':
    # Añadir el bloque génesis a la base de datos interna
        db.add_block(blockchain.chain[0])
            # Ejecutar la API
                app.run(debug=True)
        