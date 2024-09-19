# BK_4App.py
from reflex import ReflexApp
from blockchain import Blockchain

class BK_4App(ReflexApp):
    def __init__(self):
            super().__init__()
                    self.title = "Blockchain"

                        def render(self):
                                # Aquí puedes añadir la lógica de representación web para blockchain
                                        return "Gestión de Blockchain"

                                        if __name__ == "__main__":
                                            app = BK_4App()
                                                app.run()
                                            