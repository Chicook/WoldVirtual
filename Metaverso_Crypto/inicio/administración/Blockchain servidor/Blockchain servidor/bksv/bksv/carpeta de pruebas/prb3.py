class PixlNFT:
    def __init__(self):
        self.token_ids = 0
        self.tokens = {}

    def create_token(self, caller_address, token_uri, value):
        if value < 1:
            raise ValueError("Not enough ETH sent; check price!")
        self.token_ids += 1
        new_item_id = self.token_ids
        self.tokens[new_item_id] = {"owner": caller_address, "uri": token_uri}
        print(f"Token created: {new_item_id}, {token_uri}")
        return new_item_id
