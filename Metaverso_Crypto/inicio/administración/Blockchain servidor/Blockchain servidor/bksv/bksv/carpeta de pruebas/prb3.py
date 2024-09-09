import random
from prb2 import registrar_actividad_css

def generar_codigo_temporal():
    """
    Genera un código temporal de 6 dígitos.
    """
    return random.randint(100000, 999999)

def manejar_accion(usuario, accion):
    """
    Maneja las acciones del usuario y registra la actividad en la blockchain.
    
    Args:
        usuario (str): Nombre del usuario.
        accion (str): Acción a realizar (explorar/intercambiar).
    """
    if accion == "explorar":
        print(f"Bienvenido/a {usuario} al entorno de exploración.")
    elif accion == "intercambiar":
        print(f"Realizando intercambio para {usuario}.")
    else:
        print("Acción no reconocida.")
    
    # Registrar la actividad en la blockchain
    registrar_actividad_css(f"Acción realizada: {accion} por {usuario}")
