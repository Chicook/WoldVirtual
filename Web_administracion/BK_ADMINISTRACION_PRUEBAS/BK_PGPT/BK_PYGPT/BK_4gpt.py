from flask import request, jsonify
import hashlib
from app.database.queries import execute_query, fetch_query

def register():
    data = request.json
        hashed_password = hashlib.sha256(data['password'].encode()).hexdigest()
            
                query = "INSERT INTO usuarios (nombre, contraseña) VALUES (?, ?)"
                    execute_query(query, (data['username'], hashed_password))

                        return jsonify({"message": "Usuario registrado"})

                        def login():
                            data = request.json
                                hashed_password = hashlib.sha256(data['password'].encode()).hexdigest()
                                    
                                        query = "SELECT * FROM usuarios WHERE nombre=? AND contraseña=?"
                                            result = fetch_query(query, (data['username'], hashed_password))

                                                if result:
                                                        return jsonify({"message": "Login exitoso", "user_id": result[0][0]})
                                                            else:
                                                                    return jsonify({"message": "Usuario o contraseña incorrectos"}), 401
                            