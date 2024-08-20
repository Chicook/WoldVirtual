class RecursosUsuario:
    def __init__(self, porcentaje_cpu, porcentaje_ancho_banda):
        """
        Inicializa los recursos del usuario.
        
        :param porcentaje_cpu: Porcentaje de CPU asignado al usuario.
        :param porcentaje_ancho_banda: Porcentaje de ancho de banda asignado al usuario.
        """
        self.porcentaje_cpu = porcentaje_cpu
        self.porcentaje_ancho_banda = porcentaje_ancho_banda

    @staticmethod
    def asignar_recursos_a_usuario(usuario, recursos_comunitarios):
        """
        Asigna recursos comunitarios a un usuario basado en sus porcentajes.
        
        :param usuario: Instancia de RecursosUsuario.
        :param recursos_comunitarios: Diccionario con los recursos comunitarios.
        :return: Diccionario con los recursos asignados al usuario.
        """
        recursos_asignados = {
            'cpu': recursos_comunitarios['cpu'] * (usuario.porcentaje_cpu / 100),
            'ancho_banda': recursos_comunitarios['ancho_banda'] * (usuario.porcentaje_ancho_banda / 100),
        }
        return recursos_asignados

    def liberar_recursos(self):
        """
        Libera los recursos asignados al usuario.
        """
        self.porcentaje_cpu = 0
        self.porcentaje_ancho_banda = 0

    def obtener_recursos(self):
        """
        Obtiene los recursos actuales del usuario.
        
        :return: Diccionario con los recursos actuales del usuario.
        """
        return {
            'cpu': self.porcentaje_cpu,
            'ancho_banda': self.porcentaje_ancho_banda
        }

class MonitoreoRecursos:
    def __init__(self):
        """
        Inicializa el monitoreo de recursos.
        """
        self.recursos_usuarios = {}

    def actualizar_recursos(self, nombre_usuario, uso_cpu, uso_ancho_banda):
        """
        Actualiza el uso de recursos de un usuario.
        
        :param nombre_usuario: Nombre del usuario.
        :param uso_cpu: Uso de CPU del usuario.
        :param uso_ancho_banda: Uso de ancho de banda del usuario.
        """
        self.recursos_usuarios[nombre_usuario] = {
            'uso_cpu': uso_cpu,
            'uso_ancho_banda': uso_ancho_banda
        }

    def obtener_informacion(self):
        """
        Obtiene la información de uso de recursos de todos los usuarios.
        
        :return: Diccionario con la información de uso de recursos.
        """
        return self.recursos_usuarios

    def monitorear_uso_recursos(self):
        """
        Monitorea el uso de recursos de todos los usuarios.
        
        :return: Diccionario con el monitoreo de uso de recursos.
        """
        monitoreo = {}
        for usuario, recursos in self.recursos_usuarios.items():
            monitoreo[usuario] = {
                'uso_cpu': recursos['uso_cpu'],
                'uso_ancho_banda': recursos['uso_ancho_banda']
            }
        return monitoreo

    @staticmethod
    def inicializar():
        """
        Inicializa los recursos.
        """
        # Código para inicializar recursos
        print("Recursos inicializados")
