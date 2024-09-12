# prb1.py
from Metaverso_Crypto.inicio.Zona_depruebas.webadministrativa.Blockchain_Principal.Zona_de_pruebas.admin.pruebas2.Bk_Servidor.BK_dbts.src.BK_Scv.prb2 import init_pygame, create_blockchain_connection, create_block
from prb3 import init_opengl, validate_block
from prb4 import draw_cube
from prb5 import main_loop

display = (800, 600)

init_pygame(display)
init_opengl(display)

# Create and validate block for prb1 module
web3 = create_blockchain_connection()
data = "Initialization complete"
block = create_block(web3, data)
if validate_block(web3, block):
    print("Block validated for prb1:", block)
else:
    print("Block validation failed for prb1")

main_loop(draw_cube)
