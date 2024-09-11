from Metaverso_Crypto.inicio.contracts_py.boveda_de_seguridad.ci2 import LiquidityPool

def add_liquidity(self, user, amount1, amount2):
    if amount1 <= 0 or amount2 <= 0:
        raise ValueError("Amounts must be greater than zero")
    
    balance1_before = self.token1.balance_of(self)
    balance2_before = self.token2.balance_of(self)
    
    self.token1.transfer_from(user, self, amount1)
    self.token2.transfer_from(user, self, amount2)
    
    balance1_after = self.token1.balance_of(self)
    balance2_after = self.token2.balance_of(self)
    
    liquidity_amount = min(balance1_after - balance1_before, balance2_after - balance2_before)
    
    if liquidity_amount <= 0:
        raise ValueError("Insufficient liquidity")
    
    self.totalSupply += liquidity_amount
    self.balances[user] = self.balances.get(user, 0) + liquidity_amount
    self.lastTransactionTime = datetime.now()

LiquidityPool.add_liquidity = add_liquidity
