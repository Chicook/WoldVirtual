from ci2 import LiquidityPool

def buy_tokens(self, user, amount):
    if amount <= 0:
        raise ValueError("Amount must be greater than zero")
    if self.token1.balance_of(self) < amount:
        raise ValueError("Insufficient liquidity for this transaction")
    
    self.token1.transfer_from(user, self, amount)
    tokens_bought = (amount * self.token2.balance_of(self)) // self.token1.balance_of(self)
    
    if tokens_bought <= 0:
        raise ValueError("Insufficient liquidity")
    
    self.token2.transfer(user, tokens_bought)
    self.lastTransactionTime = datetime.now()

def sell_tokens(self, user, tokens):
    if tokens <= 0:
        raise ValueError("Tokens must be greater than zero")
    if self.token2.balance_of(self) < tokens:
        raise ValueError("Insufficient liquidity for this transaction")
    
    self.token2.transfer_from(user, self, tokens)
    tokens_sold = (tokens * self.token1.balance_of(self)) // self.token2.balance_of(self)
    
    if tokens_sold <= 0:
        raise ValueError("Insufficient liquidity")
    
    self.token1.transfer(user, tokens_sold)
    self.lastTransactionTime = datetime.now()

LiquidityPool.buy_tokens = buy_tokens
LiquidityPool.sell_tokens = sell_tokens
