# bloque central de la plataforma #

#__version__ = "0.0.1"

#class MyCode:
    #def __init__(self):
        #pass

    #def run(self):
        print(f"Ejecutando la versión: {__version__}")

#if __name__ == "__main__":
    #my_code_instance = MyCode()
    #my_code_instance.run()

#import tkinter as tk
#import hashlib
from flask import Flask, request, jsonify, render_template, url_for, render_template_string
from web3 import Web3
import datetime
import time
import requests
import json
from threading import Thread
from flask_cors import CORS
from eth_account import Account
from flask_sockets import Sockets
from flask_mysqldb import MySQL
import jwt
from functools import wraps
import bpy
import random
import string
import re
import gzip
import http.server
import socketserver
import os
from flask_socketio import SocketIO
import zipfile
import psycopg2
import torch
import torchvision.models as models
import pytorch3d
from pytorch3d.transforms import Rotate, Translate
from pytorch3d.renderer import OpenGLPerspectiveCameras, RasterizationSettings, MeshRenderer, MeshRasterizer, SoftPhongShader
from torchvision.transforms import functional as F
from PIL import Image

# esto es solo un punto de partida #

usuarios = {}

def registrar_usuario(username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    usuarios[username] = hashed_password

def verificar_credenciales(username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return usuarios.get(username) == hashed_password

def manejar_accion(usuario, accion):
    if accion == "explorar":
        print(f"Bienvenido/a {usuario} al entorno de exploración.")
    elif accion == "intercambiar":
        print(f"Realizando intercambio para {usuario}.")
    else:
        print("Acción no reconocida.")

# Ejemplo de registro de usuario
registrar_usuario("usuario1", "contrasena_segura")

# Ejemplo de verificación de credenciales y manejo de entorno virtual
usuario_actual = "usuario1"
contrasena_ingresada = "contrasena_segura"

if verificar_credenciales(usuario_actual, contrasena_ingresada):
    print("Inicio de sesión exitoso")
    accion_usuario = "explorar"
    manejar_accion(usuario_actual, accion_usuario)
else:
    print("Credenciales incorrectas")
	
# Punto de partida #
# Instala las bibliotecas necesarias
# pip install torch torchvision pytorch3d

# Carga un modelo 3D base (ejemplo: una esfera)
mesh = pytorch3d.utils.create_sphere(radius=1.0, device='cuda')

# Carga un modelo de red neuronal para generar características faciales (ejemplo: ResNet)
facial_model = models.resnet18(pretrained=True)
facial_model = torch.nn.Sequential(*(list(facial_model.children())[:-1])).cuda()
facial_model.eval()

# Genera características faciales de una imagen (ejemplo: imagen facial) #

image_path = 'ruta/a/tu/imagen/facial.jpg'
input_image = Image.open(image_path).convert("RGB")
input_tensor = F.to_tensor(input_image).unsqueeze(0).cuda()
facial_features = facial_model(input_tensor)

# Combina las características faciales con el modelo 3D
# (aquí deberías implementar la lógica específica para tu caso)

# Configura cámaras y renderizador
cameras = OpenGLPerspectiveCameras(device='cuda')
raster_settings = RasterizationSettings(image_size=256, blur_radius=0.0, faces_per_pixel=1)
renderer = MeshRenderer(
    rasterizer=MeshRasterizer(cameras=cameras, raster_settings=raster_settings),
    shader=SoftPhongShader(device='cuda')
)

# Renderiza el avatar 3D
images = renderer(meshes_world=mesh, cameras=cameras)

# Visualiza el resultado
pytorch3d.vis.plot_image(images[0, ..., :3].cpu().numpy())

class RecursosUsuario:
    def __init__(self, porcentaje_cpu, porcentaje_ancho_banda):
        self.porcentaje_cpu = porcentaje_cpu
        self.porcentaje_ancho_banda = porcentaje_ancho_banda

def asignar_recursos_a_usuario(usuario, recursos_comunitarios):
    recursos_asignados = {
        'cpu': recursos_comunitarios['cpu'] * (usuario.porcentaje_cpu / 100),
        'ancho_banda': recursos_comunitarios['ancho_banda'] * (usuario.porcentaje_ancho_banda / 100),
    }
    return recursos_asignados

def monitorear_usuarios():
    # Implementa lógica de monitoreo para conocer el uso de recursos de cada usuario
    # Devuelve una estructura de datos con información sobre el uso de recursos

# Ejemplo de uso
usuarios = {
    'usuario1': RecursosUsuario(porcentaje_cpu=10, porcentaje_ancho_banda=20),
    'usuario2': RecursosUsuario(porcentaje_cpu=5, porcentaje_ancho_banda=15),
    # Agrega más usuarios según sea necesario
}

recursos_comunitarios = {
    'cpu': 100,  # Porcentaje basado en la capacidad total del servidor
    'ancho_banda': 1000,  # Medido en MB/s
}

for nombre_usuario, usuario in usuarios.items():
    recursos_asignados = asignar_recursos_a_usuario(usuario, recursos_comunitarios)
    print(f"Recursos asignados para {nombre_usuario}: {recursos_asignados}")

# Lógica de monitoreo (aquí es estática, debes implementar un sistema de monitoreo en tiempo real)
monitoreo = monitorear_usuarios()
print("Información de monitoreo de usuarios:")
print(monitoreo)

class MonitoreoRecursos:
    def __init__(self):
        self.recursos_usuarios = {}

    def actualizar_recursos(self, nombre_usuario, uso_cpu, uso_ancho_banda):
        self.recursos_usuarios[nombre_usuario] = {
            'uso_cpu': uso_cpu,
            'uso_ancho_banda': uso_ancho_banda
        }

    def obtener_informacion(self):
        return self.recursos_usuarios

# Función simulada para representar el uso de recursos por parte de un usuario
def simular_uso_recursos(nombre_usuario):
    # Simula el uso de CPU y ancho de banda de forma aleatoria (puedes reemplazar esto con datos reales)
    import random
    uso_cpu = random.uniform(0, 100)
    uso_ancho_banda = random.uniform(0, 100)
    return uso_cpu, uso_ancho_banda

# Ejemplo de uso
monitoreo = MonitoreoRecursos()

# Simula el monitoreo durante un período
for nombre_usuario in usuarios:
    uso_cpu, uso_ancho_banda = simular_uso_recursos(nombre_usuario)
    monitoreo.actualizar_recursos(nombre_usuario, uso_cpu, uso_ancho_banda)

# Obtiene la información de monitoreo
informacion_monitoreo = monitoreo.obtener_informacion()
print("Información de monitoreo de usuarios:")
print(informacion_monitoreo)

def conectar_base_datos():
    """
    Establece una conexión a la base de datos y ejecuta una consulta de ejemplo.
    """
    try:
        # Configuración de conexión
        conexion = psycopg2.connect(
            database="tu_base_datos",
            user="tu_usuario",
            password="tu_contraseña",
            host="tu_host",
            port="tu_puerto"
        )

        # Consulta de ejemplo
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM usuarios")
            resultados = cursor.fetchall()

            for resultado in resultados:
                print(resultado)

    except Exception as e:
        print(f"Error en la conexión a la base de datos: {e}")
    finally:
        if conexion:
            conexion.close()

# Llamada a la función
conectar_base_datos()

def comprimir_recursos():
    directorio_recursos = '/ruta/a/tus/recursos'
    archivo_zip = '/ruta/del/archivo/recursos.zip'

    with zipfile.ZipFile(archivo_zip, 'w') as zipf:
        for carpeta, subcarpetas, archivos in os.walk(directorio_recursos):
            for archivo in archivos:
                ruta_completa = os.path.join(carpeta, archivo)
                zipf.write(ruta_completa, os.path.relpath(ruta_completa, directorio_recursos))

def renderizar_recursos():
    archivo_zip = '/ruta/del/archivo/recursos.zip'
    directorio_destino = '/ruta/destino/para/recursos'

    with zipfile.ZipFile(archivo_zip, 'r') as zipf:
        zipf.extractall(directorio_destino)

# Llamadas a las funciones
comprimir_recursos()
renderizar_recursos()

app = Flask(__name__)

# Supongamos que tienes una instancia de la clase Blockchain #

class Blockchain:
    def __init__(self):
        self.chain = []  # Aquí guardas los bloques de tu cadena
	    
        # Otras inicializaciones y lógica de tu cadena de bloques #

    def obtener_informacion_cadena(self):
	    
        # Aquí implementas la lógica para obtener información de la cadena de bloques #
	    
        informacion = {
            'longitud': len(self.chain),
            'bloques': [block.__dict__ for block in self.chain],  
		
		# Convertir bloques a diccionarios #
            # Otra información relevante de tu cadena de bloques #
		
        }
        return informacion

# Creas una instancia de tu blockchain #

mi_blockchain = Blockchain()

# Ruta para obtener información de la cadena de bloques #

@app.route('/informacion_cadena', methods=['GET'])
def informacion_cadena():
    informacion = mi_blockchain.obtener_informacion_cadena()
    return jsonify(informacion), 200

if __name__ == '__main__':
    app.run(debug=True)

#  inicio del código #

# streaming de radio 📻 y tv 📺 #

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('audio_stream')
def handle_audio(data):
    # Procesa y transmite el audio a los clientes conectados
    socketio.emit('audio_stream', data)

if __name__ == '__main__':
    socketio.run(app, debug=True)

# servidor#

# Define el puerto en el que deseas ejecutar el servidor
PORT = 8000

# Obtén el directorio actual#

dir_path = os.path.dirname(os.path.realpath(__file__))

# Lee el contenido de los archivos HTML, CSS y JavaScript #

with open(os.path.join(dir_path, 'Wallet.html'), 'r') as file:
    html_content = file.read()

with open(os.path.join(dir_path, 'Wallet.css'), 'r') as file:
    css_content = file.read()

with open(os.path.join(dir_path, 'Wallet.js'), 'r') as file:
    js_content = file.read()

# Crea una instancia del manejador SimpleHTTPRequestHandler #

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            # Responde con el contenido de index.html
            self.send_response(200)
            self.send_header('Content-type', 'Wallet/html')
            self.end_headers()
            self.wfile.write(html_content.encode())
        elif self.path.endswith('.css'):
            # Responde con el contenido del archivo CSS solicitado
            self.send_response(200)
            self.send_header('Content-type', 'Wallet/css')
            self.end_headers()
            self.wfile.write(css_content.encode())
        elif self.path.endswith('.js'):
            # Responde con el contenido del archivo JavaScript solicitado
            self.send_response(200)
            self.send_header('Content-type', 'Wallet/javascript')
            self.end_headers()
            self.wfile.write(js_content.encode())
        else:
            # Utiliza el manejador predeterminado para otros tipos de archivos
            super().do_GET()

# Configura el servidor en el puerto especificado #

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print("Servidor en el puerto", PORT)
    
    # Establece el directorio raíz para el servidor
    os.chdir(dir_path)
    
    # Inicia el servidor
    httpd.serve_forever()
	    
app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu_clave_secreta'  # Reemplaza con una clave segura en un entorno de producción

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')  # Puedes obtener el token desde la solicitud, ajusta según tus necesidades

        if not token:
            return jsonify({'mensaje': 'Token faltante'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except jwt.ExpiredSignatureError:
            return jsonify({'mensaje': 'Token ha expirado'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'mensaje': 'Token inválido'}), 401

        return f(*args, **kwargs)

    return decorated

@app.route('/login')
def login():
    # Aquí verificarías las credenciales del usuario y, si son válidas, generas un token
    user = {'username': 'usuario_ejemplo'}
    token = jwt.encode({'user': user['username'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
    app.config['SECRET_KEY'])
    return jsonify({'token': token.decode('UTF-8')})

@app.route('/recurso_protgido')
@token_required
def recurso_protgido():
    return jsonify({'mensaje': 'Este es un recurso protegido'})

if __name__ == '__main__':
    app.run(debug=True)

app = Flask(__name__)

# Mock usuarios autorizados (por ejemplo, utiliza una base de datos en la implementación real)#

usuarios_autorizados = {'usuario1': 'clave1', 'usuario2': 'clave2'}

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')

        if not token:
            return jsonify({'mensaje': 'Token faltante'}), 401

        # Aquí deberías implementar la lógica de verificación del token
        usuario_valido = verificar_token(token)
        if not usuario_valido:
            return jsonify({'mensaje': 'Token inválido'}), 401

        return f(*args, **kwargs)

    return decorated

def verificar_token(token):
    # Aquí deberías implementar la lógica real de verificación del token
    return True  # Devuelve True si el token es válido

@app.route('/login')
def login():
    usuario = request.args.get('usuario')
    clave = request.args.get('clave')

    if usuario in usuarios_autorizados and usuarios_autorizados[usuario] == clave:
        token = generar_token(usuario)
        return jsonify({'token': token})
    else:
        return jsonify({'mensaje': 'Credenciales inválidas'}), 401

def generar_token(usuario):
    # Aquí deberías implementar la lógica real para generar el token
    return 'token_de_prueba'

@app.route('/recurso_protegido')
@token_required
def recurso_protegido():
    return jsonify({'mensaje': 'Este es un recurso protegido'})

if __name__ == '__main__':
    app.run(debug=True)
		
def comprimir_y_guardar_datos(datos, archivo_salida):
    datos_serializados = json.dumps(datos).encode('utf-8')
    datos_comprimidos = gzip.compress(datos_serializados)

    with open(archivo_salida, 'wb') as archivo:
        archivo.write(datos_comprimidos)

def cargar_y_descomprimir_datos(archivo_entrada):
    with open(archivo_entrada, 'rb') as archivo:
        datos_comprimidos = archivo.read()

    datos_descomprimidos = gzip.decompress(datos_comprimidos)
    return json.loads(datos_descomprimidos)

# Ejemplo de uso #

datos_isla_virtual = {
    "nombre": "Isla Encantada",
    "descripcion": "Una isla mágica creada por los usuarios",
    "objetos": [
        {"nombre": "Casa Principal", "tipo": "Edificio", "ubicacion": {"x": 10, "y": 5, "z": 8}},
        {"nombre": "Jardín de Flores", "tipo": "Área", "ubicacion": {"x": 15, "y": 7, "z": 10}}
    ]
}

# Escribir datos comprimidos #

comprimir_y_guardar_datos(datos_isla_virtual, 'isla_virtual_comprimida.gz')

# Cargar y descomprimir datos #

datos_recuperados = cargar_y_descomprimir_datos('isla_virtual_comprimida.gz')
print(datos_recuperados)
	
# Crear una instancia de la aplicación Flask #

app = Flask(__name__)

class ContratoMigracion:
    def __init__(self, contrato_actual, nuevo_contrato):
        self.contrato_actual = contrato_actual
        self.nuevo_contrato = nuevo_contrato

    def obtener_datos_para_migracion(self):
        # Implementar lógica para obtener datos del contrato actual
        datos_a_migrar = self.contrato_actual.obtener_datos()
        return datos_a_migrar

    def migrar_contratos(self, datos_a_migrar):
        try:
            # Implementar lógica de migración utilizando los datos obtenidos
            self.nuevo_contrato.migrar(datos_a_migrar)
            # Realizar otras acciones de migración si es necesario
            # ...

            print("Migración de contratos completada con éxito.")
        except Exception as e:
            print(f"Error durante la migración de contratos: {e}")

# Ejemplo de uso
contrato_actual = ContratoActual()  # Sustituir por tu implementación real
nuevo_contrato = NuevoContrato()    # Sustituir por tu implementación real

migrador = ContratoMigracion(contrato_actual, nuevo_contrato)
datos_a_migrar = migrador.obtener_datos_para_migracion()
migrador.migrar_contratos(datos_a_migrar)

@app.route('/migrar_contratos', methods=['POST'])
def endpoint_migrar_contratos():
    # Obtener los datos del contrato actual y el nuevo contrato desde la solicitud
    data = request.get_json()

    # Validar que los datos requeridos estén presentes
    if 'contrato_actual' not in data or 'nuevo_contrato' not in data:
        return jsonify({'mensaje': 'Datos insuficientes para la migración de contratos'}), 400

    # Obtener los contratos desde los datos #
	
    contrato_actual = data['contrato_actual']
    nuevo_contrato = data['nuevo_contrato']

    # Llamar a la función de migración de contratos #
	
    migrar_contratos(contrato_actual, nuevo_contrato)

    # Devolver una respuesta exitosa #
	
    return jsonify({'mensaje': 'Migración de contratos exitosa'})

# Incluir aquí otras rutas y funciones necesarias para la interoperabilidad

# Iniciar la aplicación Flask #

if __name__ == '__main__':
    app.run(debug=True)

class Blockchain:
    def __init__(self):
        self.current_key_version = 1
        self.key_rotation_interval = 30  # en segundos

    def generate_new_block(self):
	    
        # Lógica para generar un nuevo bloque
        # ...

    def rotate_keys(self):
        while True:
            time.sleep(self.key_rotation_interval)
            self.current_key_version += 1
            print(f"Rotación de claves: Nueva versión {self.current_key_version}")

    def run(self):
	    
        # Iniciar hilo para la rotación de claves en segundo plano #
	    
        rotation_thread = threading.Thread(target=self.rotate_keys, daemon=True)
        rotation_thread.start()

        try:
		
            # Tu lógica principal aquí (ej. generar bloques)
		
            while True:
                self.generate_new_block()
                time.sleep(5)  # Intervalo ficticio para la demostración
        except KeyboardInterrupt:
            print("Deteniendo la ejecución de la Blockchain.")

if __name__ == "__main__":
	
    # Crear una instancia de la Blockchain y ejecutarla #
	
    blockchain = Blockchain()
    blockchain.run()

app = Flask(__name__)

# ... (Importaciones ya realizadas en la primera parte del código) #

html_code = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blockchain Demo</title>
</head>
<body>
    <h1>Blockchain Demo</h1>
    
    <button onclick="generarNuevoBloque()">Generar Nuevo Bloque</button>
    <div id="resultado"></div>

    <script>
        function generarNuevoBloque() {
            fetch('http://localhost:5000/nuevo_bloque?prueba=123&hash_anterior=abc')
                .then(response => response.json())
                .then(data => {
                    document.getElementById('resultado').innerHTML = `<p>${data.mensaje}</p><pre>${JSON.stringify(data.bloque, null, 2)}</pre>`;
                })
                .catch(error => console.error('Error:', error));
        }
    </script>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(html_code)

# Inicializar la blockchain
mi_blockchain = Blockchain()  # Asegúrate de adaptar esto según la estructura de tu código

# Implementar endpoints de Flask para interactuar con la blockchain
@app.route('/nuevo_bloque', methods=['GET'])
def nuevo_bloque():
    prueba = request.args.get('prueba')  # Ajusta según tus necesidades
    hash_anterior = request.args.get('hash_anterior')
    
    nuevo_bloque = mi_blockchain.nuevo_bloque(prueba, hash_anterior)
    respuesta = {'mensaje': 'Nuevo bloque creado', 'bloque': nuevo_bloque}
    return jsonify(respuesta), 200

# Define más endpoints según lo que necesites #

if __name__ == '__main__':
	
    # Ejecutar la blockchain en un hilo separado #
	
    blockchain_thread = threading.Thread(target=mi_blockchain.ejecutar)
    blockchain_thread.start()

    # Ejecutar Flask en el hilo principal #
	
    app.run(port=5000)
	
class NFT:
    def __init__(self, id_unica=None, nombre=None, coordenadas=None, propietario=None):
        if id_unica and nombre and coordenadas:
            # Caso 1: Crear un NFT con propiedades específicas
            self.id_unica = id_unica
            self.nombre = nombre
            self.coordenadas = coordenadas
            self.propietario = propietario
            self.timestamp_creacion = time.time()
            self.hash = self.calcular_hash()
        elif id_unica and propiedades:
            # Caso 2: Crear un NFT con un diccionario de propiedades
            self.id_unica = id_unica
            self.propiedades = propiedades
        else:
            raise ValueError("No se proporcionaron propiedades suficientes para crear el NFT")

    def calcular_hash(self):
        datos_codificados = str(self.id_unica) + str(self.nombre) + str(self.coordenadas) + str(self.propietario) + str(self.timestamp_creacion)
        return hashlib.sha256(datos_codificados.encode('utf-8')).hexdigest()

# Caso 1: Crear una isla como NFT único con propiedades específicas #

isla1_nft = NFT(id_unica="ID_ISLA_1", nombre="Isla 1", coordenadas="Coordenadas XYZ")

# Acceder a las propiedades de la isla #

print(f"Isla: {isla1_nft.nombre}, Ubicación: {isla1_nft.coordenadas}")

# Acceder al hash único generado #

print(f"Hash único: {isla1_nft.hash}")

# Caso 2: Crear una isla como NFT único con un diccionario de propiedades #

isla2_nft = NFT(id_unica="ID_ISLA_2", propiedades={"nombre": "Isla 2", "ubicacion": "Coordenadas XYZ"})

# Guardar la isla en una lista o estructura de datos similar #

islas_nfts = [isla1_nft, isla2_nft]

# Acceder a las propiedades de las islas #

for isla_nft in islas_nfts:
    if hasattr(isla_nft, 'nombre') and hasattr(isla_nft, 'coordenadas'):
        print(f"Isla: {isla_nft.nombre}, Ubicación: {isla_nft.coordenadas}")
    elif hasattr(isla_nft, 'propiedades'):
        nombre = isla_nft.propiedades.get('nombre', 'Nombre no disponible')
        ubicacion = isla_nft.propiedades.get('ubicacion', 'Ubicación no disponible')
        print(f"Isla: {nombre}, Ubicación: {ubicacion}")

# ... (Importaciones ya realizadas en la primera parte del código) #

class GeneradorAvatar:
    def __init__(self):
        self.colores = ['rojo', 'azul', 'verde', 'amarillo', 'naranja']
        self.formas = ['círculo', 'cuadrado', 'triángulo', 'estrella', 'corazón']
        self.elementos = ['gafas', 'sombrero', 'barba', 'bigote', 'pendientes']

    def generar_avatar(self):
        color = random.choice(self.colores)
        forma = random.choice(self.formas)
        elemento = random.choice(self.elementos)
        nombre = ''.join(random.choices(string.ascii_letters, k=8))  # Uso de random.choices para mayor claridad
        avatar_info = f"Avatar de {nombre}: {color}, {forma}, con {elemento}"
        return avatar_info

class Sincronizador:

    def __init__(self, estado_inicial="Inicial"):
        self.estado = estado_inicial

    def obtener_estado(self):
        return self.estado

    def actualizar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

# Uso del GeneradorAvatar #

generador = GeneradorAvatar()
avatar_generado = generador.generar_avatar()
print(avatar_generado)

# Uso del Sincronizador #

sincronizador = Sincronizador()

estado_inicial = sincronizador.obtener_estado()
print(f"Estado Inicial: {estado_inicial}")

nuevo_estado = "Conectado a Unity"
sincronizador.actualizar_estado(nuevo_estado)
print(f"Nuevo Estado: {sincronizador.obtener_estado()}")

# Para trabajar en blender #

# Borra todos los objetos en la escena #

bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

# Crear un suelo cuadrado de color azul metálico #

bpy.ops.mesh.primitive_plane_add(size=10, enter_editmode=False, align='WORLD', location=(0, 0, 0))
bpy.ops.object.shade_smooth()

# Crear y asignar material #

material = bpy.data.materials.new(name="BlueMetallic")
material.use_nodes = True
bsdf = material.node_tree.nodes.new(type='ShaderNodeBsdfPrincipled')
bsdf.base_color = (0, 0, 1, 1)  # Color azul
bsdf.metallic = 1  # Superficie metálica
bpy.context.object.data.materials.append(material)

# Configurar la vista de la cámara #

bpy.ops.object.camera_add(enter_editmode=False, align='VIEW', location=(0, 0, 5), rotation=(0, 0, 0))
camera = bpy.context.object
bpy.ops.object.select_by_type(type='CAMERA')
bpy.context.scene.camera = bpy.context.selected_objects[0]

# Configurar la iluminación #

bpy.ops.object.light_add(type='SUN', radius=1, align='WORLD', location=(5, 5, 5))
light = bpy.context.object

class Bloque:
    def __init__(self, index, timestamp, datos, hash_anterior):
        self.index = index
        self.timestamp = timestamp
        self.datos = datos
        self.hash_anterior = hash_anterior
        self.nonce = 0
        self.hash = self.calcular_hash()

    def minar_bloque(self, dificultad):
        while self.hash[:dificultad] != '0' * dificultad:
            self.nonce += 1
            self.hash = self.calcular_hash()

    def calcular_hash(self):
        datos_codificados = f"{self.index}{self.timestamp}{self.datos}{self.hash_anterior}{self.nonce}"
        return hashlib.sha256(datos_codificados.encode('utf-8')).hexdigest()

class Blockchain:
    def __init__(self):
        self.cadena = []
        self.transacciones = []
        self.mutex = threading.Lock()

    def agregar_bloque(self, datos):
        with self.mutex:
            indice = len(self.cadena) + 1
            timestamp = time.time()
            hash_anterior = self.obtener_hash_anterior()
            nuevo_bloque = Bloque(indice, timestamp, datos, hash_anterior)
            self.transacciones = []  # Reiniciar lista de transacciones actuales
            self.cadena.append(nuevo_bloque)
            return nuevo_bloque

    def obtener_hash_anterior(self):
        return self.cadena[-1].hash if self.cadena else "1"  # Bloque génesis

    def imprimir_cadena(self):
        with self.mutex:
            for bloque in self.cadena:
                print(f"Índice: {bloque.index}, Hash: {bloque.hash}")

# Ejemplo de uso #

blockchain = Blockchain()
blockchain.agregar_bloque("Datos del bloque 1")
blockchain.imprimir_cadena()

# ... (Importaciones ya realizadas en la primera parte del código)

def minar_bloques(blockchain, dificultad, datos, num_bloques=5, tiempo_entre_minado=2):
    for _ in range(num_bloques):
        bloque = blockchain.agregar_bloque(datos)
        bloque.minar_bloque(dificultad)
        print(f"Bloque minado - Índice: {bloque.index}, Hash: {bloque.hash}")
        time.sleep(tiempo_entre_minado)

# Ejemplo de uso #

blockchain = Blockchain()

# Crear dos threads para minar bloques simultáneamente #

thread1 = threading.Thread(target=minar_bloques, args=(blockchain, 2, "Transacción 1"))
thread2 = threading.Thread(target=minar_bloques, args=(blockchain, 2, "Transacción 2"))

# Iniciar los threads #

thread1.start()
thread2.start()

# Esperar a que ambos threads terminen #

thread1.join()
thread2.join()

# Imprimir la cadena después de la minería simultánea #

blockchain.imprimir_cadena()

class Transaccion:
    def __init__(self, remitente, destinatario, cantidad, tipo_moneda):
        self.remitente = remitente
        self.destinatario = destinatario
        self.cantidad = cantidad
        self.tipo_moneda = tipo_moneda

class Usuario:
    def __init__(self, direccion, saldo):
        self.direccion = direccion
        self.saldo = saldo

class PlataformaBlockchain:
    def __init__(self):
        self.usuarios = []
        self.transacciones = []

    def validar_direccion(self, direccion):
        return re.match(r'^[a-fA-F0-9]{40}$', direccion) is not None

    def autenticar_usuario(self, direccion):
	    
        # Implementa la lógica de autenticación según tus necesidades #
	    
        return True

    def agregar_usuario(self, direccion, saldo):
        if self.validar_direccion(direccion):
            nuevo_usuario = Usuario(direccion, saldo)
            self.usuarios.append(nuevo_usuario)
        else:
            print("Dirección no válida. Asegúrate de que sigue el formato correcto.")

    def realizar_transaccion(self, remitente, destinatario, cantidad, tipo_moneda):
        if not self.validar_direccion(remitente) or not self.validar_direccion(destinatario):
            print("Dirección de remitente o destinatario no válida.")
            return False
		
        # Implementa la lógica para realizar la transacción según tus necesidades #
	    
        nueva_transaccion = Transaccion(remitente, destinatario, cantidad, tipo_moneda)
        self.transacciones.append(nueva_transaccion)
        print("Transacción realizada con éxito.")
        return True

        if not self.autenticar_usuario(remitente):
            print("Autenticación de remitente fallida.")
            return False

        remitente_obj = next((u for u in self.usuarios if u.direccion == remitente), None)
        if remitente_obj and remitente_obj.saldo >= cantidad:
            remitente_obj.saldo -= cantidad
            destinatario_obj = next((u for u in self.usuarios if u.direccion == destinatario), None)
            if destinatario_obj:
                destinatario_obj.saldo += cantidad
                nueva_transaccion = Transaccion(remitente, destinatario, cantidad, tipo_moneda)
                self.transacciones.append(nueva_transaccion)
                return True

        print("Transacción fallida. Fondos insuficientes o dirección no encontrada.")
        return False

# Ejemplo de uso #

plataforma = PlataformaBlockchain()
plataforma.agregar_usuario("direccion_usuario1", 100)
plataforma.agregar_usuario("direccion_usuario2", 50)

# Lógica básica de transferencia #

resultado = plataforma.realizar_transaccion("direccion_usuario1", "direccion_usuario2", 10, "WoldcoinVirtual")
if resultado:
    print("Transacción exitosa")
    for usuario in plataforma.usuarios:
        print(f"Dirección: {usuario.direccion}, Saldo: {usuario.saldo}")
    for transaccion in plataforma.transacciones:
        print(f"De: {transaccion.remitente}, A: {transaccion.destinatario}, Cantidad: {transaccion.cantidad}, Moneda: {transaccion.tipo_moneda}")
else:
    print("Transacción fallida. Fondos insuficientes o dirección no válida.")

class ContratoIngresoCripto:
    def __init__(self, web3, contrato_address, propietario_address):
        self.web3 = web3
        self.contrato_address = contrato_address
        self.propietario_address = propietario_address
        # Asumiendo que ya tienes el ABI del contrato compilado
        self.contrato = self.web3.eth.contract(address=self.contrato_address, abi=ABI_CONTRATO_INGRESO)

    def depositar(self, cantidad):
        # Asumiendo que el contrato tiene la función 'depositar' y el token es ERC-20
        # Debes ajustar esto según tu contrato real
        transaccion = {
            'from': self.propietario_address,
            'gas': 200000,
            'gasPrice': self.web3.toWei('50', 'gwei'),
        }
        self.contrato.functions.depositar(cantidad).transact(transaccion)
        print(f"Depósito de {cantidad} realizado por {self.propietario_address}")

    # Otros métodos según las funciones de tu contrato...#

# Uso en la aplicación #

cadena_bloques = CadenaBloques()
contrato_ingreso = ContratoIngresoCripto(cadena_bloques.web3, 'DIRECCION_DEL_CONTRATO', 'DIRECCION_DEL_PROPIETARIO')

# Ejemplo de depósito #

cantidad_a_depositar = 10  # Ajusta según tu caso
contrato_ingreso.depositar(cantidad_a_depositar)

# Código de la aplicación...#

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu_clave_secreta'  # Reemplaza con una clave segura en un entorno de producción

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')  # Puedes obtener el token desde la solicitud, ajusta según tus necesidades

        if not token:
            return jsonify({'mensaje': 'Token faltante'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except jwt.ExpiredSignatureError:
            return jsonify({'mensaje': 'Token ha expirado'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'mensaje': 'Token inválido'}), 401

        return f(*args, **kwargs)

    return decorated

@app.route('/login')
def login():
    # Aquí verificarías las credenciales del usuario y, si son válidas, generas un token
    user = {'username': 'usuario_ejemplo'}
    token = jwt.encode({'user': user['username'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
    app.config['SECRET_KEY'])
    return jsonify({'token': token.decode('UTF-8')})

@app.route('/recurso_protgido')
@token_required
def recurso_protgido():
    return jsonify({'mensaje': 'Este es un recurso protegido'})

if __name__ == '__main__':
    app.run(debug=True)
	
# Direcciones y claves privadas (actualiza según tus necesidades) #

# estas addres key son solo ejemplos #

contract_address = '0x123456789ABCDEF123456789ABCDEF123456789A'
sender_address = '0x987654321ABCDEF987654321ABCDEF9876543210'
private_key = 'tu_clave_privada'
abi = [...]  # Coloca aquí el ABI del contrato NFT

app = Flask(__name__)

# Conexión a la blockchain #

web3 = Web3(Web3.HTTPProvider('tu_url_de_ethereum'))

def connect_to_blockchain():
    if web3.isConnected():
        print("Conexión exitosa con la blockchain")
    else:
        print("Error: No se pudo conectar a la blockchain")

# Función para mintear un nuevo NFT #

def mint_avatar_nft(owner_address):
    try:
        contract.functions.mintAvatarNFT(owner_address).transact({
            'from': sender_address,
            'gas': 200000,
            'gasPrice': web3.toWei('50', 'gwei'),
            'nonce': web3.eth.getTransactionCount(sender_address),
            'privateKey': private_key,
        })

        print(f"NFT creado exitosamente para el avatar: {owner_address}")
        return "Acción completada en la blockchain"
    except Exception as e:
        print(f"Error en la transacción al mintear NFT: {e}")
        return "Error en la transacción"

# Función para obtener la información de un NFT #

def get_nft_info(token_id):
    try:
        info = contract.functions.getNFTInfo(token_id).call()
        return {'owner': info[0], 'metadata': info[1]}  # Ajusta según la estructura real de tu contrato
    except Exception as e:
        print(f"Error al obtener información del NFT: {e}")
        return {'error': 'Error al obtener información del NFT'}

# Otras funciones y lógica...#


if __name__ == '__main__':
    connect_to_blockchain()
    app.run(debug=True)


# partes a mejorar., red propia en wallets como metamask #

@app.route('/network_config', methods=['GET'])
def get_network_config():
    try:
        network_config = {
            'chainId': 1337,
            'chainName': 'My Development Chain',
            'rpcUrls': ['http://localhost:8545'],
            'nativeCurrency': {'name': 'WoldcoinVirtual', 'symbol': 'WV', 'decimals': 18},
            'blockExplorerUrls': ['http://localhost:8545']
        }
        return jsonify(network_config)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    connect_thread = Thread(target=connect_to_blockchain)
    connect_thread.start()

    app.run(debug=True)
	
class InterfazEmpresa:
    def __init__(self, master):
        self.master = master
        master.title("Interfaz Empresa")

        # Etiqueta para mostrar porcentajes de recursos #
	    
        self.etiqueta_porcentajes = tk.Label(master, text="Porcentajes de Recursos:")
        self.etiqueta_porcentajes.pack()

        # Mostrar porcentajes en una etiqueta (puedes personalizar esto según tu lógica)#
	    
        porcentaje_procesador = 80
        porcentaje_discos_duros = 60
        porcentaje_tarjetas_graficas = 75
        porcentaje_memoria_ram = 90
        porcentaje_ancho_banda = 50

        texto_porcentajes = f"Procesador: {porcentaje_procesador}%\nDiscos Duros: {porcentaje_discos_duros}%\nTarjetas Gráficas: {porcentaje_tarjetas_graficas}%\nMemoria RAM: {porcentaje_memoria_ram}%\nAncho de Banda: {porcentaje_ancho_banda}%"
        self.etiqueta_porcentajes_info = tk.Label(master, text=texto_porcentajes)
        self.etiqueta_porcentajes_info.pack()

        # Botón para obtener detalles de la cadena de bloques#
	    
        self.boton_detalle_cadena = tk.Button(master, text="Detalles de la Cadena de Bloques", command=self.mostrar_detalles_cadena)
        self.boton_detalle_cadena.pack()

    def mostrar_detalles_cadena(self):
	    
        # Aquí puedes agregar la lógica para obtener y mostrar detalles de la cadena de bloques#
	    
        detalles_cadena = "Detalles de la Cadena de Bloques:\n(Información detallada aquí)"
	    
        # Puedes mostrar los detalles en una nueva ventana, etiquetas, o personalizar según tus necesidades#
	    
	 tk.messagebox.showinfo("Detalles de la Cadena de Bloques", detalles_cadena)

# Crear la ventana principal para la interfaz de la empresa #

root_empresa = tk.Tk()
interfaz_empresa = InterfazEmpresa(root_empresa)

# Mantener la ventana abierta #

root_empresa.mainloop()

class InterfazCompartirRecursos:
    def __init__(self, master):
        self.master = master
        master.title("Compartir Recursos")

        # Campos para el procesador #
	    
        self.etiqueta_procesador = tk.Label(master, text="Procesador:")
        self.etiqueta_procesador.pack()
        self.entry_procesador = tk.Entry(master)
        self.entry_procesador.pack()

        # Campos para discos duros #
	    
        self.etiqueta_discos_duros = tk.Label(master, text="Discos Duros:")
        self.etiqueta_discos_duros.pack()
        self.entry_discos_duros = tk.Entry(master)
        self.entry_discos_duros.pack()

        # Campos para tarjetas gráficas #
	    
        self.etiqueta_tarjetas_graficas = tk.Label(master, text="Tarjetas Gráficas:")
        self.etiqueta_tarjetas_graficas.pack()
        self.entry_tarjetas_graficas = tk.Entry(master)
        self.entry_tarjetas_graficas.pack()

        # Campos para memoria RAM #
	    
        self.etiqueta_memoria_ram = tk.Label(master, text="Memoria RAM:")
        self.etiqueta_memoria_ram.pack()
        self.entry_memoria_ram = tk.Entry(master)
        self.entry_memoria_ram.pack()

        # Campos para ancho de banda #
	    
        self.etiqueta_ancho_banda = tk.Label(master, text="Ancho de Banda:")
        self.etiqueta_ancho_banda.pack()
        self.entry_ancho_banda = tk.Entry(master)
        self.entry_ancho_banda.pack()

        # Botón para compartir recursos #
	    
        self.boton_compartir = tk.Button(master, text="Compartir Recursos", command=self.compartir_recursos)
        self.boton_compartir.pack()

    def compartir_recursos(self):
        # Obtener los valores de los campos #
	    
        procesador = self.entry_procesador.get()
        discos_duros = self.entry_discos_duros.get()
        tarjetas_graficas = self.entry_tarjetas_graficas.get()
        memoria_ram = self.entry_memoria_ram.get()
        ancho_banda = self.entry_ancho_banda.get()

        # Aquí puedes realizar las acciones necesarias para agregar los recursos a la cadena de bloques #
	    
        print(f"Recursos compartidos - Procesador: {procesador}, Discos Duros: {discos_duros}, Tarjetas Gráficas: {tarjetas_graficas}, Memoria RAM: {memoria_ram}, Ancho de Banda: {ancho_banda}")

# Crear la ventana principal#

root = tk.Tk()
interfaz = InterfazCompartirRecursos(root)

# Supongamos que en la blockchain de la plataforma tienes información sobre usuarios y recursos #
# pendiente de seguir desarrollando #
usuarios_recursos_blockchain = {
    'usuario1': {
        'cpu': 10,
        'ancho_banda': 50,
    },
    'usuario2': {
        'cpu': 5,
        'ancho_banda': 30,
    },
    # ... más usuarios y recursos
}

# Supongamos que en el servidor descentralizado comunitario también tienes información sobre usuarios y recursos
usuarios_recursos_servidor = {
    'usuario1': {
        'cpu': 8,
        'ancho_banda': 40,
    },
    'usuario2': {
        'cpu': 6,
        'ancho_banda': 25,
    },
    # ... más usuarios y recursos
}

# Supongamos que en el metaverso Crypto tienes una clase para manejar la conexión

class ConexionMetaverso:
    def __init__(self):
        self.usuarios_recursos_blockchain = {}
        self.usuarios_recursos_servidor = {}

    def conectar_blockchain(self, usuarios_recursos_blockchain):
        self.usuarios_recursos_blockchain = usuarios_recursos_blockchain

    def conectar_servidor(self, usuarios_recursos_servidor):
        self.usuarios_recursos_servidor = usuarios_recursos_servidor

    def obtener_recursos_usuario(self, nombre_usuario):
        recursos_blockchain = self.usuarios_recursos_blockchain.get(nombre_usuario, {})
        recursos_servidor = self.usuarios_recursos_servidor.get(nombre_usuario, {})

        # Combina los recursos de la blockchain y el servidor
        recursos_combinados = {
            'cpu': min(recursos_blockchain.get('cpu', 0), recursos_servidor.get('cpu', 0)),
            'ancho_banda': min(recursos_blockchain.get('ancho_banda', 0), recursos_servidor.get('ancho_banda', 0)),
        }

        return recursos_combinados

# Crear una instancia de la clase ConexionMetaverso en el servidor descentralizado
conexion_metaverso = ConexionMetaverso()

# Conectar los recursos desde la blockchain
conexion_metaverso.conectar_blockchain(usuarios_recursos_blockchain)

# Conectar los recursos desde el servidor descentralizado
conexion_metaverso.conectar_servidor(usuarios_recursos_servidor)

# En el metaverso Crypto, puedes obtener los recursos de un usuario específico
nombre_usuario_buscar = 'usuario1'
recursos_obtenidos = conexion_metaverso.obtener_recursos_usuario(nombre_usuario_buscar)

# Ahora puedes usar los recursos obtenidos para la renderización u otras operaciones
print(f"Recursos del usuario {nombre_usuario_buscar}: {recursos_obtenidos}")

# Mantener la ventana abierta#

root.mainloop()

app = Flask(__name__)

# Diccionario para almacenar los saldos de los usuarios en la versión demo #

saldos_demo = {}

# Ruta para que los usuarios vean su saldo en la versión demo #

@app.route('/ver_saldo_demo/<usuario>')
def ver_saldo_demo(usuario):
    saldo = saldos_demo.get(usuario, 0)
    return f"Saldo en la versión demo para {usuario}: {saldo}"

# Ruta para que los usuarios migren a la versión de producción #

@app.route('/migrar/<usuario>')
def migrar(usuario):
    saldo_demo = saldos_demo.get(usuario, 0)

    # Realizar acciones necesarias para verificar la validez de la migración
    # ...

    # Ejemplo: Proceso de migración #
	
    saldo_comercial = saldo_demo  # En la realidad, aquí deberías quemar tokens de prueba y emitir tokens comerciales

    return f"Migración exitosa. Saldo en la versión comercial para {usuario}: {saldo_comercial}"

if __name__ == '__main__':
    app.run(debug=True)

# seccion opensim. # visor web #

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Plataforma Principal</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
            }
            h1 {
                color: #333;
            }
        </style>
    </head>
    <body>
        <h1>Bienvenido a la Plataforma Principal</h1>
    </body>
    </html>
    """)

@app.route('/viewer')
def viewer():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Visor OpenSim</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
            }
            h1 {
                color: #333;
            }
            #opensim-viewer {
                border: 1px solid #ccc;
                padding: 20px;
                margin: 20px;
            }
        </style>
        <script>
            document.addEventListener('DOMContentLoaded', function() {
                console.log('El visor de OpenSim se ha cargado');
                // Puedes agregar más código según las necesidades del visor
            });
        </script>
    </head>
    <body>
        <h1>Visor OpenSim</h1>
        <div id="opensim-viewer">
            <!-- Aquí podrías agregar elementos para mostrar el visor -->
        </div>
    </body>
    </html>
    """)

if __name__ == '__main__':
    app.run(debug=True)

app = Flask(__name__)

@app.route('/')
def index():
    # CSS y JavaScript incluidos directamente en el código Python
    contenido_html = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Título de la Página</title>
        
        <style>
            body {
                background-color: #f4f4f4;
                font-family: Arial, sans-serif;
            }

            h1 {
                color: #333;
            }

            /* Agrega más estilos según tus necesidades */
        </style>

        <script>
            // Tu código JavaScript aquí
            function saludar() {
                alert("¡Hola desde JavaScript!");
            }

            // Agrega más funciones según tus necesidades
        </script>
    </head>
    <body>
        <h1>Hola Mundo</h1>
        
        <!-- Contenido del cuerpo del HTML -->

        <button onclick="saludar()">Saludar</button>
    </body>
    </html>
    """

    return render_template_string(contenido_html)

if __name__ == '__main__':
    app.run(debug=True)

app = Flask(__name__)

# Configuración MySQL y otras funciones #

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'base_datos'
conexion = MySQL(app)

@app.before_request
def before_request():
    print("Antes de la petición...")

@app.after_request
def after_request(response):
    print("Después de la petición")
    return response

# Estructura HTML para index.html #

html_index = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ data.titulo }}</title>
</head>
<body>
    <h1>{{ data.bienvenida }}</h1>
    <p>Número de cursos: {{ data.numero_cursos }}</p>
    <ul>
        {% for curso in data.cursos %}
            <li>{{ curso.nombre }}</li>
        {% endfor %}
    </ul>
</body>
</html>
"""

# Estructura HTML para contacto.html #

html_contacto = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ data.titulo }}</title>
</head>
<body>
    <h1>{{ data.titulo }}</h1>
    <p>Nombre: {{ data.nombre }}</p>
    <p>Edad: {{ data.edad }}</p>
</body>
</html>
"""

@app.route('/')
def index():
    cursos = ['PHP', 'Python', 'Java', 'Kotlin', 'Dart', 'JavaScript']
    data = {
        'titulo': 'Index123',
        'bienvenida': '¡Saludos!',
        'cursos': cursos,
        'numero_cursos': len(cursos)
    }
    return render_template_string(html_index, data=data)

@app.route('/contacto/<nombre>/<int:edad>')
def contacto(nombre, edad):
    data = {
        'titulo': 'Contacto',
        'nombre': nombre,
        'edad': edad
    }
    return render_template_string(html_contacto, data=data)

def query_string():
    print(request)
    print(request.args)
    print(request.args.get('param1'))
    print(request.args.get('param2'))
    return "Ok"

@app.route('/cursos')
def listar_cursos():
    data = {}
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT codigo, nombre, creditos FROM curso ORDER BY nombre ASC"
        cursor.execute(sql)
        cursos = cursor.fetchall()
        data['cursos'] = cursos
        data['mensaje'] = 'Exito'
    except Exception as ex:
        data['mensaje'] = 'Error...'
    return jsonify(data)

def pagina_no_encontrada(error):
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.add_url_rule('/query_string', view_func=query_string)
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True, port=5000)

app = Flask(__name__)

# Mockup de datos de blockchain #

blockchain_data = {
    'owner_address': '0x123456789ABCDEF123456789ABCDEF123456789A',
    'contract_address': '0x987654321ABCDEF987654321ABCDEF9876543210',
    'private_key': 'tu_clave_privada',
    'abi': [...]  # Coloca aquí el ABI del contrato NFT
}

# Funciones de la blockchain (métodos mockup)#

def mint_avatar_nft(owner_address): 
	
    # Implementa la lógica real aquí (llamada a la función mintAvatarNFT)#
	
    print(f"NFT creado exitosamente para el avatar: {owner_address}")
    return "Acción completada en la blockchain"

def transfer_avatar_nft(owner_address, to_address, token_id):
    # Implementa la lógica real aquí (llamada a la función transferNFT)#
	
    print(f"NFT transferido exitosamente de {owner_address} a {to_address}")
    return "Acción completada en la blockchain"

# Rutas de la interfaz web#

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mint_nft', methods=['POST'])
def mint_nft():
    owner_address = request.form.get('owner_address')
    result = mint_avatar_nft(owner_address)
    return result

@app.route('/transfer_nft', methods=['POST'])
def transfer_nft():
    owner_address = request.form.get('owner_address')
    to_address = request.form.get('to_address')
    token_id = request.form.get('token_id')
    result = transfer_avatar_nft(owner_address, to_address, token_id)
    return result

if __name__ == '__main__':
    app.run(debug=True)
	
app = Flask(__name__)
sockets = Sockets(app)

# Lista de usuarios conectados
usuarios_conectados = []

# Función para enviar mensajes a todos los usuarios#

def enviar_mensaje(mensaje):
    for usuario in usuarios_conectados:
        try:
            usuario['cliente'].send(jsonify({'mensaje': mensaje}))
        except:
            pass

# Ruta principal que renderiza la interfaz web#

@app.route('/')
def index():
    return render_template('index.html')

# Ruta para que los usuarios se conecten al servidor#

@sockets.route('/conectar')
def conectar(ws):
    usuarios_conectados.append({'cliente': ws})
    print('Nuevo usuario conectado.')

    while not ws.closed:
        mensaje = ws.receive()
        if mensaje:
            print(f"Mensaje recibido: {mensaje}")
            enviar_mensaje(mensaje)

if __name__ == '__main__':
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler

    server = pywsgi.WSGIServer(('localhost', 5000), app, handler_class=WebSocketHandler)
    print("Servidor iniciado en http://localhost:5000")
    server.serve_forever()

app = Flask(__name__)
CORS(app)

@app.route('/network_config', methods=['GET'])
def get_network_config():
    # Define los detalles de tu blockchain de desarrollo
    network_config = {
        'chainId': 1337,  # Cambia esto según tu configuración
        'chainName': 'woldbkvirtual',
        'rpcUrls': ['http://localhost:8545'],  # Cambia la URL según tu nodo RPC
        'nativeCurrency': {'name': 'WoldcoinVirtual', 'symbol': 'Wcv', 'decimals': 3},
        'blockExplorerUrls': ['http://localhost:8545']  # Cambia la URL según tu explorador de bloques
    }
    return jsonify(network_config)

if __name__ == '__main__':
    app.run(debug=True)

web3 = Web3(Web3.HTTPProvider('tu_url_de_ethereum'))

# Direcciones y claves privadas (actualiza según tus necesidades)
contract_address = '0x123456789ABCDEF123456789ABCDEF123456789A'
sender_address = '0x987654321ABCDEF987654321ABCDEF9876543210'
private_key = 'tu_clave_privada'
abi = [...]  # Coloca aquí el ABI del contrato NFT

# Contrato NFT
contract = web3.eth.contract(address=contract_address, abi=abi)

# Conexión a la blockchain
def connect_to_blockchain():
    try:
        if web3.isConnected():
            print("Conexión exitosa con la blockchain")
        else:
            print("Error: No se pudo conectar a la blockchain")
    except Exception as e:
        print(f"Error en la conexión a la blockchain: {e}")
    finally:
        # Cierra la conexión si es necesario
        # web3.close()

# Función para mintear un nuevo NFT
def mint_avatar_nft(owner_address):
    try:
        transaction = contract.functions.mintAvatarNFT(owner_address).buildTransaction({
            'from': sender_address,
            'gas': 200000,
            'gasPrice': web3.toWei('50', 'gwei'),
            'nonce': web3.eth.getTransactionCount(sender_address),
        })

        signed_transaction = web3.eth.account.signTransaction(transaction, private_key)
        tx_hash = web3.eth.sendRawTransaction(signed_transaction.rawTransaction)
        print(f"Transacción exitosa. Hash: {tx_hash.hex()}")
    except Exception as e:
        print(f"Error al mintear NFT: {e}")

# Cierra la conexión al finalizar el programa
# web3.close()

        web3.eth.waitForTransactionReceipt(tx_hash)
# Función para mintear un nuevo NFT
def mint_avatar_nft(owner_address):
    try:
        # Construir la transacción para mintear un NFT
        transaction = contract.functions.mintAvatarNFT(owner_address).buildTransaction({
            'from': sender_address,
            'gas': 200000,
            'gasPrice': web3.toWei('50', 'gwei'),
            'nonce': web3.eth.getTransactionCount(sender_address),
        })

        # Firmar y enviar la transacción
        signed_transaction = web3.eth.account.signTransaction(transaction, private_key)
        tx_hash = web3.eth.sendRawTransaction(signed_transaction.rawTransaction)

        # Esperar a la confirmación de la transacción
        web3.eth.waitForTransactionReceipt(tx_hash)

        print(f"NFT creado exitosamente para el avatar: {owner_address}")
        return "Acción completada en la blockchain"
    except Exception as e:
        print(f"Error al mintear NFT: {e}")
        return "Error en la transacción"

# Función para transferir un NFT
def transfer_avatar_nft(owner_address, to_address, token_id):
    try:
        # Construir la transacción para transferir un NFT
        transaction = contract.functions.transferNFT(to_address, token_id).buildTransaction({
            'from': owner_address,
            'gas': 200000,
            'gasPrice': web3.toWei('50', 'gwei'),
            'nonce': web3.eth.getTransactionCount(owner_address),
        })

        # Firmar y enviar la transacción
        signed_transaction = web3.eth.account.signTransaction(transaction, private_key)
        tx_hash = web3.eth.sendRawTransaction(signed_transaction.rawTransaction)

        # Esperar a la confirmación de la transacción
        web3.eth.waitForTransactionReceipt(tx_hash)

        print(f"NFT transferido exitosamente de {owner_address} a {to_address}")
        return "Acción completada en la blockchain"
    except Exception as e:
        print(f"Error en la transferencia de NFT: {e}")
        return "Error en la transacción"

        signed_transaction = web3.eth.account.signTransaction(transaction, private_key)
        tx_hash = web3.eth.sendRawTransaction(signed_transaction.rawTransaction)

        web3.eth.waitForTransactionReceipt(tx_hash)

        print(f"NFT transferido exitosamente de {owner_address} a {to_address}")
        return "Acción completada en la blockchain"
    except Exception as e:
        print(f"Error en la transacción: {e}")
        return "Error en la transacción"

# Supongamos que estas funciones representan eventos en OpenSim que se activan al mover el avatar
def avatar_moved_to_location(location):
    # Lógica para manejar el evento de movimiento del avatar
    special_action_triggered(owner_address)

def avatar_reached_transfer_location(owner_address, to_address, token_id):
    # Lógica para manejar el evento cuando el avatar llega a la ubicación de transferencia
    transfer_nft_triggered(owner_address, to_address, token_id)

# Supongamos que estas funciones se activan en respuesta a eventos en OpenSim
def handle_avatar_events():
    # Lógica para manejar eventos del avatar en OpenSim
    # Por ejemplo, detectar ubicaciones y activar funciones correspondientes

    # Supongamos que el avatar se mueve a una ubicación específica
    avatar_moved_to_location("UbicacionA")

    # Supongamos que el avatar llega a la ubicación de transferencia
    avatar_reached_transfer_location(owner_address, to_address, token_id)

# Conexión a la blockchain al inicio
connect_to_blockchain()

# Supongamos que esto se ejecuta continuamente para manejar eventos del avatar
while True:
    handle_avatar_events()
    # Otros procesos y lógica en OpenSim

web3 = Web3(Web3.HTTPProvider('tu_url_de_ethereum'))

# Direcciones y claves privadas (actualiza según tus necesidades)
contract_address = '0x123456789ABCDEF123456789ABCDEF123456789A'
sender_address = '0x987654321ABCDEF987654321ABCDEF9876543210'
private_key = 'tu_clave_privada'

# (opcional) # abi = [...]  # Coloca aquí el ABI del contrato NFT

# Contrato NFT

contract = web3.eth.contract(address=contract_address, abi=abi)

# Conexión a la blockchain
def connect_to_blockchain():
    if web3.isConnected():
        print("Conexión exitosa con la blockchain")
    else:
        print("Error: No se pudo conectar a la blockchain")

# Función para mintear un nuevo NFT
def mint_avatar_nft(owner_address):
    try:
        transaction = contract.functions.mintAvatarNFT(owner_address).buildTransaction({
            'from': sender_address,
            'gas': 200000,
            'gasPrice': web3.toWei('50', 'gwei'),
            'nonce': web3.eth.getTransactionCount(sender_address),
        })

        signed_transaction = web3.eth.account.signTransaction(transaction, private_key)
        tx_hash = web3.eth.sendRawTransaction(signed_transaction.rawTransaction)

        web3.eth.waitForTransactionReceipt(tx_hash)

        print(f"NFT creado exitosamente para el avatar: {owner_address}")
        return "Acción completada en la blockchain"
    except Exception as e:
        print(f"Error en la transacción: {e}")
        return "Error en la transacción"

# Función para transferir un NFT
def transfer_avatar_nft(owner_address, to_address, token_id):
    try:
        transaction = contract.functions.transferNFT(to_address, token_id).buildTransaction({
            'from': owner_address,
            'gas': 200000,
            'gasPrice': web3.toWei('50', 'gwei'),
            'nonce': web3.eth.getTransactionCount(owner_address),
        })

        signed_transaction = web3.eth.account.signTransaction(transaction, private_key)
        tx_hash = web3.eth.sendRawTransaction(signed_transaction.rawTransaction)

        web3.eth.waitForTransactionReceipt(tx_hash)

        print(f"NFT transferido exitosamente de {owner_address} a {to_address}")
        return "Acción completada en la blockchain"
    except Exception as e:
        print(f"Error en la transacción: {e}")
        return "Error en la transacción"

# Conexión a la blockchain al inicio
connect_to_blockchain()

# Supongamos que esto se activa cuando un avatar realiza una acción especial en OpenSim
def special_action_triggered(owner_address):
    print("Acción especial en OpenSim detectada.")
    mint_avatar_nft(owner_address)

# Supongamos que esto se activa cuando un avatar decide transferir su NFT a otra dirección
def transfer_nft_triggered(owner_address, to_address, token_id):
    print(f"Transferencia de NFT iniciada desde {owner_address} a {to_address}.")
    transfer_avatar_nft(owner_address, to_address, token_id)

web3 = Web3(Web3.HTTPProvider('tu_url_de_ethereum'))

# Contrato NFT
contract_address = '0x123456789ABCDEF123456789ABCDEF123456789A'
sender_address = '0x987654321ABCDEF987654321ABCDEF9876543210'
private_key = 'tu_clave_privada'

# (opcional) # abi = [...]  # Coloca aquí el ABI del contrato NFT

# Contrato NFT
contract = web3.eth.contract(address=contract_address, abi=abi)

# Función para mintear un nuevo NFT
# Función para mintear un nuevo NFT
def mint_avatar_nft(owner_address):
    try:
        # Construir la transacción para mintear un NFT
        transaction = contract.functions.mintAvatarNFT(owner_address).buildTransaction({
            'from': sender_address,
            'gas': 200000,
            'gasPrice': web3.toWei('50', 'gwei'),
            'nonce': web3.eth.getTransactionCount(sender_address),
        })

        # Firmar y enviar la transacción
        signed_transaction = web3.eth.account.signTransaction(transaction, private_key)
        tx_hash = web3.eth.sendRawTransaction(signed_transaction.rawTransaction)

        # Esperar a la confirmación de la transacción
        web3.eth.waitForTransactionReceipt(tx_hash)

        print(f"NFT creado exitosamente para el avatar: {owner_address}")
        return "Acción completada en la blockchain"
    except Exception as e:
        print(f"Error en la transacción al mintear NFT: {e}")
        return "Error en la transacción"

# Función para transferir un NFT
def transfer_avatar_nft(owner_address, to_address, token_id):
    try:
        transaction = contract.functions.transferNFT(to_address, token_id).buildTransaction({
            'from': owner_address,
            'gas': 200000,
            'gasPrice': web3.toWei('50', 'gwei'),
            'nonce': web3.eth.getTransactionCount(owner_address),
        })

        signed_transaction = web3.eth.account.signTransaction(transaction, private_key)
        tx_hash = web3.eth.sendRawTransaction(signed_transaction.rawTransaction)

        web3.eth.waitForTransactionReceipt(tx_hash)

        print(f"NFT transferido exitosamente de {owner_address} a {to_address}")
        return "Acción completada en la blockchain"
    except Exception as e:
        print(f"Error en la transacción: {e}")
        return "Error en la transacción"

# Supongamos que esto se activa cuando un avatar realiza una acción especial en OpenSim
def special_action_triggered(owner_address):
    mint_avatar_nft(owner_address)

# Supongamos que esto se activa cuando un avatar decide transferir su NFT a otra dirección
def transfer_nft_triggered(owner_address, to_address, token_id):
    transfer_avatar_nft(owner_address, to_address, token_id)

web3 = Web3(Web3.HTTPProvider('tu_url_de_ethereum'))

# Contrato NFT
contract_address = '0x123456789ABCDEF123456789ABCDEF123456789A'
sender_address = '0x987654321ABCDEF987654321ABCDEF9876543210'
private_key = 'tu_clave_privada'
abi = [...]  # Coloca aquí el ABI del contrato NFT

# Contrato NFT
contract = web3.eth.contract(address=contract_address, abi=abi)

# Función para mintear un nuevo NFT
# Contrato NFT
contract_address = '0x123456789ABCDEF123456789ABCDEF123456789A'
sender_address = '0x987654321ABCDEF987654321ABCDEF9876543210'
private_key = 'tu_clave_privada'
abi = [...]  # Coloca aquí el ABI del contrato NFT

# Conectarse a una red de Ethereum (puede ser una red de prueba o la red principal)
web3 = Web3(Web3.HTTPProvider('tu_url_de_ethereum'))

# Configuración de la blockchain y contrato NFT
contract_address = '0x123456789ABCDEF123456789ABCDEF123456789A'
sender_address = '0x987654321ABCDEF987654321ABCDEF9876543210'
private_key = 'tu_clave_privada'
abi = [...]  # Coloca aquí el ABI del contrato NFT

# Instanciar el contrato NFT después de la conexión
contract = web3.eth.contract(address=contract_address, abi=abi)

# Función para mintear un nuevo NFT
def mint_avatar_nft(owner_address):
    try:
        # Construir la transacción para mintear un NFT
        transaction = contract.functions.mintAvatarNFT(owner_address).buildTransaction({
            'from': sender_address,
            'gas': 200000,
            'gasPrice': web3.toWei('50', 'gwei'),
            'nonce': web3.eth.getTransactionCount(sender_address),
        })

        # Firmar y enviar la transacción
        signed_transaction = web3.eth.account.signTransaction(transaction, private_key)
        tx_hash = web3.eth.sendRawTransaction(signed_transaction.rawTransaction)

        # Esperar a la confirmación de la transacción
        web3.eth.waitForTransactionReceipt(tx_hash)

        print(f"NFT creado exitosamente para el avatar: {owner_address}")
        return "Acción completada en la blockchain"
    except Exception as e:
        print(f"Error en la transacción al mintear NFT: {e}")
        return "Error en la transacción"

def special_action_triggered(owner_address):
    mint_avatar_nft(owner_address)

def perform_blockchain_action(location):
    try:
        contract_address = '0x123456789ABCDEF123456789ABCDEF123456789A'
        sender_address = '0x987654321ABCDEF987654321ABCDEF9876543210'
        private_key = 'tu_clave_privada'
        abi = [...]  # Coloca aquí el ABI del contrato inteligente
        contract = web3.eth.contract(address=contract_address, abi=abi)

        transaction = contract.functions.performAction(location).buildTransaction({
            'from': sender_address,
            'gas': 200000,
            'gasPrice': web3.toWei('50', 'gwei'),
            'nonce': web3.eth.getTransactionCount(sender_address),
        })

        signed_transaction = web3.eth.account.signTransaction(transaction, private_key)
        tx_hash = web3.eth.sendRawTransaction(signed_transaction.rawTransaction)

        web3.eth.waitForTransactionReceipt(tx_hash)

        print(f"Acción en la blockchain realizada exitosamente en la ubicación: {location}")
        return "Acción completada en la blockchain"
    except Exception as e:
        print(f"Error en la transacción en la blockchain: {e}")
        return "Error en la transacción"


app = Flask(__name__)

# Endpoint para recibir solicitudes desde OpenSim
@app.route('/opensim-interaction', methods=['POST'])
def opensim_interaction():
    data = request.get_json()

    if "action" in data and data["action"] == "avatar_moved":
        location = data.get("location", "")
        if location:
            # Lógica para realizar acciones en la blockchain según la ubicación del avatar
            blockchain_action_result = perform_blockchain_action(location)

            # Devolver una respuesta a OpenSim
            response = {"status": "success", "message": "Interacción exitosa en la blockchain"}
            return jsonify(response)
        else:
            return jsonify({"status": "error", "message": "Falta la ubicación en la solicitud"})

    return jsonify({"status": "error", "message": "Acción no reconocida"})

def perform_blockchain_action(location):
    # Lógica para realizar acciones en la blockchain según la ubicación del avatar
    # Puedes invocar contratos inteligentes, realizar transacciones, etc.
    # Implementa esta función según los detalles de tu blockchain
    print(f"Realizando acción en la blockchain para la ubicación: {location}")
    # Aquí puedes agregar la lógica específica de tu blockchain
    return "Acción completada en la blockchain"

if __name__ == '__main__':
    # Iniciar el servidor Flask en segundo plano
    server_thread = Thread(target=app.run, kwargs={'port': 5000})
    server_thread.start()

    # Simular solicitud desde OpenSim
    url = 'http://localhost:5000/opensim-interaction'
    data = {"action": "avatar_moved", "location": "Coordenadas_X_Y_Z"}

    response = requests.post(url, json=data)

    if response.status_code == 200:
        result = response.json()
        print(result)
    else:
        print("Error en la solicitud:", response.status_code)

    # Detener el servidor Flask al finalizar
    server_thread.join()

app = Flask(__name__)

# Endpoint para recibir solicitudes desde OpenSim
@app.route('/opensim-interaction', methods=['POST'])
def opensim_interaction():
    data = request.get_json()

    # Procesar la solicitud y realizar acciones en tu blockchain
    # Aquí puedes llamar a funciones relacionadas con contratos inteligentes, por ejemplo

    # Devolver una respuesta a OpenSim
    response = {"status": "success", "message": "Interacción exitosa"}
    return jsonify(response)

if __name__ == '__main__':
    # Iniciar el servidor Flask en segundo plano
    from threading import Thread
    server_thread = Thread(target=app.run, kwargs={'port': 5000})
    server_thread.start()

    # Simular solicitud desde OpenSim
    url = 'http://localhost:5000/opensim-interaction'
    data = {"key": "value"}  # Puedes ajustar los datos según tus necesidades

    response = requests.post(url, json=data)

    if response.status_code == 200:
        result = response.json()
        print(result)
    else:
        print("Error en la solicitud:", response.status_code)

    # Detener el servidor Flask al finalizar
    server_thread.join()

class Minero:

def __init__(self, blockchain):
        self.blockchain = blockchain

    def minar_bloque(self, datos, espacio_reservado=None):
        nuevo_bloque = Bloque(
            index=len(self.blockchain.bloques) + 1,
            timestamp=time.time(),
            datos=datos,
            hash_anterior=self.blockchain.bloques[-1].hash,
            espacio_reservado=espacio_reservado
        )

        self.proof_of_work(nuevo_bloque)
        self.blockchain.agregar_bloque(nuevo_bloque)

    def proof_of_work(self, bloque):
        while bloque.hash[:4] != "0000":
            bloque.nonce += 1
            bloque.hash = bloque.calcular_hash()

    def proof_of_space(self, espacio_reservado_actual, espacio_reservado_nuevo):
        """
        Verificar si el nuevo espacio reservado es mayor al actual.

        :param espacio_reservado_actual: Espacio reservado actual
        :param espacio_reservado_nuevo: Espacio reservado nuevo
        :return: True si es válido, False si no lo es
        """
        return espacio_reservado_nuevo > espacio_reservado_actual

# Uso de la clase CadenaBloques y Minero
mi_blockchain = CadenaBloques()
mi_minero = Minero(mi_blockchain)
datos_del_bloque = "Datos importantes"
espacio_reservado_actual = "espacio_anterior"  # Reemplaza esto con tu implementación real de espacio reservado

# Minar un bloque con datos y espacio reservado
mi_minero.minar_bloque(datos_del_bloque, espacio_reservado_actual)

class Bloque:

# Clase Bloque

    def __init__(self):
        # Inicialización del bloque

    # Otras funciones del bloque...


	    
    def minar_bloque(self, dificultad):
        while self.hash[:dificultad] != '0' * dificultad:
            self.nonce += 1
            self.hash = self.calcular_hash()

    def calcular_hash(self):
        datos_codificados = str(self.index) + str(self.timestamp) + str(self.datos) + str(self.hash_anterior)
        return hashlib.sha256(datos_codificados.encode('utf-8')).hexdigest()

    def __init__(self, index, timestamp, datos, hash_anterior, resource_logs=None, compensacion=None):
        self.index = index
        self.timestamp = timestamp
        self.datos = datos
        self.hash_anterior = hash_anterior
        self.nonce = 0
        self.hash = self.calcular_hash()
        self.resource_logs = resource_logs or []
        self.compensacion = compensacion

class CadenaBloques:

    def __init__(self):
        self.cadena = []

    def agregar_bloque(self, nuevo_bloque):
        self.cadena.append(nuevo_bloque)

# Uso del GeneradorAvatar y la CadenaBloques
generador_avatar = GeneradorAvatar()
cadena_bloques = CadenaBloques()

for i in range(5):  # Generar 5 avatares y agregar a la cadena de bloques
    avatar_info = generador_avatar.generar_avatar()
    timestamp = datetime.now()
    hash_anterior = cadena_bloques.cadena[-1].hash if cadena_bloques.cadena else "1"
    nuevo_bloque = Bloque(len(cadena_bloques.cadena) + 1, timestamp, avatar_info, hash_anterior)
    cadena_bloques.agregar_bloque(nuevo_bloque)

# Imprimir la cadena de bloques
for bloque in cadena_bloques.cadena:
    print(f"Índice: {bloque.index}, Timestamp: {bloque.timestamp}, Avatar: {bloque.avatar_info}, Hash: {bloque.hash}")

    def nuevo_bloque(self, proof, previous_hash=None, resource_logs=None):
        nuevo_bloque = Bloque(
            index=len(self.bloques) + 1,
            timestamp=time.time(),
            datos=self.transacciones,
            hash_anterior=previous_hash or self.hash(self.bloques[-1]) if self.bloques else "1",
            resource_logs=resource_logs
        )
        self.transacciones = []
        self.bloques.append(nuevo_bloque)
        return nuevo_bloque

    def validar_prueba(self, prev_proof, proof, hash_anterior):
        guess = f'{prev_proof}{proof}{hash_anterior}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    def __init__(self, blockchain):
        self.blockchain = blockchain

    def minar_bloque(self, datos, resource_logs=None):
        if not self.validar_recursos(resource_logs):
            print("Registros de recursos inválidos. No se puede minar el bloque.")
            return

        compensacion = self.calcular_compensacion(resource_logs)
        nuevo_bloque = Bloque(
            index=len(self.blockchain.bloques) + 1,
            timestamp=time.time(),
            datos=datos,
            hash_anterior=self.blockchain.bloques[-1].hash,
            resource_logs=resource_logs,
            compensacion=compensacion
        )

        self.proof_of_work(nuevo_bloque)
        self.blockchain.agregar_bloque(nuevo_bloque)

    def proof_of_work(self, bloque):
        while bloque.hash[:4] != "0000":
            bloque.nonce += 1
            bloque.hash = bloque.calcular_hash()

    def validar_recursos(self, resource_logs):
        return all(log['amount'] > 0 for log in resource_logs)

    def calcular_compensacion(self, resource_logs):
        return sum(log['amount'] for log in resource_logs)

# Uso de la clase CadenaBloques y Minero
mi_blockchain = CadenaBloques()
mi_minero = Minero(mi_blockchain)
datos_del_bloque = "Datos importantes"
registros_de_recursos = [{'user': 'Alice', 'amount': 5, 'timestamp': time.time()}]

mi_minero.minar_bloque(datos_del_bloque, registros_de_recursos)

    def __init__("self, blockchain"):
        self.blockchain = blockchain

    def minar_bloque("self, datos"):
        nuevo_bloque = Bloque(len("self.blockchain.cadena"), time.time(), datos, self.blockchain.cadena[-1].hash)
        self.proof_of_work("nuevo_bloque")
        self.blockchain.agregar_bloque("nuevo_bloque")

    def proof_of_work("self, bloque"):
        while bloque.hash[:4] != "0000":
            bloque.marca_tiempo = time.time()
            bloque.hash = bloque.generar_hash()

# Crear una instancia de la cadena de bloques y del minero
mi_blockchain = Blockchain()
minero = Minero(mi_blockchain)

# Minar un bloque
minero.minar_bloque("Datos del bloque 1")

class blokchain:

     def minar_bloque("self, datos"):
        nuevo_bloque = Bloque(
            index=len(self.cadena),
            timestamp=time.time(),
            datos=datos,
            hash_anterior=self.cadena[-1].hash
        )
        nuevo_bloque.proof_of_work()
        self.cadena.append("nuevo_bloque")

# Uso de la función para minar un bloque
datos_a_guardar = "Datos importantes"
mi_blockchain.minar_bloque("datos_a_guardar")

    def validar_cadena("self"):
        for i in range("1, len"("self.cadena")):
            bloque_actual = self.cadena[i]
            bloque_anterior = self.cadena[i - 1]

            if bloque_actual.hash != bloque_actual.generar_hash():
                return False

            if bloque_actual.hash_anterior != bloque_anterior.hash:
                return False

        return True

# Uso de la función para validar la cadena
if mi_blockchain.validar_cadena():
    print("La cadena de bloques es válida.")
else:
    print("La cadena de bloques no es válida. ¡Alerta de manipulación!")

     def minar_bloque(self, datos):
        nuevo_bloque = Bloque(
            index=len(self.bloques),
            datos=datos,
            timestamp=time(),
            hash_anterior=self.bloques[-1].hash,
        )

        nuevo_bloque.proof_of_work(self.dificultad)
        self.bloques.append(nuevo_bloque)

      def __init__(self):
        self.cadena = []
        self.agregar_bloque(self.crear_bloque_genesis())

    def crear_bloque_genesis(self):
        return Bloque(0, time.time(), "Bloque Génesis", "0")

    def agregar_bloque(self, nuevo_bloque):
        nuevo_bloque.hash_anterior = self.cadena[-1].hash
        self.cadena.append(nuevo_bloque)

# Crear una instancia de la cadena de bloques
mi_blockchain = Blockchain()

app = Flask("__name__")
class InterfazCompartirRecursos:
    def __init__("self, master"):
        self.master = master
        master.title("Compartir Recursos")

        self.etiqueta = tk.Label(master, text="Ingrese la información del recurso:")
        self.etiqueta.pack()

        self.etiqueta_nombre = tk.Label(master, text="Nombre:")
        self.etiqueta_nombre.pack()

        self.entry_nombre = tk.Entry(master)
        self.entry_nombre.pack()

        self.etiqueta_descripcion = tk.Label(master, text="Descripción:")
        self.etiqueta_descripcion.pack()

        self.entry_descripcion = tk.Entry(master)
        self.entry_descripcion.pack()

        self.boton_compartir = tk.Button(master, text="Compartir Recurso", command=self.compartir_recurso)
        self.boton_compartir.pack()
	    
    def compartir_recurso(self):
        nombre = self.entry_nombre.get()
        descripcion = self.entry_descripcion.get()

        # Aquí puedes realizar las acciones necesarias para agregar el recurso a la cadena de bloques
        print(f"Recurso compartido - Nombre: {nombre}, Descripción: {descripcion}")

# Crear la ventana principal
root = tk.Tk()
interfaz = InterfazCompartirRecursos(root)

# Mantener la ventana abierta
root.mainloop()

# Blokchain.py

class ContratoA:
    def __init__(self):
        # Lógica del contrato A
        pass

class ContratoB:
    def __init__(self):
        # Lógica del contrato B
        pass

class Blokchain:
    def __init__(self):
        self.contratoA = ContratoA()
        self.contratoB = ContratoB()

    # Puedes agregar funciones adicionales o lógica específica aquí

# Ejemplo de uso
blokchain = Blokchain()

class BlockchainInteraction:
    def __init__(self, node_url, contract_address, contract_abi):
        self.w3 = Web3(Web3.HTTPProvider(node_url))
        self.token_ico_address = contract_address
        self.token_ico_abi = contract_abi
        self.token_ico_contract = self.w3.eth.contract(address=self.token_ico_address, abi=self.token_ico_abi)

    def check_owner(self):
        owner = self.token_ico_contract.functions.owner().call()
        print("Dueño del contrato TokenICO:", owner)

    def purchase_tokens(self, amount):
        transaction_hash = self.token_ico_contract.functions.purchaseTokens(amount).transact({'from': self.w3.eth.accounts[0]})
        print("Compra de tokens realizada. Transaction Hash:", transaction_hash)

    def run_cli(self):
        print("CLI para interactuar con contratos inteligentes")
        while True:
            print("1. Verificar dueño del contrato")
            print("2. Comprar tokens")
            print("0. Salir")
            choice = input("Ingrese su elección: ")

            if choice == "1":
                self.check_owner()
            elif choice == "2":
                amount_to_purchase = int(input("Ingrese la cantidad de tokens a comprar: "))
                self.purchase_tokens(amount_to_purchase)
            elif choice == "0":
                break
            else:
                print("Opción no válida. Inténtelo de nuevo.")


if __name__ == "__main__":
    node_url = 'http://localhost:8545'  # Reemplaza con tu propia URL
    contract_address = "0xYourTokenICOAddress"
    contract_abi = [...]  # Reemplaza con el ABI de tu contrato

    blockchain_interaction = BlockchainInteraction(node_url, contract_address, contract_abi)
    blockchain_interaction.run_cli()
	
web3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

# Configuración del contrato inteligente en Solidity
contract_source_code = """

//este es un ejemplo de contrato solidity//
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

contract WoldcoinVirtual {
        string public name = "WoldcoinVirtual";
            string public symbol = "WCV";
                uint8 public decimals = 3;
                    uint256 public totalSupply = 30000000 * (10 ** uint256(decimals));
                        address public owner;
                            uint256 public commission = 1 * (10 ** uint256(decimals - 3)); // 0.001 tokens

                                mapping(address => uint256) public balanceOf;
                                    mapping(address => mapping(address => uint256)) public allowance;
                                        mapping(address => uint256) public stakedBalance;
                                            mapping(address => uint256) public stakedTimestamp;

                                                event Transfer(address indexed from, address indexed to, uint256 value);
                                                    event Approval(address indexed owner, address indexed spender, uint256 value);
                                                        event Staked(address indexed user, uint256 amount);
                                                            event Unstaked(address indexed user, uint256 amount);

                                                                constructor() {
                                                                            owner = msg.sender;
                                                                                    balanceOf[msg.sender] = totalSupply;
                                                                }

                                                                    modifier onlyOwner() {
                                                                                require(msg.sender == owner, "Only owner can call this function");
                                                                                        _;
                                                                    }

                                                                        function transfer(address to, uint256 value) public returns (bool) {
                                                                                    require(to != address(0), "Invalid address");
                                                                                            require(balanceOf[msg.sender] >= value, "Insufficient balance");

                                                                                                    uint256 fee = (value * commission) / (10 ** uint256(decimals));
                                                                                                            uint256 netValue = value - fee;

                                                                                                                    balanceOf[msg.sender] -= value;
                                                                                                                            balanceOf[to] += netValue;
                                                                                                                                    balanceOf[owner] += fee;

                                                                                                                                            emit Transfer(msg.sender, to, netValue);
                                                                                                                                                    emit Transfer(msg.sender, owner, fee);

                                                                                                                                                            return true;
                                                                        }

                                                                            function approve(address spender, uint256 value) public returns (bool) {
                                                                                        allowance[msg.sender][spender] = value;
                                                                                                emit Approval(msg.sender, spender, value);
                                                                                                        return true;
                                                                            }

                                                                                function transferFrom(address from, address to, uint256 value) public returns (bool) {
                                                                                            require(from != address(0), "Invalid address");
                                                                                                    require(to != address(0), "Invalid address");
                                                                                                            require(balanceOf[from] >= value, "Insufficient balance");
                                                                                                                    require(allowance[from][msg.sender] >= value, "Allowance exceeded");

                                                                                                                            uint256 fee = (value * commission) / (10 ** uint256(decimals));
                                                                                                                                    uint256 netValue = value - fee;

                                                                                                                                            balanceOf[from] -= value;
                                                                                                                                                    balanceOf[to] += netValue;
                                                                                                                                                            balanceOf[owner] += fee;
                                                                                                                                                                    allowance[from][msg.sender] -= value;

                                                                                                                                                                            emit Transfer(from, to, netValue);
                                                                                                                                                                                    emit Transfer(from, owner, fee);

                                                                                                                                                                                            return true;
                                                                                }

                                                                                    function stake(uint256 amount) public returns (bool) {
                                                                                                require(amount > 0, "Amount must be greater than zero");
                                                                                                        require(balanceOf[msg.sender] >= amount, "Insufficient balance");

                                                                                                                balanceOf[msg.sender] -= amount;
                                                                                                                        stakedBalance[msg.sender] += amount;
                                                                                                                                stakedTimestamp[msg.sender] = block.timestamp;

                                                                                                                                        emit Staked(msg.sender, amount);

                                                                                                                                                return true;
                                                                                    }

                                                                                        function unstake(uint256 amount) public returns (bool) {
                                                                                                    require(amount > 0, "Amount must be greater than zero");
                                                                                                            require(stakedBalance[msg.sender] >= amount, "Insufficient staked balance");
                                                                                                                    require(block.timestamp >= stakedTimestamp[msg.sender] + 1 days, "Staking duration not met");

                                                                                                                            stakedBalance[msg.sender] -= amount;
                                                                                                                                    balanceOf[msg.sender] += amount;
                                                                                                                                            stakedTimestamp[msg.sender] = 0;

                                                                                                                                                    emit Unstaked(msg.sender, amount);

                                                                                            return true;
    }
}

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/access/AccessControl.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@pancakeswap/pancake-swap-lib/contracts/token/BEP20/IBEP20.sol";


contract  Micontrato{

using SafeMath for uint256;
using SafeERC20 for IERC20;
    using SafeMath for uint256;
    using SafeERC20 for IERC20;
event Deposit(address indexed user, uint256 amount);
    event Withdrawal(address indexed user, uint256 amount);
        event EmergencyWithdrawal(address indexed user, uint256 amount);

constructor(){
    btcbAddress = 0x7130d2A12B9BCbFAe4f2634d864A1Ee1Ce3Ead9c;
    allowedWallet = 0xA8E670588bbB447c1e98557C64f740016d908085;
    name = "WoldcoinVirtual";
    symbol = "WCV";
    decimals = 3;
    totalSupply = 30000000;  
}
  function transfer(address to, uint256 amount) external {
    require(amount > 0, "Amount must be greater than 0");
    require(balanceOf[msg.sender] >= amount, "Insufficient balance");

    balanceOf[msg.sender] -= amount;
    balanceOf[to] += amount;

    emit Transfer(msg.sender, to, amount);
  }

event Transfer(address indexed from, address indexed to, uint256 amount);
bytes32 public constant ADMIN_ROLE = keccak256("ADMIN_ROLE");
using SafeMath for uint256;
using SafeERC20 for IERC20;
 address public btcbAddress = 0x7130d2A12B9BCbFAe4f2634d864A1Ee1Ce3Ead9c;
 address public allowedWallet
=0xA8E670588bbB447c1e98557C64f740016d908085;
string public name = "WoldcoinVirtual";
 string public symbol = "WCV";
 uint8 public decimals = 3;
uint256 public totalSupply = 30000000  ;
mapping(address => uint256) public balanceOf;
    mapping(address => uint256) public liquidityPool;
    event LiquidityAdded(address indexed provider, uint256 amount);
    event LiquidityRemoved(address indexed provider, uint256 amount);
    function addLiquidity(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        balanceOf[msg.sender] -= amount;
        totalSupply += amount;
        liquidityPool[msg.sender] += amount;
        emit LiquidityAdded(msg.sender, amount);
    }
    function removeLiquidity(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(liquidityPool[msg.sender] >= amount, "Insufficient liquidity");
        balanceOf[msg.sender] += amount;
        totalSupply -= amount;
        liquidityPool[msg.sender] -= amount;

        emit LiquidityRemoved(msg.sender, amount);
        }
    event LiquidityAddedWithBTCB(address indexed provider, uint256 amount);
    function getTokenPrice() external view returns (uint256) {
    }
}

contract sueldo {
    address public owner;
    mapping(address => uint256) public salaries;

    event SalaryPaid(address indexed employee, uint256 amount);

    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    function setSalary(address employee, uint256 amount) external onlyOwner {
        salaries[employee] = amount;
    }

    function paySalary() external {
        uint256 salary = salaries[msg.sender];
        require(salary > 0, "No salary set for the caller");

        // Consider additional conditions and security checks as needed

        // Transfer the salary in cryptocurrency (replace 'tokenTransferFunction' with the actual transfer function)
        // tokenTransferFunction(msg.sender, salary);

        emit SalaryPaid(msg.sender, salary);
    }
}

contract SimpleBlockchain {
        mapping(address => uint256) public balances;

            event Transfer(address indexed from, address indexed to, uint256 value);

                function transfer(address to, uint256 value) external {
                        require(balances[msg.sender] >= value, "Saldo insuficiente");
                                balances[msg.sender] -= value;
                                        balances[to] += value;
                                                emit Transfer(msg.sender, to, value);
                                                    }
}


contract AvatarMovementContract {
    address public owner;
    mapping(address => bool) public avatarsAtLocation;

    event AvatarMoved(address indexed avatar, string location);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    function avatarMoved(string memory location) public {
        require(!avatarsAtLocation[msg.sender], "Avatar is already at this location");
        
        // Perform actions related to avatar movement (e.g., update state, emit events)
        avatarsAtLocation[msg.sender] = true;
        
        // Emit an event to log the avatar movement
        emit AvatarMoved(msg.sender, location);
    }

    // Additional functions and logic can be added based on your requirements
}



"""

# Desplegar el contrato
contract_bytecode = "608060405234801561000f575f80fd5b50335f806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055506105ee8061005c5f395ff3fe608060405234801561000f575f80fd5b506004361061003f575f3560e01c80633a9ef6a814610043578063895c96cf1461005f5780638da5cb5b1461008f575b5f80fd5b61005d60048036038101906100589190610369565b6100ad565b005b6100796004803603810190610074919061040a565b6101dc565b604051610086919061044f565b60405180910390f35b6100976101f9565b6040516100a49190610477565b60405180910390f35b60015f3373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f205f9054906101000a900460ff1615610137576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161012e90610510565b60405180910390fd5b6001805f3373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020015f205f6101000a81548160ff0219169083151502179055503373ffffffffffffffffffffffffffffffffffffffff167ff6f6c02a98adeca28116c9f85cadf2d87a76b025771729ce64dd76d45058757f826040516101d19190610598565b60405180910390a250565b6001602052805f5260405f205f915054906101000a900460ff1681565b5f8054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b5f604051905090565b5f80fd5b5f80fd5b5f80fd5b5f80fd5b5f601f19601f8301169050919050565b7f4e487b71000000000000000000000000000000000000000000000000000000005f52604160045260245ffd5b61027b82610235565b810181811067ffffffffffffffff8211171561029a57610299610245565b5b80604052505050565b5f6102ac61021c565b90506102b88282610272565b919050565b5f67ffffffffffffffff8211156102d7576102d6610245565b5b6102e082610235565b9050602081019050919050565b828183375f83830152505050565b5f61030d610308846102bd565b6102a3565b90508281526020810184848401111561032957610328610231565b5b6103348482856102ed565b509392505050565b5f82601f8301126103505761034f61022d565b5b81356103608482602086016102fb565b91505092915050565b5f6020828403121561037e5761037d610225565b5b5f82013567ffffffffffffffff81111561039b5761039a610229565b5b6103a78482850161033c565b91505092915050565b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f6103d9826103b0565b9050919050565b6103e9816103cf565b81146103f3575f80fd5b50565b5f81359050610404816103e0565b92915050565b5f6020828403121561041f5761041e610225565b5b5f61042c848285016103f6565b91505092915050565b5f8115159050919050565b61044981610435565b82525050565b5f6020820190506104625f830184610440565b92915050565b610471816103cf565b82525050565b5f60208201905061048a5f830184610468565b92915050565b5f82825260208201905092915050565b7f41766174617220697320616c72656164792061742074686973206c6f636174695f8201527f6f6e000000000000000000000000000000000000000000000000000000000000602082015250565b5f6104fa602283610490565b9150610505826104a0565b604082019050919050565b5f6020820190508181035f830152610527816104ee565b9050919050565b5f81519050919050565b5f5b8381101561055557808201518184015260208101905061053a565b5f8484015250505050565b5f61056a8261052e565b6105748185610490565b9350610584818560208601610538565b61058d81610235565b840191505092915050565b5f6020820190508181035f8301526105b08184610560565b90509291505056fea26469706673582212201c4f2fc27e4c22d64aa5484861db8f419991287c80e6d019cb75a447712146bd64736f6c63430008180033"  # Reemplaza con el bytecode de tu contrato

contract_abi = "[
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "avatar",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "location",
				"type": "string"
			}
		],
		"name": "AvatarMoved",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "location",
				"type": "string"
			}
		],
		"name": "avatarMoved",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"name": "avatarsAtLocation",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "owner",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]
		

"  # Reemplaza con el ABI de tu contrato

contract = web3.eth.contract(abi=contract_abi, bytecode=contract_bytecode)

# Configuración de la blockchain simple

class Bloque:
	
    def __init__(self, index, timestamp, avatar_info, hash_anterior):
        self.index = index
        self.timestamp = timestamp
        self.avatar_info = avatar_info
        self.hash_anterior = hash_anterior
        self.nonce = 0
        self.hash = self.calcular_hash()

    def calcular_hash(self):
        datos_codificados = str(self.index) + str(self.timestamp) + str(self.avatar_info) + str(self.hash_anterior) + str(self.nonce)
        return hashlib.sha256(datos_codificados.encode('utf-8')).hexdigest()


    def minar_bloque(self, dificultad):
        while self.hash[:dificultad] != '0' * dificultad:
            self.nonce += 1
            self.hash = self.calcular_hash()

    def calcular_hash(self):
        datos_codificados = str(self.index) + str(self.timestamp) + str(self.datos) + str(self.hash_anterior)
        return hashlib.sha256(datos_codificados.encode('utf-8')).hexdigest()

    def __init__(self, index, timestamp, datos, hash_anterior):
        self.index = index
        self.timestamp = timestamp
        self.datos = datos
        self.hash_anterior = hash_anterior
        self.nonce = 0
        self.hash = self.calcular_hash()

    def proof_of_work(self):
        # (código anterior)

    def validar_prueba(self):
        # (código anterior)
	
def minar_bloque(self, dificultad):
        while self.hash[:dificultad] != '0' * dificultad:
            self.nonce += 1
            self.hash = self.calcular_hash()

    def calcular_hash(self):
        datos_codificados = (
            str(self.index)
            + str(self.timestamp)
            + str(self.datos)
            + str(self.hash_anterior)
            + str(self.espacio_reservado)
        )
        return hashlib.sha256(datos_codificados.encode('utf-8')).hexdigest()

    def __init__(self, index, timestamp, datos, hash_anterior, espacio_reservado=None):
        self.index = index
        self.timestamp = timestamp
        self.datos = datos
        self.hash_anterior = hash_anterior
        self.nonce = 0
        self.espacio_reservado = espacio_reservado
        self.hash = self.calcular_hash()
	    
def __init__(self, index, timestamp, data, proof, previous_hash, resource_logs=None):
        # Otras inicializaciones...

        # Inicializa los registros de recursos si no se proporcionan
        self.resource_logs = resource_logs or []

    def add_resource_log(self, user, amount):
        """
        Agrega un registro de recursos al bloque.

        :param user: Usuario que utilizó los recursos
        :param amount: Cantidad de recursos utilizados
        """
        resource_log = {
            'user': user,
            'amount': amount,
            'timestamp': time.time()
        }
        self.resource_logs.append(resource_log)

# Modifica la clase CadenaBloques para incluir registros de recursos
	
def minar_bloque(self, dificultad):
        while self.hash[:dificultad] != '0' * dificultad:
            self.nonce += 1
            self.hash = self.calcular_hash()

    def proof_of_work(self, dificultad):
        self.nonce = 0  # Restablecer el nonce
        while not self.validar_prueba(dificultad):
            self.nonce += 1
            self.hash = self.calcular_hash()

    def validar_prueba(self, dificultad):
        return self.hash[:dificultad] == '0' * dificultad

    def calcular_hash(self):
        datos_codificados = str(self.index) + str(self.timestamp) + str(self.datos) + str(self.hash_anterior)
        return hashlib.sha256(datos_codificados.encode('utf-8')).hexdigest()

    def __init__(self, index, timestamp, datos, hash_anterior):
        self.index = index
        self.timestamp = timestamp
        self.datos = datos
        self.hash_anterior = hash_anterior
        self.nonce = 0
        self.hash = self.calcular_hash()
	
    def minar_bloque(self, dificultad):
        while self.hash[:dificultad] != '0' * dificultad:
            self.nonce += 1
            self.hash = self.calcular_hash()

    def calcular_hash(self):
        datos_codificados = str(self.index) + str(self.timestamp) + str(self.datos) + str(self.hash_anterior)
        return hashlib.sha256(datos_codificados.encode('utf-8')).hexdigest()

    def __init__(self, index, timestamp, datos, hash_anterior):
        # (código anterior)

    def proof_of_work(self):
        # (código anterior)

    def validar_prueba(self):
        # (código anterior)

class CadenaBloques:


# Clase CadenaBloques

    def __init__(self):
        # Configurar la conexión a un nodo Ethereum (o Infura)
        self.web3 = Web3(Web3.HTTPProvider('URL_DEL_NODO_O_INFURA'))
        if not self.web3.isConnected():
            raise Exception("No se pudo conectar al nodo Ethereum o Infura")

        # Otras configuraciones de la cadena de bloques...

	
    def __init__(self):
        # ... (otras inicializaciones)
        self.total_supply = 30000000
        self.mining_reward = 0.010  # recompensa por bloque minado

    def nuevo_bloque(self, prueba, hash_anterior=None):
        # ... (lógica existente)

        # Calcular la recompensa de minería y actualizar el total de suministro
        recompensa = self.mining_reward
        self.total_supply -= recompensa

        # Asegurarse de que el total de suministro no sea negativo
        if self.total_supply < 0:
            raise Exception("Total de suministro insuficiente")

        # Resto de la lógica para añadir el bloque a la cadena
        # ...
        # ... (otras funciones)

def __init__(self):
        self.cadena = []
        self.transacciones = []
        self.w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

    def generar_billetera(self):
        clave_privada = Account.create().privateKey
        direccion = Account.privateKeyToAccount(clave_privada).address
        return clave_privada, direccion

    def recibir_ether(self, direccion):
        balance_wei = self.w3.eth.getBalance(direccion)
        balance_ether = self.w3.fromWei(balance_wei, 'ether')
        return balance_ether

    def enviar_ether(self, clave_privada_destino, cantidad):
        cuenta_envio = Account.privateKeyToAccount(clave_privada_destino)
        transaccion = {
            'to': cuenta_envio.address,
            'value': self.w3.toWei(cantidad, 'ether'),
            'gas': 2000000,
            'gasPrice': self.w3.toWei('50', 'gwei'),
            'nonce': self.w3.eth.getTransactionCount(cuenta_envio.address),
        }

        firma = Account.sign_transaction(transaccion, self.w3.toBytes(hexstr=cuenta_envio.privateKey))
        tx_hash = self.w3.eth.sendRawTransaction(firma.rawTransaction)

        return tx_hash

    def historial_transacciones(self, direccion):
        historial = []
        for bloque in self.cadena:
            for transaccion in bloque.datos:
                if transaccion['from'] == direccion or transaccion['to'] == direccion:
                    historial.append(transaccion)
        return historial

    # Resto de las funciones de tu clase...

# Ejemplo de uso:
mi_cadena = CadenaBloques()

# Generar una nueva billetera
clave_privada_emisor, direccion_emisor = mi_cadena.generar_billetera()
print(f'Dirección Ethereum del emisor: {direccion_emisor}')

# Generar otra billetera para recibir Ether
clave_privada_receptor, direccion_receptor = mi_cadena.generar_billetera()
print(f'Dirección Ethereum del receptor: {direccion_receptor}')

# Verificar el saldo inicial del emisor
saldo_inicial_emisor = mi_cadena.recibir_ether(direccion_emisor)
print(f'Saldo inicial del emisor: {saldo_inicial_emisor} Ether')

# Enviar Ether del emisor al receptor
cantidad_a_enviar = 1.5
tx_hash = mi_cadena.enviar_ether(clave_privada_receptor, cantidad_a_enviar)
print(f'Transacción enviada. Hash: {tx_hash}')

# Verificar el saldo actual del emisor y receptor
saldo_actual_emisor = mi_cadena.recibir_ether(direccion_emisor)
saldo_actual_receptor = mi_cadena.recibir_ether(direccion_receptor)
print(f'Saldo actual del emisor: {saldo_actual_emisor} Ether')
print(f'Saldo actual del receptor: {saldo_actual_receptor} Ether')

# Obtener el historial de transacciones del emisor
historial_emisor = mi_cadena.historial_transacciones(direccion_emisor)
print(f'Historial de transacciones del emisor: {historial_emisor}')

def __init__(self):
        self.cadena = []
        self.transacciones = []
        self.w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

    def generar_billetera(self):
        clave_privada = Account.create().privateKey
        direccion = Account.privateKeyToAccount(clave_privada).address
        return clave_privada, direccion

    def recibir_ether(self, direccion):
        balance_wei = self.w3.eth.getBalance(direccion)
        balance_ether = self.w3.fromWei(balance_wei, 'ether')
        return balance_ether

    def minar_bloque(self, proof, hash_anterior=None):
        nuevo_bloque = Bloque(
            index=len(self.cadena) + 1,
            timestamp=time.time(),
            datos=self.transacciones,
            proof=proof,
            hash_anterior=hash_anterior or self.hash(self.cadena[-1]) if self.cadena else "1",
        )

        # Reiniciar la lista de transacciones actuales
        self.transacciones = []

        # Agregar el bloque a la cadena
        self.cadena.append(nuevo_bloque)
        return nuevo_bloque

    @staticmethod
    def validar_prueba(prev_proof, proof, hash_anterior):
        guess = f'{prev_proof}{proof}{hash_anterior}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"  # Personaliza según los requisitos de tu cadena

# Ejemplo de uso:
mi_cadena = CadenaBloques()

# Generar una nueva billetera
clave_privada, direccion = mi_cadena.generar_billetera()
print(f'Dirección Ethereum: {direccion}')

# Verificar el saldo actual
saldo_actual = mi_cadena.recibir_ether(direccion)
print(f'Saldo actual: {saldo_actual} Ether')

# Minar un bloque con una prueba de trabajo
proof = 12345  # Reemplaza esto con tu lógica de prueba de trabajo
mi_cadena.minar_bloque(proof)

# Puedes seguir utilizando las funciones de billetera y blockchain según tus necesidades

def nuevo_bloque(self, proof, previous_hash=None, espacio_reservado=None):
        nuevo_bloque = Bloque(
            index=len(self.bloques) + 1,
            timestamp=time.time(),
            datos=self.transacciones,
            hash_anterior=previous_hash or self.hash(self.bloques[-1]) if self.bloques else "1",
            espacio_reservado=espacio_reservado
        )
        self.transacciones = []
        self.bloques.append(nuevo_bloque)
        return nuevo_bloque

    def validar_prueba(self, prev_proof, proof, hash_anterior):
        guess = f'{prev_proof}{proof}{hash_anterior}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"
	
 nuevo bloque en la cadena.

        :param proof: Prueba de trabajo para el nuevo bloque
        :param previous_hash: Hash del bloque anterior (opcional)
        :param resource_logs: Registros de recursos para el bloque
        :return: Nuevo bloque
        """
        nuevo_bloque = Bloque(
            index=len(self.bloques) + 1,
            timestamp=time.time(),
            data=self.transacciones,  # Puedes ajustar esto según tu implementación
            proof=proof,
            previous_hash=previous_hash or self.hash(self.bloques[-1]) if self.bloques else "1",
            resource_logs=resource_logs
        )

        # Restablecer la lista de transacciones actuales
        self.transacciones = []

        # Agregar el bloque a la cadena
        self.bloques.append(nuevo_bloque)
        return nuevo_bloque

    # Otras funciones de la cadena de bloques...

# Ahora, cuando minas un bloque, puedes agregar registros de recursos
# Supongamos que 'user' utilizó 'amount' de recursos
user = "Alice"
amount = 5

# Antes de minar, puedes registrar el uso de recursos
resource_logs = [{'user': user, 'amount': amount, 'timestamp': time.time()}]

# Minar el bloque con los registros de recursos
mi_blockchain.minar_bloque("Datos del bloque", resource_logs)

def __init__(self):
        self.bloques = []

    def agregar_bloque(self, datos, dificultad=4):
        hash_anterior = self.bloques[-1].hash if self.bloques else "1"
        bloque = Bloque(index=len(self.bloques) + 1, timestamp=time.time(), datos=datos, hash_anterior=hash_anterior)
        bloque.proof_of_work(dificultad)
        self.bloques.append(bloque)
        return bloque

# Ejemplo de uso
cadena = CadenaBloques()
cadena.agregar_bloque("Datos del bloque 1")
cadena.agregar_bloque("Datos del bloque 2")

for bloque in cadena.bloques:
    print(f"Bloque {bloque.index}: Hash {bloque.hash}")
	
def agregar_bloque(self, proof, hash_anterior=None, stake=None, espacio=None):
        """
        Agregar un nuevo bloque a la cadena.

        :param proof: Prueba asociada al bloque
        :param hash_anterior: Hash del bloque anterior (opcional para el bloque génesis)
        :param stake: Participación del participante (opcional)
        :param espacio: Espacio del participante (opcional)
        :return: Nuevo bloque
        """
        bloque = {
            'index': len(self.bloques) + 1,
            'timestamp': time(),
            'transacciones': self.transacciones,
            'proof': proof,
            'hash_anterior': hash_anterior or self.hash(self.bloques[-1]) if self.bloques else "1",
            'stake': stake,
            'espacio': espacio
        }

        # Restablecer la lista de transacciones actuales
        self.transacciones = []

        # Validar prueba de participación y espacio si se proporcionan
        if stake is not None and not self.prueba_de_participacion_y_trabajo(self.bloques[-1]['proof'], proof, bloque['hash_anterior'], stake):
            raise ValueError("La prueba de participación y trabajo no es válida.")

        if espacio is not None and not self.prueba_de_espacio(espacio):
            raise ValueError("El participante no tiene suficiente espacio para la prueba de espacio.")

        # Agregar el bloque a la cadena
        self.bloques.append(bloque)
        return bloque
	
def prueba_de_espacio(self, espacio):
    """
        Validar la prueba de espacio: Comprobar si el participante tiene el espacio requerido.

        :param espacio: Espacio requerido para la prueba
        :return: True si tiene suficiente espacio, False si no lo tiene
        """
        # Aquí puedes implementar la lógica para validar el espacio del participante
        # Puedes utilizar la capacidad de almacenamiento del participante u otros factores.
        # Devuelve True si tiene suficiente espacio y False si no lo tiene.
        pass	

def prueba_de_participacion(self, participante):
        """
        Determinar la cantidad de participación que un participante tiene en la cadena.

        :param participante: Dirección del participante
        :return: Cantidad de participación del participante
        """
        # Aquí puedes implementar la lógica para determinar la participación del participante
        # Puede involucrar consultar su saldo, historial de participación, etc.
        # Devuelve la cantidad de participación.
        pass

    def prueba_de_participacion_y_trabajo(self, prev_proof, hash_anterior, participante):
        """
        Algoritmo de prueba de trabajo y participación combinado.

        :param prev_proof: Prueba previa
        :param hash_anterior: Hash del bloque anterior
        :param participante: Dirección del participante
        :return: Prueba válida
        """
        proof = 0
        while not self.validar_prueba(prev_proof, proof, hash_anterior, participante):
            proof += 1
        return proof

    def validar_prueba(self, prev_proof, proof, hash_anterior, participante):
        """
        Validar la prueba de trabajo y participación: Comprobar si el hash cumple con los requisitos.

        :param prev_proof: Prueba previa
        :param proof: Prueba actual
        :param hash_anterior: Hash del bloque anterior
        :param participante: Dirección del participante
        :return: True si es válido, False si no lo es
        """
        # Aquí debes implementar la lógica de validación que incluye la participación
        # Puedes utilizar la cantidad de participación y otros factores en la validación.
        # Devuelve True si la prueba es válida y False si no lo es.
        pass

def nuevo_bloque(self, prueba, hash_anterior=None):
        """
        Crea un nuevo bloque en la cadena de bloques.

        :param prueba: Prueba de trabajo para este bloque
        :param hash_anterior: Hash del bloque anterior (opcional)
        :return: Nuevo bloque
        """
        bloque = {
            'indice': len(self.cadena) + 1,
            'marca_tiempo': time(),
            'transacciones': self.transacciones,
            'prueba': prueba,
            'hash_anterior': hash_anterior or self.hash(self.ultimo_bloque),
        }

        # Restablecer la lista de transacciones actuales
        self.transacciones = []

        self.cadena.append(bloque)
        return bloque

@staticmethod
    def prueba_de_trabajo(ultimo_proof):
        """
        Encuentra un número p' tal que hash(pp') contiene 4 ceros al principio, donde p es la prueba anterior
        y p' es la nueva prueba.

        :param ultimo_proof: Prueba anterior
        :return: Nueva prueba
        """
        prueba = 0
        while not CadenaBloques.validar_prueba(ultimo_proof, prueba):
            prueba += 1
        return prueba

    @staticmethod
    def validar_prueba(ultimo_proof, prueba):
        """
        Verifica si el hash(ultimo_proof, prueba) contiene 4 ceros al principio.

        :param ultimo_proof: Prueba anterior
        :param prueba: Prueba actual
        :return: True si es válido, False si no
        """
        conjetura = f'{ultimo_proof}{prueba}'.encode()
        hash_conjetura = hashlib.sha256(conjetura).hexdigest()
        return hash_conjetura[:4] == "0000"
	    
def nuevo_bloque(self, proof, hash_anterior=None):
        """
        Crear un nuevo bloque en la cadena.

        :param proof: Prueba de trabajo para el nuevo bloque
        :param hash_anterior: Hash del bloque anterior (opcional)
        :return: Nuevo bloque
        """
        bloque = {
            'index': len(self.bloques) + 1,
            'timestamp': time(),
            'transacciones': self.transacciones,
            'proof': proof,
            'hash_anterior': hash_anterior or self.hash(self.bloques[-1]) if self.bloques else "1",
        }

        # Reiniciar la lista de transacciones actuales
        self.transacciones = []

        self.bloques.append(bloque)
        return bloque

@staticmethod
    def validar_prueba(prev_proof, proof, hash_anterior):
        """
        Validar la prueba de trabajo: Comprobar si el hash cumple con los requisitos.

        :param prev_proof: Prueba previa
        :param proof: Prueba actual
        :param hash_anterior: Hash del bloque anterior
        :return: True si es válido, False si no lo es
        """
        guess = f'{prev_proof}{proof}{hash_anterior}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"  # Personaliza según los requisitos de tu cadena

    def prueba_de_trabajo(self, prev_proof, hash_anterior):
        """
        Algoritmo de prueba de trabajo: Encontrar un número (proof) tal que cumpla con las condiciones.

        :param prev_proof: Prueba previa
        :param hash_anterior: Hash del bloque anterior
        :return: Prueba válida
        """
        proof = 0
        while not self.validar_prueba(prev_proof, proof, hash_anterior):
            proof += 1
        return proof
	    
def agregar_bloque(self, proof, hash_anterior=None):
        """
        Agregar un nuevo bloque a la cadena

        :param proof: Prueba asociada al bloque
        :param hash_anterior: Hash del bloque anterior (opcional para el bloque génesis)
        :return: Nuevo bloque
        """
        bloque = {
            'indice': len(self.cadena) + 1,
            'timestamp': time(),
            'transacciones': self.transacciones,
            'proof': proof,
            'hash_anterior': hash_anterior or self.hash(self.cadena[-1])
        }

        # Restablecer la lista de transacciones actuales
        self.transacciones = []

        # Agregar el bloque a la cadena
        self.cadena.append(bloque)
        return bloque

@staticmethod
    def hash(bloque):
        """
        Crear un hash SHA-256 del bloque

        :param bloque: Bloque
        :return: Hash del bloque
        """
        # Asegurarnos de que el diccionario esté ordenado para obtener el mismo hash
        bloque_string = json.dumps(bloque, sort_keys=True).encode()
        return hashlib.sha256(bloque_string).hexdigest()

    def prueba_de_trabajo(self, last_proof):
        """
        Algoritmo simple de prueba de trabajo:
        - Encuentra un número p' tal que hash(pp') contenga 4 ceros al principio, donde p es la prueba anterior
        - p es la prueba actual, p' es la nueva prueba

        :param last_proof: Prueba anterior
        :return: Nueva prueba
        """
        proof = 0
        while self.validar_prueba(last_proof, proof) is False:
            proof += 1
        return proof

    @staticmethod
    def validar_prueba(last_proof, proof):
        """
        Verificar si la prueba es válida:
        - ¿El hash(last_proof, proof) contiene 4 ceros al principio?

        :param last_proof: Prueba anterior
        :param proof: Prueba actual
        :return: True si es válido, False si no lo es
        """
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    def agregar_transaccion(self, remitente, destinatario, cantidad):
        """
        Agregar una transacción al bloque actual

        :param remitente: Dirección del remitente
        :param destinatario: Dirección del destinatario
        :param cantidad: Cantidad transferida
        :return: El índice del bloque que contendrá esta transacción
        """
        self.transacciones.append({
            'remitente': remitente,
            'destinatario': destinatario,
            'cantidad': cantidad,
        })
        return self.obtener_ultimo_bloque()['indice'] + 1

    def agregar_bloque(self, prueba, previous_hash=None):
        """
        Agregar un nuevo bloque a la cadena de bloques

        :param prueba: Prueba del nuevo bloque
        :param previous_hash: Hash del bloque anterior
        :return: Nuevo bloque agregado
        """
        bloque = {
            'indice': len(self.cadena) + 1,
            'timestamp': time(),
            'transacciones': self.transacciones,
            'prueba': prueba,
            'previous_hash': previous_hash or self.hash(self.obtener_ultimo_bloque()),
        }
        # Reiniciar la lista de transacciones después de agregarlas al bloque
        self.transacciones = []
        self.cadena.append(bloque)
        return bloque
	    
@staticmethod
    def validar_prueba(previous_proof, proof, previous_hash)
        Validar la prueba de trabajo: Comprobar si el hash cumple con los requisitos

        :param previous_proof: Prueba del bloque anterior
        :param proof: Prueba actual
        :param previous_hash: Hash del bloque anterior
        :return: True si es válido, False si no lo es
        """
        guess = f"{previous_proof}{proof}{previous_hash}".encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"  # Puedes ajustar el requisito según la dificultad

    def prueba_de_trabajo(self, previous_proof, previous_hash):
        """
        Algoritmo de prueba de trabajo: Encontrar un número que cumpla con la validación

        :param previous_proof: Prueba del bloque anterior
        :param previous_hash: Hash del bloque anterior
        :return: Nueva prueba
        """
        proof = 0
        while not self.validar_prueba(previous_proof, proof, previous_hash):
            proof += 1
        return proof 

  def agregar_bloque(self, proof, previous_hash=None):
        """
        Añadir un bloque a la cadena de bloques

        :param proof: Prueba generada por el algoritmo de prueba de trabajo
        :param previous_hash: Hash del bloque anterior
        :return: Nuevo bloque
        """
        bloque = Bloque(
            index=len(self.chain) + 1,
            timestamp=time(),
            proof=proof,
            previous_hash=previous_hash or self.hash(self.chain[-1]),
        )

        self.chain.append(bloque)
        return bloque
	
def prueba_trabajo(self, last_proof):
        """
        Algoritmo de prueba de trabajo:
        - Encontrar un número p' tal que hash(pp') contiene 4 ceros al inicio, donde p es la prueba anterior
        - p es la prueba actual

        :param last_proof: Prueba anterior
        :return: Prueba actual
        """
        proof = 0
        while self.validar_prueba(last_proof, proof) is False:
            proof += 1

        return proof

    @staticmethod
    def validar_prueba(last_proof, proof):
        """
        Validar si encontrar una prueba es exitoso, es decir, hash(last_proof, proof) contiene 4 ceros al inicio.

        :param last_proof: Prueba anterior
        :param proof: Prueba actual
        :return: True si es válido, False si no lo es
        """
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"	

def minar_bloque(self, minero):
        bloque_nuevo = Bloque(
            index=self.obtener_ultimo_bloque().index + 1,
            transacciones=self.transacciones_pendientes,
            marca_tiempo=time(),
            prueba_trabajo=self.proof_of_work(self.obtener_ultimo_bloque().prueba_trabajo)
        )

        # Reiniciar la lista de transacciones pendientes
        self.transacciones_pendientes = []

        # Agregar el bloque recién minado a la cadena
        self.bloques.append(bloque_nuevo)

        # Devolver el bloque minado
        return bloque_nuevo
	
    def __init__(self):
        self.chain = []
        self.crear_bloque_genesis()

    def crear_bloque_genesis(self):
        bloque_genesis = Bloque(index=0, timestamp=time.time(), datos="Bloque Génesis", hash_anterior="0")
        bloque_genesis.proof_of_work()
        self.chain.append(bloque_genesis)

    def agregar_bloque(self, datos):
        ultimo_bloque = self.chain[-1]
        nuevo_index = ultimo_bloque.index + 1
        nuevo_timestamp = time.time()
        nuevo_hash_anterior = ultimo_bloque.hash
        nuevo_bloque = Bloque(nuevo_index, nuevo_timestamp, datos, nuevo_hash_anterior)
        nuevo_bloque.proof_of_work()
        self.chain.append(nuevo_bloque)

    def validar_cadena(self):
        for i in range(1, len(self.chain)):
            bloque_actual = self.chain[i]
            bloque_anterior = self.chain[i - 1]

            # Verificar el hash anterior
            if bloque_actual.hash_anterior != bloque_anterior.hash:
                return False

            # Verificar la prueba de trabajo
            if not bloque_actual.validar_prueba():
                return False

        return True

# Uso de la cadena de bloques
mi_cadena = CadenaBloques()
mi_cadena.agregar_bloque("Datos del bloque 1")
mi_cadena.agregar_bloque("Datos del bloque 2")

# Validar la cadena
es_valida = mi_cadena.validar_cadena()
print(f"La cadena es válida: {es_valida}")

    def proof_of_work(self):
        # (código anterior)

    def validar_prueba(self):
        # (código anterior)
	    
class CadenaBloques:

def nuevo_bloque(self, proof, previous_hash=None):
        """
        Crea un nuevo bloque en la cadena

        :param proof: La prueba dada por el algoritmo de prueba de trabajo
        :param previous_hash: Hash del bloque anterior
        :return: Nuevo bloque
        """
        bloque = {
            'index': len(self.cadena) + 1,
            'timestamp': time(),
            'transacciones': self.transacciones,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.cadena[-1]) if self.cadena else None
        }

        # Reiniciar la lista de transacciones
        self.transacciones = []

        self.cadena.append(bloque)
        return bloque

  @staticmethod
    def prueba_de_trabajo(last_proof):
        """
        Encuentra un número p' tal que hash(pp') contenga 4 ceros al principio, donde p es el proof anterior
        """
        proof = 0
        while not CadenaBloques.validar_prueba(last_proof, proof):
            proof += 1

        return proof

    @staticmethod
    def validar_prueba(last_proof, proof):
        """
        Valida la prueba: ¿hash(last_proof, proof) contiene 4 ceros al principio?
        """
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

def agregar_bloque(self, proof, hash_anterior=None):
        bloque = {
            'index': len(self.bloques) + 1,
            'timestamp': time(),
            'transacciones': self.transacciones,
            'proof': proof,
            'hash_anterior': hash_anterior or self.hash(self.bloques[-1]),
        }

        # Reiniciar lista de transacciones
        self.transacciones = []

        self.bloques.append(bloque)
        return bloque

def proof_of_work(self, ultimo_proof):
        nuevo_proof = 1
        verificar_proof = False

        while not verificar_proof:
            # Operación hash sha256 sobre la combinación de los proofs
            operacion = hashlib.sha256(
                str(nuevo_proof**2 - ultimo_proof**2).encode()).hexdigest()

            # Verificar si el hash tiene 4 ceros al principio
            if operacion[:4] == '0000':
                verificar_proof = True
            else:
                nuevo_proof += 1

        return nuevo_proof

def agregar_transaccion(self, remitente, destinatario, cantidad):
        self.transacciones_pendientes.append({
            'remitente': remitente,
            'destinatario': destinatario,
            'cantidad': cantidad
        })

        # Devolver el índice del bloque que contendrá esta transacción
        return self.obtener_ultimo_bloque().index + 1

def minar_bloque(self, recompensa_minero):
        # Crear un bloque con las transacciones pendientes y la recompensa para el minero
        nuevo_bloque = Bloque(
            len(self.chain) + 1,
            self.transacciones_pendientes,
            time(),
            self.obtener_ultimo_bloque().hash
        )

        # Reiniciar las transacciones pendientes
        self.transacciones_pendientes = []

        # Agregar el bloque a la cadena
        self.chain.append(nuevo_bloque)

        # Agregar una transacción de recompensa para el minero
        self.agregar_transaccion(
            remitente="Red",
            destinatario=recompensa_minero,
            cantidad=1.0
        )

        return nuevo_bloque
		
hain = [self.crear_bloque_genesis()]
        self.transacciones_pendientes = []

    # (código anterior)

    def agregar_transaccion(self, remitente, destinatario, cantidad):
        # Crear un diccionario con la información de la transacción
        transaccion = {
            'remitente': remitente,
            'destinatario': destinatario,
            'cantidad': cantidad
        }

        # Agregar la transacción a las transacciones pendientes
        self.transacciones_pendientes.append(transaccion)

        # Devolver el índice del bloque que contendrá esta transacción
        return self.obtener_ultimo_bloque().index + 1

# (código anterior)

# Agregar una transacción a la cadena de bloques
indice_bloque_siguiente = mi_cadena.agregar_transaccion('UsuarioA', 'UsuarioB', 1.5)

# Mostrar la cadena de bloques después de agregar la transacción
print(f"\nCadena de bloques después de agregar transacción:")
for bloque in mi_cadena.chain:
    print(bloque.__dict__)
	
	self.chain = [self.crear_bloque_genesis()]
        self.transacciones_pendientes = []

    # (código anterior)

    def minar_bloque(self, minero):
        # Obtener el último bloque
        ultimo_bloque = self.obtener_ultimo_bloque()

        # Crear un nuevo bloque con las transacciones pendientes y la recompensa del minero
        nuevo_bloque = Bloque(
            index=ultimo_bloque.index + 1,
            transacciones=self.transacciones_pendientes.copy(),
            marca_tiempo=time(),
            hash_anterior=ultimo_bloque.hash,
            minero=minero
        )

        # Limpiar las transacciones pendientes
        self.transacciones_pendientes = []

        # Agregar el bloque a la cadena
        self.chain.append(nuevo_bloque)

        return nuevo_bloque

# (código anterior)

# Minar un nuevo bloque con recompensa para 'Minero1'
mi_cadena.minar_bloque('Minero1')

def __init__(self):
        self.chain = [self.crear_bloque_genesis()]
        self.transacciones_pendientes = []

    def crear_bloque_genesis(self):
        # (código anterior)

    def obtener_ultimo_bloque(self):
        return self.chain[-1]

    def agregar_transaccion(self, remitente, destinatario, cantidad):
        self.transacciones_pendientes.append({
            'remitente': remitente,
            'destinatario': destinatario,
            'cantidad': cantidad
        })

    def agregar_bloque(self, minero):
        # (código anterior)

# (código anterior)

# Agregar transacciones
mi_cadena.agregar_transaccion('Juan', 'Maria', 1.5)
mi_cadena.agregar_transaccion('Ana', 'Carlos', 2.3)

# Mostrar transacciones pendientes y último bloque
print("Transacciones pendientes:", mi_cadena.transacciones_pendientes)
print("Último bloque:", mi_cadena.obtener_ultimo_bloque().hash)

self.chain = [self.crear_bloque_genesis()]

    def crear_bloque_genesis(self):
        # (código anterior)

    def agregar_bloque(self, datos):
        # (código anterior)

    def minar_bloque(self, dificultad):
        # (código anterior)

    def verificar_integridad(self):
        for i in range(1, len(self.chain)):
            bloque_actual = self.chain[i]
            bloque_anterior = self.chain[i - 1]
            
            # Verificar que el hash del bloque actual sea correcto
            if bloque_actual.hash != bloque_actual.calcular_hash():
                return False
            
            # Verificar que el hash anterior coincida con el bloque anterior
            if bloque_actual.hash_anterior != bloque_anterior.hash:
                return False
		
        return True

# (código anterior)

# Verificar integridad
integridad_correcta = mi_cadena.verificar_integridad()
print(f"Integridad de la cadena: {integridad_correcta}")

# Uso de la cadena de bloques
mi_cadena = CadenaBloques()
mi_cadena.agregar_bloque("Datos del bloque 1")
mi_cadena.agregar_bloque("Datos del bloque 2")

# Minar un nuevo bloque
mi_cadena.minar_bloque(2)  # La dificultad se puede ajustar según la potencia computacional disponible

# Verificar integridad
integridad_correcta = mi_cadena.verificar_integridad()
print(f"Integridad de la cadena: {integridad_correcta}")

    for i in range(1, len(self.chain)):
            bloque_actual = self.chain[i]
            bloque_anterior = self.chain[i - 1]

            if bloque_actual.hash_anterior != bloque_anterior.calcular_hash():
                return False

        return True

# Uso de la cadena de bloques
mi_cadena = CadenaBloques()
mi_cadena.agregar_bloque("Datos del bloque 1")
mi_cadena.agregar_bloque("Datos del bloque 2")

# Verificar integridad
integridad_correcta = mi_cadena.verificar_integridad()
print(f"Integridad de la cadena: {integridad_correcta}")

     def mostrar_cadena(self):
        for bloque in self.chain:
            print(f"Index: {bloque.index}")
            print(f"Timestamp: {bloque.timestamp}")
            print(f"Datos: {bloque.datos}")
            print(f"Hash: {bloque.hash}")
            print(f"Hash Anterior: {bloque.hash_anterior}")
            print("----")

# Uso de la cadena de bloques
mi_cadena = CadenaBloques()
mi_cadena.agregar_bloque("Datos del bloque 1")
mi_cadena.agregar_bloque("Datos del bloque 2")

# Mostrar la cadena
mi_cadena.mostrar_cadena()
    def __init__(self):
        self.chain = []
        self.crear_bloque_genesis()

    def crear_bloque_genesis(self):
        bloque_genesis = Bloque(index=0, timestamp=time.time(), datos="Bloque Génesis", hash_anterior="0")
        bloque_genesis.proof_of_work()
        self.chain.append(bloque_genesis)

    def agregar_bloque(self, datos):
        ultimo_bloque = self.chain[-1]
        nuevo_index = ultimo_bloque.index + 1
        nuevo_timestamp = time.time()
        nuevo_hash_anterior = ultimo_bloque.hash
        nuevo_bloque = Bloque(nuevo_index, nuevo_timestamp, datos, nuevo_hash_anterior)
        nuevo_bloque.proof_of_work()
        self.chain.append(nuevo_bloque)

# Uso de la cadena de bloques
mi_cadena = CadenaBloques()
mi_cadena.agregar_bloque("Datos del bloque 1")
mi_cadena.agregar_bloque("Datos del bloque 2")

# Imprimir la cadena de bloques
for bloque in mi_cadena.chain:
    print(bloque.__dict__)	

def proof_of_work(self):
        dificultad_objetivo = "0000"  # Puedes ajustar la dificultad según tus necesidades
        self.nonce = 0

        while self.validar_prueba()[:len(dificultad_objetivo)] != dificultad_objetivo:
            self.nonce += 1

    def validar_prueba(self):
        contenido = f"{self.index}{self.timestamp}{self.datos}{self.hash_anterior}{self.nonce}"
        return hashlib.sha256(contenido.encode()).hexdigest()

# Uso de la función de prueba de trabajo
mi_bloque = Bloque(index=1, timestamp=time.time(), datos="Datos de ejemplo", hash_anterior="hash_anterior")
mi_bloque.proof_of_work()
print(f"Prueba de trabajo exitosa. Nonce: {mi_bloque.nonce}")

    def __init__(self, indice, marca_tiempo, datos, hash_anterior):
        self.indice = indice
        self.marca_tiempo = marca_tiempo
        self.datos = datos
        self.hash_anterior = hash_anterior
        self.hash = self.generar_hash()

    def generar_hash(self):
        sha = hashlib.sha256()
        sha.update((str(self.indice) + str(self.marca_tiempo) + str(self.datos) + str(self.hash_anterior)).encode('utf-8'))
        return sha.hexdigest()

    def proof_of_work(self, dificultad):
        self.nonce = 0
        while self.hash[:dificultad] != "0" * dificultad:
            self.nonce += 1
            self.hash = self.calcular_hash()

    def calcular_hash(self):
        return hashlib.sha256(
            f"{self.index}{self.timestamp}{self.datos}{self.nonce}{self.hash_anterior}".encode()
        ).hexdigest()
	
      def crear_bloque_genesis():
    return Bloque(0, datetime.datetime.now(), "Bloque Génesis", "0")

cadena_bloques = [crear_bloque_genesis()]
bloque_actual = cadena_bloques[0]
      
def __init__(self, index, previous_hash, data, proof, stake):
        self.index = index
        self.previous_hash = previous_hash
        self.data = data
        self.proof = proof  # Prueba de trabajo
        self.stake = stake  # Prueba de participación

    def proof_of_work(last_proof, data, difficulty):
        proof = 0
        while not is_valid_proof(last_proof, data, proof, difficulty):
            proof += 1
        return proof

    def is_valid_proof(last_proof, data, proof, difficulty):
        guess = f'{last_proof}{data}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:difficulty] == '0' * difficulty

    def propose_block(data, stake, blockchain):
        last_block = blockchain[-1]
        new_block_index = last_block.index + 1
        last_proof = last_block.proof
        new_proof = proof_of_work(last_proof, data, difficulty)
        new_block = Bloque(new_block_index, last_block.hash(), data, new_proof, stake)
        blockchain.append(new_block)
     def new_block(self, proof, previous_hash=None):
     def new_transaction(self, sender, recipient, amount):
	     
# Resto de tu código para la blockchain...

# Ruta principal que renderiza la interfaz web
@app.route('/')
def index():
    return render_template('../recursos/blochain/WoldbkVirtual.html')

if __name__ == '__main__':
    app.run(debug=True)
