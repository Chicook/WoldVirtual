# módulo usuarios # 

import hashlib

# Diccionario para almacenar usuarios y contraseñas
usuarios = {}

def registrar_usuario(username, password):
    """
    Registra un nuevo usuario con una contraseña encriptada.

    Args:
        username (str): Nombre de usuario.
        password (str): Contraseña del usuario.

    Raises:
        ValueError: Si el usuario ya existe.
    """
    if username in usuarios:
        raise ValueError("El usuario ya existe.")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    usuarios[username] = hashed_password
    print(f"Usuario {username} registrado con éxito.")

def verificar_credenciales(username, password):
    """
    Verifica las credenciales del usuario.

    Args:
        username (str): Nombre de usuario.
        password (str): Contraseña del usuario.

    Returns:
        bool: True si las credenciales son correctas, False en caso contrario.
    """
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return usuarios.get(username) == hashed_password

def manejar_accion(usuario, accion):
    """
    Maneja las acciones del usuario.

    Args:
        usuario (str): Nombre del usuario.
        accion (str): Acción a realizar.

    Raises:
        ValueError: Si la acción no es reconocida.
    """
    acciones = {
        "explorar": f"Bienvenido/a {usuario} al entorno de exploración.",
        "intercambiar": f"Realizando intercambio para {usuario}."
    }
    print(acciones.get(accion, "Acción no reconocida."))

def eliminar_usuario(username):
    """
    Elimina un usuario del sistema.

    Args:
        username (str): Nombre del usuario a eliminar.

    Raises:
        ValueError: Si el usuario no existe.
    """
    if username in usuarios:
        del usuarios[username]
        print(f"Usuario {username} eliminado con éxito.")
    else:
        raise ValueError("El usuario no existe.")

def listar_usuarios():
    """
    Lista todos los usuarios registrados.

    Returns:
        list: Lista de nombres de usuarios.
    """
    return list(usuarios.keys())

# Ejemplo de uso
if __name__ == "__main__":
    try:
        registrar_usuario("nombre", "contraseña")
        if verificar_credenciales("nombre", "contraseña"):
            manejar_accion("nombre", "explorar")
        else:
            print("Credenciales incorrectas.")
        print(f"Usuarios registrados: {listar_usuarios()}")
        eliminar_usuario("nombre")
        print(f"Usuarios registrados después de eliminar: {listar_usuarios()}")
    except ValueError as e:
        print(e)
        
# modulo usuarios #

# import hashlib

# Diccionario para almacenar usuarios y contraseñas
# usuarios = {}

# def registrar_usuario(username, password):
   # """
   # Registra un nuevo usuario con una contraseña encriptada.

   # Args:
      #  username (str): Nombre de usuario.
       # password (str): Contraseña del usuario.

  #  Raises:
      #  ValueError: Si el usuario ya existe.
   # """
   # if username in usuarios:
      #  raise ValueError("El usuario ya existe.")
  #  hashed_password = hashlib.sha256(password.encode()).hexdigest()
  #  usuarios[username] = hashed_password
   # print(f"Usuario {username} registrado con éxito.")

# def verificar_credenciales(username, password):
   # """
   # Verifica las credenciales del usuario.

   # Args:
       # username (str): Nombre de usuario.
      #  password (str): Contraseña del usuario.

  #  Returns:
      #  bool: True si las credenciales son correctas, False en caso contrario.
   # """
   # hashed_password = hashlib.sha256(password.encode()).hexdigest()
 #   return usuarios.get(username) == hashed_password

# def manejar_accion(usuario, accion):
  #  """
 #   Maneja las acciones del usuario.

  #  Args:
      #  usuario (str): Nombre del usuario.
      #  accion (str): Acción a realizar.

  #  Raises:
      #  ValueError: Si la acción no es reconocida.
   # """
  #  acciones = {
       # "explorar": f"Bienvenido/a {usuario} al entorno de exploración.",
      #  "intercambiar": f"Realizando intercambio para {usuario}."
 #   }
   # print(acciones.get(accion, "Acción no reconocida."))

# Ejemplo de uso
# if __name__ == "__main__":
  #  try:
      #  registrar_usuario("nombre", "contraseña")
     #   if verificar_credenciales("nombre", "contraseña"):
          #  manejar_accion("nombre", "explorar")
       # else:
           # print("Credenciales incorrectas.")
 #   except ValueError as e:
       # print(e)

# usuarios.py

# import hashlib

# Diccionario para almacenar usuarios y contraseñas
# usuarios = {}

# def registrar_usuario(username, password):
   # if username in usuarios:
       # raise ValueError("El usuario ya existe.")
   # hashed_password = hashlib.sha256(password.encode()).hexdigest()
   # usuarios[username] = hashed_password
   # print(f"Usuario {username} registrado con éxito.")

# def verificar_credenciales(username, password):
   # hashed_password = hashlib.sha256(password.encode()).hexdigest()
    # return usuarios.get(username) == hashed_password

# def manejar_accion(usuario, accion):
  #  if accion == "explorar":
       # print(f"Bienvenido/a {usuario} al entorno de exploración.")
   # elif accion == "intercambiar":
       # print(f"Realizando intercambio para {usuario}.")
   # else:
        # print("Acción no reconocida.")
