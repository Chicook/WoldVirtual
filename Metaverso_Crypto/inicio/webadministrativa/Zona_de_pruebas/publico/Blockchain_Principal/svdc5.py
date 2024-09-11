import tkinter as tk
from flask import Flask, request, jsonify

def iniciar_interfaz():
    class InterfazCompartirRecursos:
        def __init__(self, master):
            self.master = master
            master.title("Compartir Recursos")

            from prb2 import crear_etiqueta
            from prb4 import crear_etiqueta_nombre, crear_entrada_nombre, crear_etiqueta_descripcion, crear_entrada_descripcion

            crear_etiqueta(master, "Ingrese la información del recurso:")
            self.etiqueta_nombre = crear_etiqueta_nombre(master)
            self.entry_nombre = crear_entrada_nombre(master)
            self.etiqueta_descripcion = crear_etiqueta_descripcion(master)
            self.entry_descripcion = crear_entrada_descripcion(master)

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

    return "Interfaz del servidor"

# Integración con Flask
app = Flask(__name__)

@app.route('/compartir_recurso', methods=['POST'])
def compartir_recurso():
    data = request.get_json()
    nombre = data['nombre']
    descripcion = data['descripcion']
    # Aquí puedes realizar las acciones necesarias para agregar el recurso a la cadena de bloques
    return jsonify({'message': f"Recurso compartido - Nombre: {nombre}, Descripción: {descripcion}"})

if __name__ == "__main__":
    app.run(debug=True)
    
