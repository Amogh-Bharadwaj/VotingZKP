from Block import Block,GENESIS_BLOCK
from MerkleTree import MerkleHash

# A class for blockchain which consists of a list of blocks and two functions to add a block and verify the chain.

class Blockchain:
    def __init__(self,blocks):
        self.blockchain = [GENESIS_BLOCK]+blocks
    
    def MineBlock(self,block:Block):
        print("Mining block....")
        block.previousHash = self.blockchain[-1].blockHash
        print("Block previous hash set: ", block.previousHash)
        block.ProofOfWork()
        block.blockHash = MerkleHash(block.transactions)
        print("Block hash computed: ", block.blockHash)
        print("Proof of Work complete")
        self.blockchain.append(block)
        
    
    def VerifyChain(self):
        if self.blockchain[0] != GENESIS_BLOCK:
            print("Error: First block of the blockchain must be the genesis block.")
            return False

        for i in range(1,len(self.blockchain)):
            if self.blockchain[i].previousHash != self.blockchain[i-1].blockHash:
                print("Error: Incorrect block hash.")
                return False
            
            elif self.blockchain[i].VerifyPoW == False:
                print("Proof of Work mismatch. Invalid chain.")
                return False
            
            else: 
                print("Chain is valid.")
                return True

            