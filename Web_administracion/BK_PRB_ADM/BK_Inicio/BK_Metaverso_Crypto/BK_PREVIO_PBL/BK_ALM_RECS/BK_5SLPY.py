from web3 import Web3
import reflex as rx

class Web3Integration:
    def __init__(self):
        self.web3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'))
        self.abi = 'TU_ABI_AQUÍ'
        self.address = 'DIRECCIÓN_DEL_CONTRATO'
        self.contract = self.web3.eth.contract(address=self.address, abi=self.abi)

    def llamar_contrato(self):
        return self.contract.functions.nombreDeLaFuncion().call()

    @staticmethod
    def interfaz():
        return rx.center(
            rx.vstack(
                rx.heading("Integración con Web3", font_size="2em"),
                rx.button("Llamar Contrato", on_click=MainState.llamar_contrato),
                rx.text(MainState.blockchain_state.resultado)
            )
        )
