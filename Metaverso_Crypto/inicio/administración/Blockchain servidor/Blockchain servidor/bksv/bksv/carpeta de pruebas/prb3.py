import uuid
import prb5

def generar_codigo_temporal():
    return str(uuid.uuid4())

def manejar_accion(nombre_usuario, accion):
    prb5.registrar_en_blockchain(f"Acción realizada: {accion} por {nombre_usuario}")
