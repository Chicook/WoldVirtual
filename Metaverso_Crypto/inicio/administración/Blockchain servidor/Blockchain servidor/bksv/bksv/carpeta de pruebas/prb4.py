class WoldcoinVirtual:
    def __init__(self):
        self.name = "WoldcoinVirtual"
        self.symbol = "WCV"
        self.decimals = 3
        self.total_supply = 30000000 * (10 ** self.decimals)
        self.owner = "owner_address"
        self.commission = 1 * (10 ** (self.decimals - 3))
        self.balance_of = {self.owner: self.total_supply}
        self.staked_balance = {}
        self.staked_timestamp = {}

    def transfer(self, from_address, to_address, value):
        if to_address == "":
            raise ValueError("Invalid address")
        if self.balance_of.get(from_address, 0) < value:
            raise ValueError("Insufficient balance")
        fee = (value * self.commission) / (10 ** self.decimals)
        net_value = value - fee
        self.balance_of[from_address] -= value
        self.balance_of[to_address] = self.balance_of.get(to_address, 0) + net_value
        self.balance_of[self.owner] += fee
        print(f"Transfer: {from_address} to {to_address}, {net_value} (fee: {fee})")

    def stake(self, caller_address, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than zero")
        if self.balance_of.get(caller_address, 0) < amount:
            raise ValueError("Insufficient balance")
        self.balance_of[caller_address] -= amount
        self.staked_balance[caller_address] = self.staked_balance.get(caller_address, 0) + amount
        self.staked_timestamp[caller_address] = "current_timestamp"
        print(f"Staked: {caller_address}, {amount}")

    def unstake(self, caller_address, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than zero")
        if self.staked_balance.get(caller_address, 0) < amount:
            raise ValueError("Insufficient staked balance")
        if "current_timestamp" < self.staked_timestamp.get(caller_address, 0) + 1:
            raise ValueError("Staking duration not met")
        self.staked_balance[caller_address] -= amount
        self.balance_of[caller_address] += amount
        self.staked_timestamp[caller_address] = 0
        print(f"Unstaked: {caller_address}, {amount}")
        
