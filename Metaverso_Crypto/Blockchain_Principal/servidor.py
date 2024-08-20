import os
from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    """
    Renderiza la plantilla principal.
    """
    return render_template('index.html')

@socketio.on('audio_stream')
def handle_audio(data):
    """
    Maneja el evento de transmisión de audio.
    
    :param data: Datos de audio transmitidos.
    """
    socketio.emit('audio_stream', data)

if __name__ == 'main':
    socketio.run(app, debug=True)

# import os
# from flask import Flask, render_template
# from flask_socketio import SocketIO

# app = Flask(__name__)
# socketio = SocketIO(app)

# @app.route('/')
# def index():
   # return render_template('index.html')

  #  @socketio.on('audio_stream')
    # def handle_audio(data):
       # socketio.emit('audio_stream', data)

      #  if __name__ == '__main__':
           # socketio.run(app, debug=True)
