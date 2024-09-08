from utils import log_action, generar_codigo_temporal, verificar_codigo_temporal, confirmar_conexion_modulos

# Ejemplo de uso
log_action("Inicio del sistema")
codigo = generar_codigo_temporal()
print(f"Código temporal generado: {codigo}")

if verificar_codigo_temporal(codigo):
    print("Código temporal verificado correctamente.")
else:
    print("Código temporal inválido o expirado.")

confirmar_conexion_modulos(["bksv.py", "Módulo2"])
