#S3 Opt3 Stefan Yuzhao Heng
global NP 
global SP
NP = -1

class Node:
    def __init__(self):
        self.Value = ""
        self.Next = NP

def InitializeList():
    List = [Node() for i in range(10)]
    SP = NP
    FP = 0
    for i in range(9):
        List[i].Next = i + 1
    List[9].Next = NP
    print(List)
    print(SP,FP)

def OutputNodes():
    
    CP = 0
    while CP != NP:
        print(List[CP].Value)
        CP = List[CP].Next
            
InitializeList()
OutputNodes()
