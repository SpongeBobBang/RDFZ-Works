#S3 Opt3 Stefan Yuzhao Heng
NP = -1

class Node:
    def __init__(self):
        self.value = " "
        self.nextP = NP

class List:
    def __init__(self):
        self.FP = 0
        self.SP = NP
        self.record = []
        
        for i in range(10):
            newNode = Node()
            newNode.nextP = i+1
            self.record.append(newNode)
        newNode.nextP = NP

List = List()
print(List.record)
