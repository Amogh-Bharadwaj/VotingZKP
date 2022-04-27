from Parameters import G,P
from random import randint

# A class for node (a voter/candidate in our case), with ZKP prover.
class Node:
    def __init__(self,weight:int):
        self.secret = randint(1,10000000) #private key of the node
        self.publicKnowledge = pow(G,self.secret,P) #power(G,secret) (mod P); public key
        # G -> Generator, P -> Prime number, 
        # brute method of solving for x -> Disc log
        self.r = None
        # r -> random number belonging to [0,p-1]
        self.votingWeight = weight
        self.votes = 0 # Relevant only for candidates, number of votes a candidate has got
    
    def Prove(self,questionNumber,verifierData):
        if questionNumber==0:
            #first step of ZKP, h = power(G,r) (mod p)
            self.r = randint(0, P-1)
            h = pow(G,self.r,P)
            return h

        else:
            #third step of ZKP:
            b = verifierData
            x = self.secret
            s = (self.r + b*x) % (P-1)
            return s