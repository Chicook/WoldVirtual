import tkinter as tk

def comunicacion_nodos():
    # Lógica de comunicación entre nodos
    return "Datos de comunicación"

def crear_etiqueta_nombre(master):
    etiqueta_nombre = tk.Label(master, text="Nombre:")
    etiqueta_nombre.pack()
    return etiqueta_nombre

def crear_entrada_nombre(master):
    entry_nombre = tk.Entry(master)
    entry_nombre.pack()
    return entry_nombre

def crear_etiqueta_descripcion(master):
    etiqueta_descripcion = tk.Label(master, text="Descripción:")
    etiqueta_descripcion.pack()
    return etiqueta_descripcion

def crear_entrada_descripcion(master):
    entry_descripcion = tk.Entry(master)
    entry_descripcion.pack()
    return entry_descripcion
