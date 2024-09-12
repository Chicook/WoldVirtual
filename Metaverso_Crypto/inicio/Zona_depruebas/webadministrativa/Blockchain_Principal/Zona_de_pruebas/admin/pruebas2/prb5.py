# prb5.py
import pygame
from OpenGL.GL import *
from prb4 import create_and_validate_block

def main_loop(draw_function):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_function()
        pygame.display.flip()
        pygame.time.wait(10)
        create_and_validate_block()

