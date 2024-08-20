class Blockchain:
    
    def __init__(self):
        self.chain = []
        self.crear_bloque_genesis()

    def crear_bloque_genesis(self):
        genesis_block = {
            'index': 0,
            'timestamp': '2024-08-20 00:00:00',
            'data': 'Bloque Génesis',
            'previous_hash': '0'
        }
        self.chain.append(genesis_block)

    def agregar_bloque(self, data):
        previous_block = self.chain[-1]
        new_block = {
            'index': len(self.chain),
            'timestamp': '2024-08-20 00:00:00',
            'data': data,
            'previous_hash': self.hash(previous_block)
        }
        self.chain.append(new_block)

    def obtener_informacion_cadena(self):
        informacion = {
            'longitud': len(self.chain),
            'bloques': [block for block in self.chain],
        }
        return informacion

    def hash(self, block):
        # Aquí puedes implementar una función de hash adecuada
        return str(block)  # Esto es solo un ejemplo, usa una función de hash real

    def validar_cadena(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block['previous_hash'] != self.hash(previous_block):
                return False
        return True

        # reservado para modificaciónes 
        # o actualizaciones de este módulo.
        
# class Blockchain:
    # def __init__(self):
           # self.chain = []

   # def obtener_informacion_cadena(self):
       # informacion = {
        #'longitud': len(self.chain),
        #'bloques': [block.__dict__ for block in self.chain],
                                                        }
       # return informacion
            
