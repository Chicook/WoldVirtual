class CryptoToken:
        def __init__(self, name, symbol, initial_supply):
            self.name = name
            self.symbol = symbol
            self.total_supply = initial_supply
            self.balances = {}

            def transfer(self, from_address, to_address, amount):
                
                if self.balances.get(from_address, 0) >= amount:
                   self.balances[from_address] -= amount
                   self.balances[to_address] = self.balances.get(to_address, 0) + amount
                                                                                       
                return True
                return False

            def mint(self, to_address, amount):
                     self.total_supply += amount
                     self.balances[to_address] = self.balances.get(to_address, 0) + amount
                                                                                                            