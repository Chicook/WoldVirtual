from flask import jsonify, request
from Wold_Virtual.BK_Adm_prb.BK_Inicio.BK_Blockchain_Principal.Bk_Servidor.BK_RCS.BK_Admin_web.BK_Scr1.BK_Stst.BK_Service.BSnts import obtener_blockchain, agregar_bloque, obtener_bloque

def configurar_rutas(app):
    @app.route('/')
    def index():
        return "El servidor está funcionando correctamente."

    @app.route('/blockchain', methods=['GET'])
    def get_blockchain():
        return jsonify({'blockchain': obtener_blockchain()})

    @app.route('/add_block', methods=['POST'])
    def add_block():
        data = request.get_json()
        if 'data' in data:
            new_block = agregar_bloque(data['data'])
            return jsonify({'message': 'Bloque agregado correctamente', 'block': new_block})
        else:
            return jsonify({'error': 'Datos no proporcionados'})

    @app.route('/block/<int:block_index>', methods=['GET'])
    def get_block(block_index):
        block = obtener_bloque(block_index)
        if block:
            return jsonify({'block': block})
        else:
            return jsonify({'error': 'Índice de bloque inválido'})

