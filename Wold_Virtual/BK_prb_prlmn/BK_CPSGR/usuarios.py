import hashlib

usuarios = {}

def registrar_usuario(username, password):
    if username in usuarios:
        raise ValueError("El usuario ya existe.")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    usuarios[username] = hashed_password
    print(f"Usuario {username} registrado con éxito.")

def verificar_credenciales(username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return usuarios.get(username) == hashed_password

def manejar_accion(usuario, accion):
    if accion == "explorar":
        print(f"Bienvenido/a {usuario} al entorno de exploración.")
    elif accion == "intercambiar":
        print(f"Realizando intercambio para {usuario}.")
    else:
        print("Acción no reconocida.")
