class Node:
    def __init__(self, address):
        self.address = address
        self.chain = Blockchain()

    def __repr__(self):
        return f"Node(address={self.address})"
      
