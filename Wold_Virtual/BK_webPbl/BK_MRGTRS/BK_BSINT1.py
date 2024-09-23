from flask import Flask
from flask_socketio import SocketIO
from Wold_Virtual.BK_webPbl.BK_MRGTRS.BK_BSINT2 import register_routes
from Wold_Virtual.BK_webPbl.BK_MRGTRS.BK_BSINT3 import handle_register, handle_delete_user

app = Flask(__name__)
socketio = SocketIO(app)

# Registrar rutas y eventos
register_routes(app, socketio)

if __name__ == '__main__':
    socketio.run(app, debug=True)