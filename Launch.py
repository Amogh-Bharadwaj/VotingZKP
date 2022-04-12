from Block import Block
from Node import Node
from Blockchain import Blockchain
from Transaction import Transaction

print("\nWELCOME TO ANNUAL ELECTIONS 2022!")
print("*"*40)

Candidates = [Node(0),Node(0),Node(0)]

#  Voters
N1 = Node(1)
N2 = Node(1)
N3 = Node(1)
N4 = Node(3)
N5 = Node(3)

def ViewAllUsers():
    print("User Database:")
    print("--------------\n")

    for i,N in enumerate([N1,N2,N3,N4,N5]):
        print("User "+str(i+1))
        print("Public Voter ID:",end=" ")
        print(N.publicKnowledge)
        print("Secret Key:",end=" ")
        print("*"*(len(str(N.secret))-3)+str(N.secret)[-3:])
        print("Vote Weight:",end=" ")
        print(N.votingWeight)
        print("Votes secured:",end=" ")
        print(N.votes)
        print("-"*80+"\n")


# Votes
T1 = Transaction(N1,2)
T2 = Transaction(N2,1)
T3 = Transaction(N3,2)
T4 = Transaction(N4,1)
T5 = Transaction(N5,0)

def ViewAllUsers():
    print("User Database:")
    print("--------------\n")
    
    UserTransactionMap = dict()
    for T in [T1,T2,T3,T4,T5]:
        if 

    for i,N in enumerate([N1,N2,N3,N4,N5]):
        print("User "+str(i+1))
        print("Public Voter ID:",end=" ")
        print(N.publicKnowledge)
        print("Secret Key:",end=" ")
        print("*"*(len(str(N.secret))-3)+str(N.secret)[-3:])
        print("Vote Weight:",end=" ")
        print(N.votingWeight)
        print("Votes secured:",end=" ")
        print(N.votes)
        print("Transactions:")
        print()
        print("-"*80+"\n")

VoteChain = Blockchain([])

VerifiedPool = []
MaliciousPool = []

for T in [T1,T2,T3,T4,T5]:
    if T.ZKP_TransactionVerification() == True:
        VerifiedPool.append(T)
    else:
        MaliciousPool.append(T)

VoteBlock = Block("INITIAL HASH",VerifiedPool)
VoteChain.MineBlock(VoteBlock)