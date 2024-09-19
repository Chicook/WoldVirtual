# BK_1App.py
from reflex import ReflexApp
from Web_administracion.BK_ADM_PREV.BK_project_root.BK_IBS.BK_App.BK_2App import BK_2App
from Web_administracion.BK_ADM_PREV.BK_project_root.BK_IBS.BK_App.BK_3App import BK_3App
from Web_administracion.BK_ADM_PREV.BK_project_root.BK_IBS.BK_App.BK_4App import BK_4App
from Web_administracion.BK_ADM_PREV.BK_project_root.BK_IBS.BK_App.BK_5App import BK_5App

class MainApp(ReflexApp):
    def __init__(self):
            super().__init__()
                    self.title = "Main Menu"
                            self.sections = {
                                        "Usuarios": BK_2App(),
                                                    "Recursos": BK_3App(),
                                                                "Blockchain": BK_4App(),
                                                                            "Compresión": BK_5App()
                                                                                    }

                                                                                        def render(self):
                                                                                                return self.menu(self.sections)

                                                                                                if __name__ == "__main__":
                                                                                                    app = MainApp()
                                                                                                        app.run()
                                                                                                    