from BK_bkP2.block import Block

class BlockchainValidator:
    @staticmethod
        def is_chain_valid(blockchain):
                for i in range(1, len(blockchain.chain)):
                            current_block = blockchain.chain[i]
                                        previous_block = blockchain.chain[i - 1]

                                                    if current_block.hash != Block.calculate_hash(current_block.index, current_block.previous_hash, current_block.timestamp, current_block.data):
                                                                    return False

                                                                                if current_block.previous_hash != previous_block.hash:
                                                                                                return False

                                                                                                        return True
                                                                    