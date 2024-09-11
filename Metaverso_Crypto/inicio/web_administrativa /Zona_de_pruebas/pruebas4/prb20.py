from prb2 import calculate_hash

def validate_blockchain(blockchain):
    for i in range(1, len(blockchain)):
        current_block = blockchain[i]
        previous_block = blockchain[i - 1]

        # Validar el hash del bloque actual
        if current_block.hash != calculate_hash(current_block.index, current_block.previous_hash, current_block.timestamp, current_block.data):
            return False

        # Validar el hash del bloque anterior
        if current_block.previous_hash != previous_block.hash:
            return False

    return True

def validate_block(block):
    return block.hash == calculate_hash(block.index, block.previous_hash, block.timestamp, block.data)

def explain_prb5():
    print("Sección prb5: Validación de la Blockchain")
    print("Funciones:")
    print("1. validate_blockchain: Función para validar toda la blockchain.")
    print("2. validate_block: Función para validar un bloque específico.")
    input("Presione Enter para volver al menú principal...")









# import hashlib
# import time

# class Block:
    # def __init__(self, index, previous_hash, transactions, timestamp):
       # self.index = index
       # self.previous_hash = previous_hash
       #  self.transactions = transactions
      #  self.timestamp = timestamp
       # self.hash = self.calculate_hash()

   # def calculate_hash(self):
       # block_string = f"{self.index}{self.previous_hash}{self.transactions}{self.timestamp}"
       # return hashlib.sha256(block_string.encode()).hexdigest()

# class Blockchain:
    # def __init__(self):
       # self.chain = []

  #  def get_latest_block(self):
       # return self.chain[-1] if self.chain else None

   # def get_latest_block_hash(self):
       # return self.get_latest_block().hash if self.get_latest_block() else "0"

  #  def add_block(self, new_block):
      #  if self.chain:
           # new_block.previous_hash = self.get_latest_block().hash
       # else:
           # new_block.previous_hash = "0"
      #  new_block.hash = new_block.calculate_hash()
        # self.chain.append(new_block)

 #   def is_chain_valid(self):
        # for i in range(1, len(self.chain)):
           # current_block = self.chain[i]
           # previous_block = self.chain[i - 1]

          #  if current_block.hash != current_block.calculate_hash():
                # return False

           # if current_block.previous_hash != previous_block.hash:
                # return False

      #  return True

# Ejemplo de uso
# blockchain = Blockchain()
