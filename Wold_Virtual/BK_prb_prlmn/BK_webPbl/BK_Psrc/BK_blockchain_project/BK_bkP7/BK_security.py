import hashlib

class Security:
    @staticmethod
        def hash_password(password):
                return hashlib.sha256(password.encode('utf-8')).hexdigest()

                    @staticmethod
                        def verify_password(stored_password, provided_password):
                                return stored_password == hashlib.sha256(provided_password.encode('utf-8')).hexdigest()
                