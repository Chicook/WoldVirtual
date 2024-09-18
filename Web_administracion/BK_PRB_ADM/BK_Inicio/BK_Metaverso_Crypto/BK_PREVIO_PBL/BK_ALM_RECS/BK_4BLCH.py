import reflex as rx
from block import create_block

class BlockchainState(rx.State):
    blockchain = []
    mensaje = ""

    def add_block(self, data):
        if self.blockchain:
            new_block = create_block(self.blockchain[-1], data)
            if self.is_block_valid(new_block, self.blockchain[-1]):
                self.blockchain.append(new_block)
                self.mensaje = "Bloque añadido y validado correctamente"
            else:
                self.mensaje = "Error en la validación del bloque"
        else:
            self.mensaje = "Blockchain no inicializada"

    def is_block_valid(self, new_block, previous_block):
        if previous_block.index + 1 != new_block.index:
            return False
        if previous_block.hash != new_block.previous_hash:
            return False
        if new_block.calculate_hash() != new_block.hash:
            return False
        return True

    @staticmethod
    def interfaz():
        return rx.center(
            rx.vstack(
                rx.heading("Gestión de Blockchain", font_size="2em"),
                rx.input(placeholder="Datos del bloque", on_blur=MainState.add_block),
                rx.text(MainState.blockchain_state.mensaje)
            )
        )
          
