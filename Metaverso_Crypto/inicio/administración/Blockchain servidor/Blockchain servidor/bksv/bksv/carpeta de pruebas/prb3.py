from prb2 import verificar_credenciales, registrar_actividad

def manejar_accion(usuario, accion):
    if accion == "explorar":
        print(f"Bienvenido/a {usuario} al entorno de exploración.")
    elif accion == "intercambiar":
        print(f"Realizando intercambio para {usuario}.")
    else:
        print("Acción no reconocida.")
    registrar_actividad(f"Acción realizada: {accion} por {usuario}")

# Ejemplo de verificación de credenciales y manejo de entorno virtual
usuario_actual = "usuario1"
contrasena_ingresada = "contrasena_segura"

if verificar_credenciales(usuario_actual, contrasena_ingresada):
    print("Inicio de sesión exitoso")
    accion_usuario = "explorar"
    manejar_accion(usuario_actual, accion_usuario)
else:
    print("Credenciales incorrectas")
