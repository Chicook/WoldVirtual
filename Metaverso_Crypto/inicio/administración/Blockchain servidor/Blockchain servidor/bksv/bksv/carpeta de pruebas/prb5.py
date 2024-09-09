import json

def crear_wallet():
    wallet_id = "bkmv" + hashlib.sha256().hexdigest()[:8]
        wallet = {'id': wallet_id, 'balance': 0}
            with open(f'{wallet_id}.json', 'w') as f:
                    json.dump(wallet, f)
                        return wallet

                        def validar_registro(forks):
                            if forks == 4:
                                    return 30000000.000
                                        else:
                                                return 0.001
                                                