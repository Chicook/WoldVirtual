from prb2 import gestionar_usuarios, calcular_hash, crear_etiqueta
from prb3 import gestionar_recursos, validar_bloque, crear_entrada
from prb4 import comunicacion_nodos, crear_etiqueta_nombre, crear_entrada_nombre, crear_etiqueta_descripcion, crear_entrada_descripcion
from prb5 import iniciar_interfaz, compartir_recurso
from web3 import Web3

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(data="Bloque inicial", previous_hash='0')  # Bloque inicial, no génesis

    def create_block(self, data, previous_hash):
        block = {'index': len(self.chain) + 1,
                 'data': data,
                 'previous_hash': previous_hash,
                 'hash': calcular_hash(data, previous_hash)}
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def add_block(self, data):
        previous_block = self.get_previous_block()
        previous_hash = previous_block['hash']
        block = self.create_block(data, previous_hash)
        if validar_bloque(block):
            self.chain.append(block)
        return block

blockchain = Blockchain()

def main():
    data = {
        'usuarios': gestionar_usuarios(),
        'recursos': gestionar_recursos(),
        'comunicacion': comunicacion_nodos(),
        'interfaz': iniciar_interfaz()
    }
    blockchain.add_block(data)

if __name__ == "__main__":
    main()
