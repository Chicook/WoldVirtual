# prb2.py
import pygame
from pygame.locals import *
from web3 import Web3

def init_pygame(display):
    pygame.init()
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

def create_blockchain_connection():
    web3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
    if web3.isConnected():
        print("Connected to blockchain")
    else:
        print("Failed to connect to blockchain")
    return web3

def create_block(web3, data):
    block = {
        'data': data,
        'hash': web3.keccak(text=data).hex()
    }
    return block
