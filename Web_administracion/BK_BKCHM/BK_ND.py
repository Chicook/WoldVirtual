# network.py

import requests
import json

class Node:
    def __init__(self, address):
            self.address = address
                    self.peers = set()

                        def add_peer(self, peer_address):
                                self.peers.add(peer_address)

                                    def broadcast_new_block(self, block):
                                            for peer in self.peers:
                                                        requests.post(f"{peer}/new_block", data=json.dumps(block.__dict__))
                                                        