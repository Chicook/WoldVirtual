# BK_3App.py
from reflex import ReflexApp
from recursos import RecursosUsuario, asignar_recursos_a_usuario, MonitoreoRecursos

class BK_3App(ReflexApp):
    def __init__(self):
            super().__init__()
                    self.title = "Recursos"

                        def render(self):
                                # Aquí puedes añadir la lógica de representación web para recursos
                                        return "Gestión de Recursos"

                                        if __name__ == "__main__":
                                            app = BK_3App()
                                                app.run()
                                            