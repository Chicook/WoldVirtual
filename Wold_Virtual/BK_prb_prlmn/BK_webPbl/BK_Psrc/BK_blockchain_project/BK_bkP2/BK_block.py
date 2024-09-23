import hashlib

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
            self.index = index
                    self.previous_hash = previous_hash
                            self.timestamp = timestamp
                                    self.data = data
                                            self.hash = hash

                                                @staticmethod
                                                    def calculate_hash(index, previous_hash, timestamp, data):
                                                            value = str(index) + str(previous_hash) + str(timestamp) + str(data)
                                                                    return hashlib.sha256(value.encode('utf-8')).hexdigest()
            