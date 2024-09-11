from ci2 import LiquidityPool

def remove_liquidity(self, user, liquidity):
    if liquidity <= 0:
        raise ValueError("Liquidity must be greater than zero")
    if self.balances.get(user, 0) < liquidity:
        raise ValueError("Insufficient liquidity balance")
    
    balance1 = self.token1.balance_of(self)
    balance2 = self.token2.balance_of(self)
    
    amount1 = (liquidity * balance1) // self.totalSupply
    amount2 = (liquidity * balance2) // self.totalSupply
    
    if amount1 <= 0 or amount2 <= 0:
        raise ValueError("Amounts must be greater than zero")
    
    self.totalSupply -= liquidity
    self.balances[user] -= liquidity
    
    self.token1.transfer(user, amount1)
    self.token2.transfer(user, amount2)
    self.lastTransactionTime = datetime.now()

LiquidityPool.remove_liquidity = remove_liquidity
