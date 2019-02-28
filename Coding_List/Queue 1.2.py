#Queue:FIFO
#S3 Opt3 Stefan Yuzhao Heng

NP = -1

class Node:
    def __init__(self):
        self.listV = "N"
        self.nextP = NP

class List:
    def __init__(self):
        self.startP = NP
        self.freeP = 0
        self.endP = NP
        self.record = []
        
        for i in range(10):
            newNode = Node()
            newNode.nextP = i+1
            self.record.append(newNode)
        newNode.nextP = NP

    def OutputListPointer(self):
        print(self.startP,self.freeP,self.endP)
    
    def OutputRecord(self):
        for i in range(10):
            print("[",self.record[i].listV,self.record[i].nextP,"]")
    
    def OutputList(self):
        currP = self.startP
        print("[",end="")
        while currP != NP:
            print(self.record[currP].listV,end=",")
            currP = self.record[currP].nextP
        print("]")

    def ListEnqueue(self,newV):
        if self.freeP != NP:
            newP = self.freeP
            self.freeP = self.record[self.freeP].nextP
            self.record[newP].listV = newV
            self.record[newP].nextP = NP
            if self.endP == NP:
                self.startP = newP
            else:
                self.record[self.endP].nextP = newP
            self.endP = newP
        else:
            print("No more space")

    def GetListEnd(self):
        currP = self.startP
        while self.record[currP].nextP != NP:
            currP = self.record[currP].nextP
        return currP

    def GetOriginalNextPointer(self,currP):
        for i in range(10):
            if currP == self.record[i].lastP:
                return(i)
    
    def ListDequeue(self):
        if self.startP != NP:
            currP = self.record[self.startP].nextP
            if currP == NP:
                self.endP = NP
            self.record[self.startP].nextP = self.freeP
            self.freeP = self.startP
            self.startP = currP

l = List()

l.ListEnqueue(3)
l.ListEnqueue(7)
l.ListEnqueue(10)
l.ListEnqueue(6)
l.OutputList()
print()
l.ListDequeue()
l.OutputList()
print()
l.ListEnqueue(4)
l.OutputList()
print()
l.ListDequeue()
l.OutputList()
