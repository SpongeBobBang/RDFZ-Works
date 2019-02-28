#S3 Opt3 Stefan Yuzhao Heng
NP = -1

class Node:
    def __init__(self):
        self.value = " "
        self.nextP = NP

class List:
    def __init__(self):
        self.freeP = 0
        self.startP = 0
        self.record = []
        
        for i in range(10):
            newNode = Node()
            newNode.nextP = i+1
            self.record.append(newNode)
        newNode.nextP = NP
    
    def OutputNodes(self):
        CP = self.startP
        while CP != NP:
            print(self.record[CP].value,end=",")
            CP = self.record[CP].nextP
        print()

    def UpdateValue(self,index,temp):
        self.record[index].value = temp

l = List()
print(l.record)

l.UpdateValue(0,"I")
l.UpdateValue(1,"am")

l.OutputNodes()
