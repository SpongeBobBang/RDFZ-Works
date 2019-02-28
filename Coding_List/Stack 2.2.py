#Stack:LIFO
#S3 Opt3 Stefan Yuzhao Heng

NP = -1

class Node:
    def __init__(self):
        self.listV = "N"
        self.nextP = NP
        self.lastP = "N"

class List:
    def __init__(self):
        self.startP = NP
        self.freeP = 0
        self.record = []
        
        for i in range(10):
            newNode = Node()
            newNode.nextP = i+1
            if i != 0:
                newNode.lastP = i-1
            self.record.append(newNode)
        newNode.nextP = NP

    def OutputListPointer(self):
        print(self.startP,self.freeP)
    
    def OutputRecord(self):
        for i in range(10):
            print("[",self.record[i].listV,self.record[i].nextP,self.record[i].lastP,"]")
    
    def OutputList(self):
        currP = self.startP
        print("[",end="")
        while currP != NP:
            print(self.record[currP].listV,end=",")
            currP = self.record[currP].nextP
        print("]")

    def ListPush(self,newV):
        self.startP = 0
        if self.freeP != NP:
            currP = self.freeP
            self.freeP = self.record[self.freeP].nextP
            self.record[currP].listV = newV
            self.record[currP].nextP = NP
            if currP != 0:
                self.record[self.record[currP].lastP].nextP = currP

    def GetListEnd(self):
        currP = self.startP
        while self.record[currP].nextP != NP:
            currP = self.record[currP].nextP
        return currP

    def GetOriginalNextPointer(self,currP):
        for i in range(10):
            if currP == self.record[i].lastP:
                return(i)
    
    def ListPop(self):
        if self.startP != NP:
            currP = self.GetListEnd()
            self.record[currP].nextP = self.GetOriginalNextPointer(currP)
            self.record[self.record[currP].lastP].nextP = NP
            self.freeP = currP
            if currP == 0:
                self.startP = NP

l = List()

l.ListPush(3)
l.ListPush(7)
l.ListPush(10)
l.ListPush(6)
l.OutputList()

l.ListPop()
l.OutputList()

l.ListPush(9)
l.ListPush(22)
l.ListPush(30)
l.OutputList()

l.ListPop()
l.OutputList()
