from freflex import ReflexApp
import sys
import os

# Añadir la ruta de la carpeta 'BK_App' al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'BK_App')))

from BK_App import BK_App, MainApp, BK_2App, BK_3App, BK_4App, BK_5App

class MainPlatform(ReflexApp):
    def __init__(self):
            
        super().__init__()

                    self.title = "Main Platform"
                    self.modules = {
                                        
                    "Overview":   BK_App(),
                    "Usuarios":   BK_2App(),
                    "Recursos":   BK_3App(),
                    "Blockchain": BK_4App(),
                    "Compresión": BK_5App()
                                                                                               
}

     def render(self):
         menu = "<ul>"
                                                                                                                    for name, module in self.modules.items():
                                                                                                                                menu += f"<li><a href='#{name}'>{name}</a></li>"
                                                                                                                                        menu += "</ul>"

                                                                                                                                                content = "<div>"
                                                                                                                                                        for name, module in self.modules.items():
                                                                                                                                                                    content += f"<section id='{name}'>{module.render()}</section>"
                                                                                                                                                                            content += "</div>"

                                                                                                                                                                                    return f"""
                                                                                                                                                                                            <h1>{self.title}</h1>
                                                                                                                                                                                                    {menu}
                                                                                                                                                                                                            {content}
                                                                                                                                                                                                                    """

                                                                                                                                                                                                                    if __name__ == "__main__":
                                                                                                                                                                                                                        app = MainPlatform()
                                                                                                                                                                                                                            app.run()
                                                                                                                                                                                                                        

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
                                                                                                                                