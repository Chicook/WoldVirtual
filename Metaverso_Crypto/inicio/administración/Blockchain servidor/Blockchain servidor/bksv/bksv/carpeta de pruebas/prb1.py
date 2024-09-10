from prb2 import obtener_blockchain, agregar_bloque, obtener_bloque
from prb3 import registrar_usuario, verificar_credenciales
from prb4 import manejar_accion
from prb5 import generar_caracteristicas_faciales, renderizar_avatar_3d
import pytorch3d
import torch

if __name__ == '__main__':
    # Ejemplo de registro de usuario
    registrar_usuario("usuario1", "contrasena_segura")

    # Ejemplo de verificación de credenciales y manejo de entorno virtual
    usuario_actual = "usuario1"
    contrasena_ingresada = "contrasena_segura"

    if verificar_credenciales(usuario_actual, contrasena_ingresada):
        print("Inicio de sesión exitoso")
        accion_usuario = "explorar"
        manejar_accion(usuario_actual, accion_usuario)
    else:
        print("Credenciales incorrectas")

    # Ejemplo de agregar un bloque a la blockchain
    nuevo_bloque = agregar_bloque("Datos del bloque")
    print(f"Nuevo bloque agregado: {nuevo_bloque}")

    # Ejemplo de consultar un bloque específico
    bloque = obtener_bloque(1)
    if bloque:
        print(f"Bloque consultado: {bloque}")
    else:
        print("Índice de bloque inválido")

    # Ejemplo de generar características faciales y renderizar un avatar 3D
    image_path = 'ruta/a/tu/imagen/facial.jpg'
    facial_features = generar_caracteristicas_faciales(image_path)
    mesh = pytorch3d.utils.create_sphere(radius=1.0, device='cuda')
    images = renderizar_avatar_3d(mesh, facial_features)
    pytorch3d.vis.plot_image(images[0, ..., :3].cpu().numpy())
    
