import requests

class Network:
    def __init__(self):
            self.nodes = set()

                def add_node(self, address):
                        self.nodes.add(address)

                            def broadcast_new_block(self, block):
                                    for node in self.nodes:
                                                requests.post(f'{node}/mine_block', json=block.__dict__)
                                                