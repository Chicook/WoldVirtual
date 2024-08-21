# recursos.py

class RecursosUsuario:
    """
    Clase para gestionar los recursos asignados a un usuario.
    """
    def __init__(self, porcentaje_cpu, porcentaje_ancho_banda):
        self.porcentaje_cpu = porcentaje_cpu
        self.porcentaje_ancho_banda = porcentaje_ancho_banda

    @staticmethod
    def asignar_recursos_a_usuario(usuario, recursos_comunitarios):
        """
        Asigna recursos comunitarios a un usuario basado en sus porcentajes.
        """
        return {
            'cpu': recursos_comunitarios['cpu'] * (usuario.porcentaje_cpu / 100),
            'ancho_banda': recursos_comunitarios['ancho_banda'] * (usuario.porcentaje_ancho_banda / 100),
        }

class MonitoreoRecursos:
    """
    Clase para monitorear el uso de recursos por parte de los usuarios.
    """
    def __init__(self):
        self.recursos_usuarios = {}

    def actualizar_recursos(self, nombre_usuario, uso_cpu, uso_ancho_banda):
        """
        Actualiza el uso de recursos para un usuario específico.
        """
        self.recursos_usuarios[nombre_usuario] = {
            'uso_cpu': uso_cpu,
            'uso_ancho_banda': uso_ancho_banda
        }

    def obtener_informacion(self):
        """
        Obtiene la información de uso de recursos de todos los usuarios.
        """
        return self.recursos_usuarios

    @staticmethod
    def inicializar():
        """
        Inicializa los recursos.
        """
        print("Recursos inicializados")
