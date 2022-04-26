from Parameters import G,P
from random import randint

# A class for node (a voter/candidate in our case), with ZKP prover.
class Node:
    def __init__(self,weight:int):
        self.secret = randint(1,10000000)
        self.publicKnowledge = pow(G,self.secret,P)
        self.r = None

        self.votingWeight = weight
        self.votes = 0 # Relevant only for candidates
    
    def Prove(self,questionNumber,verifierData):
        if questionNumber==0:
            self.r = randint(0, P-1)
            h = pow(G,self.r,P)
            return h

        else:
            b = verifierData
            x = self.secret
            s = (self.r + b*x) % (P-1)
            return s