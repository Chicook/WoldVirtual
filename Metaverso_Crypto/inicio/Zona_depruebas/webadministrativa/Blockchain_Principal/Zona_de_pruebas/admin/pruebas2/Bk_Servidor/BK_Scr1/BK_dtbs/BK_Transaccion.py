class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.timestamp = time.time()

    def __repr__(self):
        return f"Transaction(sender={self.sender}, recipient={self.recipient}, amount={self.amount}, timestamp={self.timestamp})"
