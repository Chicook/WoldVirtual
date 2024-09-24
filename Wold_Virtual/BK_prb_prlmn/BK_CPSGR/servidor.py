from flask import Flask, render_template_string
from flask_socketio import SocketIO,
import reflex as rx

app = Flask(__name__)
socketio = SocketIO(app)

app = rx.App()

def layout():
    return rx.div(
        rx.header(
            rx.h1("Metaverso Crypto 3D", class_name="header"),
            class_name="header"
        ),
        rx.nav(
            rx.a("Inicio", href="./Metaverso_Crypto/inicio/Blockchain_Principal/secciones/inicio.html"),
            rx.a("Usuarios", href="#usuarios"),
            rx.a("Recursos", href="#recursos"),
            rx.a("Blockchain", href="#blockchain"),
            rx.a("Base de Datos", href="#database"),
            rx.a("Compresión", href="#compresion"),
            rx.a("Servidor", href="#servidor"),
            class_name="nav"
        ),
        rx.div(
            rx.section(
                rx.h2("Metaverso Crypto 3D descentralizado"),
                rx.p("Próximamente en esta página principal, se darán más detalles sobre el proyecto. Tenemos diferentes secciones que explicarán su función, dentro de cada módulo programado en Python."),
                id="home",
                class_name="section"
            ),
            rx.section(
                rx.h2("Usuarios"),
                rx.p("El módulo de usuarios permite registrar nuevos usuarios, verificar credenciales y manejar acciones específicas para cada usuario."),
                id="usuarios",
                class_name="section"
            ),
            rx.section(
                rx.h2("Recursos"),
                rx.p("El módulo de recursos gestiona la asignación de recursos como CPU y ancho de banda a los usuarios, y monitorea el uso de estos recursos."),
                id="recursos",
                class_name="section"
            ),
            rx.section(
                rx.h2("Blockchain"),
                rx.p("El módulo de blockchain permite crear y gestionar una cadena de bloques, añadiendo transacciones y validando la integridad de la cadena."),
                id="blockchain",
                class_name="section"
            ),
            rx.section(
                rx.h2("Base de Datos"),
                rx.p("El módulo de base de datos se encarga de conectar a una base de datos PostgreSQL, ejecutar consultas y manejar los resultados."),
                id="database",
                class_name="section"
            ),
            rx.section(
                rx.h2("Compresión"),
                rx.p("El módulo de compresión permite comprimir y guardar datos en archivos, así como cargar y descomprimir estos datos cuando sea necesario."),
                id="compresion",
                class_name="section"
            ),
            rx.section(
                rx.h2("Servidor"),
                rx.p("El módulo de servidor utiliza Flask y Socket.IO para manejar las rutas web y la transmisión de datos en tiempo real."),
                id="servidor",
                class_name="section"
            ),
            class_name="container"
        ),
        class_name="body"
    )
    
app.add_page(layout)
    
@socketio.on('audio_stream')
def handle_audio(data):
    socketio.emit('audio_stream', data)

if __name__ == '__main__':
   # app.run()
    socketio.run(app, debug=True)
