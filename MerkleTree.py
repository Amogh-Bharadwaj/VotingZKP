from hashlib import sha256
from random import randint
from Transaction import Transaction
# In bitcoin, block information is stored as a hash. To achieve this, the transactions of the block
# are run through an algorithm to get a merkle root. In this process, each transactions is hashed 
# and the hashed transactions make up the leaves of the merkle tree.
# The leaves are then paired up and hashed to form the next nodes. This happens recursively.
# In the end we will end up with one node (the parent of the binary merkle tree) which is known as the merkle root.
# The merkle root represents the hashed block.


#SHA256 hash function. Output is a bytes object.
def nodeHash(node):
    return sha256(node).digest()

#Recursive hashing to get merkle root.
def MerkleRoot(state):
    state_size=len(state)
    
    #Reject empty states.
    if state_size==0:
        return "stateError: Empty leaf state."
    
    # All leaves converged to one parent which is the merkle root.
    if state_size==1:
       
        return state[0]
        
    node_state=[]

    for i in range(0,state_size-1,2):
        node_state.append(nodeHash(state[i]+state[i+1]))
    
    return MerkleRoot(node_state)

def MerkleHash(transactions):
    #Hashing the transactions  to form the leaves.
    leaves = []
    print("Transactions to be hashed: ", transactions)
    for t in transactions:
        leaves.append(nodeHash(str(t.voter.publicKnowledge + t.candidate).encode())) 

    #If number of leaves is odd, the last leaf is duplicated.
    if len(leaves)%2==1:
        leaves.append(leaves[-1])
    
    return MerkleRoot(leaves).hex()