# python_server/reflex_app.py
from reflex import Reflex

class MyApp(Reflex):
    def render(self):
            return """
                    <html>
                            <head>
                                        <title>Reflex App</title>
                                                </head>
                                                        <body>
                                                                    <h1>¡Hola desde Reflex!</h1>
                                                                                <p>Esta es una aplicación web creada con Reflex en Python.</p>
                                                                                        </body>
                                                                                                </html>
                                                                                                        """

                                                                                                        if __name__ == '__main__':
                                                                                                            app = MyApp()
                                                                                                                app.run()
                                                                                                            