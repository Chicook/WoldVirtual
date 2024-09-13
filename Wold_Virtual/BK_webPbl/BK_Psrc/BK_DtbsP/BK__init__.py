# BK__init__.py
from .server import app as server_app
from .reflex_app import app as reflex_app
from .server import app as server_app
from .reflex_app import MyApp

def start_app():
    my_app = MyApp()
        server_app.run(debug=True)

        if __name__ == '__main__':
            start_app()

__all__ = ['server_app', 'reflex_app']

