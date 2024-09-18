import reflex as rx
from blockchain import BlockchainState
from block import create_block
from wallet import ColdWallet
from web3_integration import Web3Integration

class MainState(rx.State):
    blockchain_state = BlockchainState()
    wallet = ColdWallet()
    web3_integration = Web3Integration()

    def add_block(self, data):
        self.blockchain_state.add_block(data)

    def generar_wallet(self):
        address = self.wallet.generate_wallet()
        self.blockchain_state.mensaje = f"Nueva dirección generada: {address}"

    def generar_codigo_temporal(self, address):
        temp_code = self.wallet.create_temp_code(address)
        self.blockchain_state.mensaje = f"Código temporal generado: {temp_code}"

    def validar_transaccion(self, address, temp_code):
        if self.wallet.validate_transaction(address, temp_code):
            self.blockchain_state.mensaje = "Transacción válida"
        else:
            self.blockchain_state.mensaje = "Transacción no válida"

    def llamar_contrato(self):
        self.blockchain_state.resultado = self.web3_integration.llamar_contrato()

def interfaz():
    return rx.center(
        rx.vstack(
            rx.heading("Blockchain con Reflex", font_size="2em"),
            rx.button("Generar Wallet", on_click=MainState.generar_wallet),
            rx.input(placeholder="Dirección para código temporal", on_blur=MainState.generar_codigo_temporal),
            rx.input(placeholder="Código temporal para validar", on_blur=MainState.validar_transaccion),
            rx.button("Llamar Contrato", on_click=MainState.llamar_contrato),
            rx.text(MainState.blockchain_state.mensaje),
            rx.text(MainState.blockchain_state.resultado),
            rx.button("Ir a Blockchain", on_click=lambda: rx.navigate("/blockchain")),
            rx.button("Ir a Wallet", on_click=lambda: rx.navigate("/wallet")),
            rx.button("Ir a Web3", on_click=lambda: rx.navigate("/web3")),
        )
    )

app = rx.App(state=MainState)
app.add_page(interfaz, path="/")
app.add_page(BlockchainState.interfaz, path="/blockchain")
app.add_page(ColdWallet.interfaz, path="/wallet")
app.add_page(Web3Integration.interfaz, path="/web3")
app.run()        
