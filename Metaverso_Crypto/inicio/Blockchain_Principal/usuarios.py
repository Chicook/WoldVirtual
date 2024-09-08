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

def actualizar_usuario(username, new_data):
    """
    Actualiza los datos de un usuario existente.

    Args:
        username (str): Nombre de usuario.
        new_data (dict): Nuevos datos para actualizar el usuario.

    Raises:
        ValueError: Si el usuario no existe.
    """
    if username not in usuarios:
        raise ValueError("El usuario no existe.")
    
    if 'password' in new_data:
        hashed_password = hashlib.sha256(new_data['password'].encode()).hexdigest()
        usuarios[username] = hashed_password
        print(f"Contraseña de {username} actualizada con éxito.")
    else:
        print("No se proporcionaron datos válidos para actualizar.")

# Ejemplo de uso
if __name__ == "__main__":
    try:
        registrar_usuario("nombre", "contraseña")
        if verificar_credenciales("nombre", "contraseña"):
            manejar_accion("nombre", "explorar")
            actualizar_usuario("nombre", {"password": "nueva_contraseña"})
            if verificar_credenciales("nombre", "nueva_contraseña"):
                print("Contraseña actualizada y verificada con éxito.")
            else:
                print("Error al verificar la nueva contraseña.")
        else:
            print("Credenciales incorrectas.")
    except ValueError as e:
        print(e)
