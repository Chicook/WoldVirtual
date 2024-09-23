import unittest
from BK_bkP3.blockchain import Blockchain
from BK_bkP2.block import Block

class TestBlockchain(unittest.TestCase):
    def setUp(self):
            self.blockchain = Blockchain()

                def test_genesis_block(self):
                        self.assertEqual(self.blockchain.chain[0].data, "Genesis Block")

                            def test_add_block(self):
                                    self.blockchain.add_block(Block(1, "", time.time(), "Test Block", ""))
                                            self.assertEqual(len(self.blockchain.chain), 2)

                                            if __name__ == '__main__':
                                                unittest.main()
                                                