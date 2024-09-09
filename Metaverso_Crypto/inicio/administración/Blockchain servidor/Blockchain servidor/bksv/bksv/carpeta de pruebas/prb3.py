import uuid
import prb4

def generar_codigo_temporal():
    return str(uuid.uuid4())

def manejar_accion(nombre_usuario, accion):
    prb4.registrar_actividad_css(f"Acción realizada: {accion} por {nombre_usuario}")
