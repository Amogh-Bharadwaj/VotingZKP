from Node import Node
from Parameters import G,P
from hashlib import sha256
import time

def Hash(seed:int):
    return sha256(hex(seed).encode()).hexdigest()

# A class for a block with block header and transactions.
class Block:
    def __init__(self,block_hash,votes):
        # Header fields
        self.timestamp = time.time();
        self.previousHash = None
        self.blockHash = block_hash
        self.difficulty = 4
        self.nonce = None;
        
        # Transactions
        self.transactions = votes
        
    def ProofOfWork(self):
        for nonce in range(1,1000000000):
            if Hash(nonce)[-self.difficulty:] == "0"*self.difficulty:
                self.nonce = nonce
                break
        
    def VerifyPoW(self):
        if Hash(nonce)[-self.difficulty:] == "0"*self.difficulty and self.blockHash == Hash(nonce):
            return True
        return False

GENESIS_BLOCK = Block("GENESIS_BLOCK",None)