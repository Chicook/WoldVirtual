# usuarios.py

import hashlib

# Diccionario para almacenar usuarios y contraseñas
usuarios = {}

def registrar_usuario(username, password):
    """
    Registra un nuevo usuario con un nombre de usuario y una contraseña.
    """
    if username in usuarios:
        raise ValueError("El usuario ya existe.")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    usuarios[username] = hashed_password
    print(f"Usuario {username} registrado con éxito.")

def verificar_credenciales(username, password):
    """
    Verifica las credenciales de un usuario.
    """
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return usuarios.get(username) == hashed_password

def manejar_accion(usuario, accion):
    """
    Maneja diferentes acciones para un usuario.
    """
    if accion == "explorar":
        print(f"Bienvenido/a {usuario} al entorno de exploración.")
    elif accion == "intercambiar":
        print(f"Realizando intercambio para {usuario}.")
    else:
        print("Acción no reconocida.")
