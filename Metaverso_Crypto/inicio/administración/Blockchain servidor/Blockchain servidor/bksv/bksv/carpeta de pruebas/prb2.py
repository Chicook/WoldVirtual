import hashlib
import prb4

usuarios = {}

def registrar_usuario(username, password, wallet_id):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    usuarios[username] = {'password': hashed_password, 'wallet': wallet_id}
    prb4.registrar_actividad_css(f"Usuario registrado: {username}")

def verificar_credenciales(username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return usuarios.get(username, {}).get('password') == hashed_password
