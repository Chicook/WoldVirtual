import prb5

usuarios = {}

def registrar_usuario(nombre_usuario, contraseña, wallet):
    usuarios[nombre_usuario] = {
        'contraseña': contraseña,
        'wallet_id': wallet
    }
    prb5.registrar_en_blockchain(f"Usuario registrado: {nombre_usuario}")

def verificar_credenciales(nombre_usuario, contraseña):
    if nombre_usuario in usuarios and usuarios[nombre_usuario]['contraseña'] == contraseña:
        return True
    return False
