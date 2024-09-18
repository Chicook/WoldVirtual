from flask import jsonify, request
import random
import string
from app.database.queries import execute_query

def create_wallet():
    wallet_id = 'bkwv' + ''.join(random.choices(string.ascii_lowercase + string.digits, k=36))
        data = request.json
            
                query = "UPDATE usuarios SET wallet=? WHERE id=?"
                    execute_query(query, (wallet_id, data['user_id']))

                        return jsonify({"wallet_id": wallet_id})

                        def send():
                            # Lógica para enviar transacciones entre usuarios
                                pass

                                def receive():
                                    # Lógica para recibir transacciones
                                        pass
                                