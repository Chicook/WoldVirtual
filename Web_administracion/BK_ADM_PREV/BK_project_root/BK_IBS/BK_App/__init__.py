# BK_App/__init__.py
from reflex import ReflexApp

class BK_App(ReflexApp):
    def __init__(self):
            super().__init__()
                    self.title = "BK_App Overview"
                            self.description = """
                                    Este módulo contiene varias aplicaciones que gestionan diferentes aspectos del sistema:
                                            - BK_1App: Módulo principal con el menú de secciones.
                                                    - BK_2App: Gestión de usuarios.
                                                            - BK_3App: Gestión de recursos.
                                                                    - BK_4App: Gestión de blockchain.
                                                                            - BK_5App: Gestión de compresión de datos.
                                                                                    """

                                                                                        def render(self):
                                                                                                return f"""
                                                                                                        <h1>{self.title}</h1>
                                                                                                                <p>{self.description}</p>
                                                                                                                        """

                                                                                                                        if __name__ == "__main__":
                                                                                                                            app = BK_App()
                                                                                                                                app.run()
                                                                                                                            