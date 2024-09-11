# prb4.py
from OpenGL.GL import *
from prb2 import create_blockchain_connection, create_block
from prb3 import validate_block

vertices = (
    (1, -1, -1),
        (1, 1, -1),
            (-1, 1, -1),
                (-1, -1, -1),
                    (1, -1, 1),
                        (1, 1, 1),
                            (-1, -1, 1),
                                (-1, 1, 1)
                                )

                                surfaces = (
                                    (0, 1, 2, 3),
                                        (3, 2, 7, 6),
                                            (6, 7, 5, 4),
                                                (4, 5, 1, 0),
                                                    (1, 5, 7, 2),
                                                        (4, 0, 3, 6)
                                                        )

                                                        def draw_cube():
                                                            glBegin(GL_QUADS)
                                                                for surface in surfaces:
                                                                        for vertex in surface:
                                                                                    glVertex3fv(vertices[vertex])
                                                                                        glEnd()

                                                                                        def create_and_validate_block():
                                                                                            web3 = create_blockchain_connection()
                                                                                                data = "Cube drawn"
                                                                                                    block = create_block(web3, data)
                                                                                                        if validate_block(web3, block):
                                                                                                                print("Block validated:", block)
                                                                                                                    else:
                                                                                                                            print("Block validation failed")
                                                                                                                