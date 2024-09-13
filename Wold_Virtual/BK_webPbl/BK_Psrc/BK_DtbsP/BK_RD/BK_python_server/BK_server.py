# python_server/server.py
from flask import Flask, send_from_directory
# python_server/server.py
from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='../assets')

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder + '/html', 'index.html')

    if __name__ == '__main__':
        app.run(debug=True)
        

app = Flask(__name__, static_folder='../assets')

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder + '/html', 'index.html')

    @app.route('/unity3d/<path:path>')
    def serve_unity(path):
        return send_from_directory(app.static_folder + '/unity3d', path)

        if __name__ == '__main__':
            app.run(debug=True)
