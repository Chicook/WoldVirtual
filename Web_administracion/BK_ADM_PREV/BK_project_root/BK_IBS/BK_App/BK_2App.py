# BK_2App.py
from reflex import ReflexApp
from usuarios import registrar_usuario, verificar_credenciales, manejar_accion

class BK_2App(ReflexApp):
    def __init__(self):
            super().__init__()
                    self.title = "Usuarios"

                        def render(self):
                                # Aquí puedes añadir la lógica de representación web para usuarios
                                        return "Gestión de Usuarios"

                                        if __name__ == "__main__":
                                            app = BK_2App()
                                                app.run()
                                            