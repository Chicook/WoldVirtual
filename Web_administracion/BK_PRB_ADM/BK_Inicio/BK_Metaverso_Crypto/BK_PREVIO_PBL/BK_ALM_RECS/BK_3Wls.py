import hashlib
import ecdsa
import base58
import os
import time
import reflex as rx

class ColdWallet:
    def __init__(self):
        self.private_keys = {}
        self.addresses = {}

    def generate_wallet(self):
        address = self.new_address()
        private_key = os.urandom(32).hex()
        self.private_keys[address] = private_key
        self.addresses[private_key] = address
        return address

    def new_address(self):
        sk = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
        vk = sk.get_verifying_key()
        sha = hashlib.sha256(vk.to_string()).digest()
        ripemd160 = hashlib.new('ripemd160')
        ripemd160.update(sha)
        raw = b'\x00' + ripemd160.digest()
        checksum = hashlib.sha256(hashlib.sha256(raw).digest()).digest()[:4]
        address = base58.b58encode(raw + checksum).decode('ascii')
        return address

    def create_temp_code(self, address):
        temp_code = hashlib.sha256(f"{address}{time.time()}".encode()).hexdigest()
        return temp_code

    def validate_transaction(self, address, temp_code):
        expected_code = hashlib.sha256(f"{address}{time.time()}".encode()).hexdigest()
        return temp_code == expected_code

    @staticmethod
    def interfaz():
        return rx.center(
            rx.vstack(
                rx.heading("Gestión de Wallets", font_size="2em"),
                rx.button("Generar Wallet", on_click=MainState.generar_wallet),
                rx.input(placeholder="Dirección para código temporal", on_blur=MainState.generar_codigo_temporal),
                rx.input(placeholder="Código temporal para validar", on_blur=MainState.validar_transaccion),
                rx.text(MainState.blockchain_state.mensaje)
            )
        )
