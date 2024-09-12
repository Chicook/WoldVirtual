class RecursosUsuario:
    def __init__(self, porcentaje_cpu, porcentaje_ancho_banda):
        self.porcentaje_cpu = porcentaje_cpu
        self.porcentaje_ancho_banda = porcentaje_ancho_banda

    def asignar_recursos(self, recursos_comunitarios):
        recursos_asignados = {
            'cpu': recursos_comunitarios['cpu'] * (self.porcentaje_cpu / 100),
            'ancho_banda': recursos_comunitarios['ancho_banda'] * (self.porcentaje_ancho_banda / 100),
        }
        log_action(f"Recursos asignados: {recursos_asignados}")
        return recursos_asignados
