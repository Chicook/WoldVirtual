class User:
    def __init__(self, user_id, wallet):
        self.user_id = user_id
        self.wallet = wallet

    def send_wcv(self, amount, recipient_wallet):
        # Lógica para enviar WCV
        print(f"{self.user_id} envió {amount} WCV a {recipient_wallet}")

    def receive_wcv(self, amount, sender_wallet):
        # Lógica para recibir WCV
        print(f"{self.user_id} recibió {amount} WCV de {sender_wallet}")
