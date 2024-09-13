# BK_pyth/server.py
from flask import Flask
from reflex_app import MyApp

app = Flask(__name__)

@app.route('/')
def index():
    return MyApp().render_home()

    @app.route('/section1')
    def section1():
        return MyApp().render_section1()

        @app.route('/section2')
        def section2():
            return MyApp().render_section2()

            if __name__ == '__main__':
                app.run(debug=True)
                