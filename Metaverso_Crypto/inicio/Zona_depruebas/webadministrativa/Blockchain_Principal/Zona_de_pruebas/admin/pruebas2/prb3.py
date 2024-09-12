# prb3.py
from OpenGL.GL import *
from OpenGL.GLU import *
from Metaverso_Crypto.inicio.Zona_depruebas.webadministrativa.Blockchain_Principal.Zona_de_pruebas.admin.pruebas2.Bk_Servidor.BK_dbts.src.BK_Scv.prb2 import create_blockchain_connection, create_block

def init_opengl(display):
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

def validate_block(web3, block):
    expected_hash = web3.keccak(text=block['data']).hex()
    return block['hash'] == expected_hash
