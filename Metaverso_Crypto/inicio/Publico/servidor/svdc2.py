import hashlib
import tkinter as tk

def gestionar_usuarios():
    # Lógica de gestión de usuarios
    return "Datos de usuarios"

def calcular_hash(data, previous_hash):
    # Calcula el hash del bloque
    block_string = f"{data}{previous_hash}".encode()
    return hashlib.sha256(block_string).hexdigest()

def crear_etiqueta(master, text):
    etiqueta = tk.Label(master, text=text)
    etiqueta.pack()
    return etiqueta
