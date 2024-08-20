from usuarios import registrar_usuario, verificar_credenciales, manejar_accion
from recursos import RecursosUsuario, asignar_recursos_a_usuario, MonitoreoRecursos
from blockchain import Blockchain
from database import conectar_base_datos
from compresion import comprimir_y_guardar_datos, cargar_y_descomprimir_datos
from servidor import app, socketio

import app
import blockchain
import compresion
import database
import recursos
import servidor
import usuarios

def main():
        # Inicializar recursos
            recursos.inicializar()

        # Conectar a la base de datos
        db = database.conectar()

        # Crear un nuevo usuario
        usuario = usuarios.crear_usuario("nombre", "contraseña")

         # Ejecutar compresión de datos
        compresion.comprimir_datos(usuario.datos)

       # Procesar transacción en la blockchain
        blockchain.procesar_transaccion(usuario.transaccion)

    # Iniciar servidor
    servidor.iniciar()

 # Iniciar la aplicación principal
            app.ejecutar()

            if __name__ == "__main__":
            main()




if __name__ == "__main__":
    # Aquí puedes iniciar la aplicación, el servidor, o cualquier otro componente
        app.run(debug=True)
        socketio.run(app)
