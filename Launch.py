from Block import Block
from Node import Node
from Blockchain import Blockchain
from Transaction import Transaction
from random import choice, randint

print("\nWELCOME TO ANNUAL ELECTIONS 2022!")
print("*"*40)

Candidates = [Node(0),Node(0),Node(0)]

#  Voters
Nodes=[]
for i in range(100):
    Nodes.append(Node(i%3))

print("Nodes initialised.")
  
# Votes
Transactions=[]
for i in range(100):
    Transactions.append(Transaction(choice(Nodes),randint(0, 2)))

print("Prepared mock transactions/votes.\n")

# Views vote of a user
def ViewUser(N:Node):
    print("User Database:")
    print("--------------\n")
    
    UserTransactionMap = dict()
    for T in Transactions:
        if T.voter == N:
            print("Voter ID: ", N.publicKnowledge)
            print("Voted at: ", T.timestamp)
            print("----------------------------------")

VoteChain = Blockchain([])

VerifiedPool = []
MaliciousPool = []

print("\nZKP Transaction Verification")
print("----------------------------")
print("Verifying...\n")
print("|", sep=' ', end='')
Loader = 0
for T in Transactions:
    print(u"█",sep='',end='',flush=True) # Just for a loading bar
    if T.ZKP_TransactionVerification() == True:
        VerifiedPool.append(T)
    else:
        MaliciousPool.append(T)
    
print("|\n")
print("Verification complete")
print("----------------------------\n")

BLOCK_LIMIT = 7
for i in range(0,len(VerifiedPool),BLOCK_LIMIT):
    Limiter = 0
    if i+ BLOCK_LIMIT >= len(VerifiedPool):
        Limiter = len(VerifiedPool) - i -1
    else:
        Limiter = BLOCK_LIMIT
    VoteBlock = Block("INITIAL HASH",VerifiedPool[i:i+Limiter])
    VoteChain.MineBlock(VoteBlock)
    print("New block mined!")
    print("Block timestamp: ", VoteBlock.timestamp)
    print("-----------------------------------------------------")
    
VoteChain.VerifyChain()
print("\n THANK YOU")

