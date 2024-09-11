## modulo principal ##

from Metaverso_Crypto.inicio.contracts_py.boveda_de_seguridad.ci2 import LiquidityPool
from Metaverso_Crypto.inicio.contracts_py.boveda_de_seguridad.ci3 import add_liquidity
from Metaverso_Crypto.inicio.contracts_py.boveda_de_seguridad.ci4 import remove_liquidity
from Metaverso_Crypto.inicio.contracts_py.boveda_de_seguridad.ci5 import buy_tokens, sell_tokens

# Ejemplo de uso
if __name__ == "__main__":
    token1 = ...  # Definir token1
    token2 = ...  # Definir token2
    pool = LiquidityPool(token1, token2)
    
    user = ...  # Definir usuario
    pool.add_liquidity(user, 100, 200)
    pool.remove_liquidity(user, 50)
    pool.buy_tokens(user, 100)
    pool.sell_tokens(user, 50)
    
    # Funciones adicionales
    balance = pool.get_balance(user)
    pool_state = pool.get_pool_state()
    print(f"Balance del usuario: {balance}")
    print(f"Estado del pool: {pool_state}")
