class TokenICO:
    def __init__(self, total_tokens):
        self.owner = "owner_address"
        self.total_tokens = total_tokens
        self.tokens_sold = 0
        self.balances = {}

    def only_owner(func):
        def wrapper(self, *args, **kwargs):
            if "caller_address" != self.owner:
                raise PermissionError("Only the owner can call this function")
            return func(self, *args, **kwargs)
        return wrapper

    def purchase_tokens(self, caller_address, amount, value):
        if self.tokens_sold + amount > self.total_tokens:
            raise ValueError("Not enough tokens available")
        if value != amount * 1:
            raise ValueError("Incorrect Ether amount")

        if caller_address not in self.balances:
            self.balances[caller_address] = 0
        self.balances[caller_address] += amount
        self.tokens_sold += amount
        print(f"TokenPurchased: {caller_address}, {amount}, {self.tokens_sold}")

    @only_owner
    def withdraw_funds(self):
        print(f"Funds withdrawn by {self.owner}")
