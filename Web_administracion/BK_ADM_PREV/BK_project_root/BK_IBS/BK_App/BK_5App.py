# BK_5App.py
from reflex import ReflexApp
from compresion import comprimir_y_guardar_datos, cargar_y_descomprimir_datos

class BK_5App(ReflexApp):
    def __init__(self):
            super().__init__()
                    self.title = "Compresión"

                        def render(self):
                                # Aquí puedes añadir la lógica de representación web para compresión
                                        return "Gestión de Compresión"

                                        if __name__ == "__main__":
                                            app = BK_5App()
                                                app.run()
                                            