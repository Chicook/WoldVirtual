class RecursosUsuario:
    def __init__(self, porcentaje_cpu, porcentaje_ancho_banda):
        self.porcentaje_cpu = porcentaje_cpu
        self.porcentaje_ancho_banda = porcentaje_ancho_banda

    @staticmethod
    def asignar_recursos_a_usuario(usuario, recursos_comunitarios):
        recursos_asignados = {
            'cpu': recursos_comunitarios['cpu'] * (usuario.porcentaje_cpu / 100),
            'ancho_banda': recursos_comunitarios['ancho_banda'] * (usuario.porcentaje_ancho_banda / 100),
        }
        return recursos_asignados

class MonitoreoRecursos:
    def __init__(self):
        self.recursos_usuarios = {}

    def actualizar_recursos(self, nombre_usuario, uso_cpu, uso_ancho_banda):
        self.recursos_usuarios[nombre_usuario] = {
            'uso_cpu': uso_cpu,
            'uso_ancho_banda': uso_ancho_banda
        }

    def obtener_informacion(self):
        return self.recursos_usuarios

    @staticmethod
    def inicializar():
        print("Recursos inicializados")
