from usuarios import registrar_usuario, verificar_credenciales, manejar_accion
from recursos import RecursosUsuario, asignar_recursos_a_usuario, MonitoreoRecursos
from blockchain import Blockchain
from database import conectar_base_datos
from compresion import comprimir_y_guardar_datos, cargar_y_descomprimir_datos
from servidor import app, socketio

if __name__ == "__main__":
    # Aquí puedes iniciar la aplicación, el servidor, o cualquier otro componente
        app.run(debug=True)
            socketio.run(app)
