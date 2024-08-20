class Blockchain:
    def __init__(self):
            self.chain = []

    def obtener_informacion_cadena(self):
        informacion = {
        'longitud': len(self.chain),
        'bloques': [block.__dict__ for block in self.chain],
                                                        }
        return informacion
            