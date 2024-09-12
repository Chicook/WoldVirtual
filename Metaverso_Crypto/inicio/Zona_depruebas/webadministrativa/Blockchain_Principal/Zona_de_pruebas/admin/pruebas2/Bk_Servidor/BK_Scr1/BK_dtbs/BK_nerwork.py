class Network:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def broadcast_transaction(self, transaction):
        for node in self.nodes:
            node.chain.add_transaction(transaction)
          
