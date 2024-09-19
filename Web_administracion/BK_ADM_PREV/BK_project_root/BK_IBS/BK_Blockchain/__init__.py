# BK_Blockchain/__init__.py
from reflex import ReflexApp

class BK_Blockchain(ReflexApp):
    def __init__(self):
            super().__init__()
                    self.title = "BK_Blockchain Overview"
                            self.description = """
                                    Este módulo contiene varias aplicaciones que gestionan diferentes aspectos de la blockchain:
                                            - BK_1Blockchain: Módulo principal que coordina las funciones.
                                                    - BK_2Blockchain: Creación del bloque génesis.
                                                            - BK_3Blockchain: Adición de nuevos bloques.
                                                                    - BK_4Blockchain: Obtención de información de la cadena.
                                                                            - BK_5Blockchain: Validación de la cadena y función de hash.
                                                                                    """

                                                                                        def render(self):
                                                                                                return f"""
                                                                                                        <h1>{self.title}</h1>
                                                                                                                <p>{self.description}</p>
                                                                                                                        """

                                                                                                                        if __name__ == "__main__":
                                                                                                                            app = BK_Blockchain()
                                                                                                                                app.run()
                                                                                                                            