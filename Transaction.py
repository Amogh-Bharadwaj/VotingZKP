from Node import Node
from random import randint
from Parameters import G,P
class Transaction:
    def __init__(self, voter:Node,candidate):
        self.voter = voter
        self.candidate = candidate

    def ZKP_TransactionVerification(self):
        ROUNDS = 500
        print("Interactive Zero-Knowledge Proof in progress...")

        for Round in range(ROUNDS):
            y = self.voter.publicKnowledge

            # Node: Chooses 0 <= r < p - 1, sends h = pow(g,r,p)
            h = self.voter.Prove(0, None)

            # Miner: Gives b = randint(0,1)
            # Node: Sends s = r+b*x % p-1
            b = randint(0,1)
            s = self.voter.Prove(1, b)

            # Miner: Checks if pow(g,s,p) == h*pow(y,b,p) % p
            valid = pow(G,s,P) == (h*pow(y,b,P)) % P
            
            if not valid:
               return False
        print("Zero-knowledge protocol passed successfully.")
        print("--------------------------------------------\n")
        return True
    
    