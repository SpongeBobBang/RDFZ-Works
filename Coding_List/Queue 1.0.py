#Queue:FIFO
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

    def ListEnqueue(self,newV):
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
    
    def ListDequeue(self):
        if self.startP != NP:
            prevP = self.startP
            self.record[self.startP].listV = "N"
            self.startP = self.record[prevP].nextP
            self.freeP = prevP
            '''
            currP = self.GetListEnd()
            self.record[currP].nextP = self.GetOriginalNextPointer(currP)
            self.record[self.record[currP].lastP].nextP = NP
            self.freeP = currP
            if currP == 0:
                self.startP = NP
            '''

l = List()

l.ListEnqueue(3)
l.ListEnqueue(7)
l.ListEnqueue(10)
l.ListEnqueue(6)
l.OutputListPointer()
l.OutputRecord()
l.OutputList()
print()
l.ListDequeue()
l.OutputListPointer()
l.OutputRecord()
l.OutputList()
print()
l.ListEnqueue(4)
l.OutputListPointer()
l.OutputRecord()
l.OutputList()
