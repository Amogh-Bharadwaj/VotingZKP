from Block import Block,GENESIS_BLOCK

class Blockchain:
    def __init__(self,blocks):
        self.blockchain = [GENESIS_BLOCK]+blocks
    
    def MineBlock(self,block:Block):
        print("Mining block....")
        block.previousHash = self.blockchain[-1].blockHash
        block.ProofOfWork()
        print("Proof of Work complete")
        self.blockchain.append(block)
        print("New block added")
    
    def VerifyChain(self):
        if self.blockchain[0] != GENESIS_BLOCK:
            print("Error: First block of the blockchain must be the genesis block.")
            return False

        for i in range(1,len(self.blockchain)):
            if self.blockchain[i].previousHash != self.blockchain[i-1].blockHash:
                print("Error: Incorrect block hash.")
                return False
            
            elif self.blockchain[i].VerifyPoW == False:
                return False
            
            else: 
                return True

            