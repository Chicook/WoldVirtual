import hashlib

usuarios = {}

def registrar_usuario(username, password):
    """
    Registra un nuevo usuario con un nombre de usuario y una contraseña.
    
    :param username: Nombre de usuario (str).
    :param password: Contraseña (str).
    """
    if username in usuarios:
        raise ValueError("El usuario ya existe.")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    usuarios[username] = hashed_password
    print(f"Usuario {username} registrado con éxito.")

def verificar_credenciales(username, password):
    """
    Verifica las credenciales de un usuario.
    
    :param username: Nombre de usuario (str).
    :param password: Contraseña (str).
    :return: True si las credenciales son correctas, False en caso contrario.
    """
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return usuarios.get(username) == hashed_password

def manejar_accion(usuario, accion):
    """
    Maneja diferentes acciones para un usuario.
    
    :param usuario: Nombre de usuario (str).
    :param accion: Acción a realizar (str).
    """
    if accion == "explorar":
        print(f"Bienvenido/a {usuario} al entorno de exploración.")
    elif accion == "intercambiar":
        print(f"Realizando intercambio para {usuario}.")
    else:
        print("Acción no reconocida.")

# Ejemplo de uso
try:
    registrar_usuario("usuario1", "contraseña123")
    if verificar_credenciales("usuario1", "contraseña123"):
        manejar_accion("usuario1", "explorar")
    else:
        print("Credenciales incorrectas.")
except ValueError as e:
    print(e)
    
# import hashlib

# usuarios = {}

# def registrar_usuario(username, password):
   # hashed_password = hashlib.sha256(password.encode()).hexdigest()
  #  usuarios[username] = hashed_password

# def verificar_credenciales(username, password):
          #  hashed_password = hashlib.sha256(password.encode()).hexdigest()
           # return usuarios.get(username) == hashed_password

# def manejar_accion(usuario, accion):
   # if accion == "explorar":
    # print(f"Bienvenido/a {usuario} al entorno de exploración.")
  #  elif accion == "intercambiar":
   # print(f"Realizando intercambio para {usuario}.")
  #  else:
   # print("Acción no reconocida.")
                            
