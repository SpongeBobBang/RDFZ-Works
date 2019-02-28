#S3 Opt3 Stefan Yuzhao Heng
NP = -1

class Node:
    def __init__(self):
        self.listV = "None"
        self.nextP = NP

class List:
    def __init__(self):
        self.startP = NP
        self.freeP = 0
        self.record = []
        newNode = None
        
        for i in range(10):
            newNode = Node()
            newNode.nextP = i+1
            self.record.append(newNode)
        newNode.nextP = NP

    def AdministratorUpdateListValue(self,index,temp):
        self.record[index].listV = temp

    def OutputRecord(self):
        print("[",end="")
        for i in range(10):
            print("[",self.record[i].listV,",",self.record[i].nextP,"]")
        print("]")
    
    def OutputList(self):
        CP = self.startP
        print("[",end="")
        while CP != NP:
            print(self.record[CP].listV,end=",")
            CP = self.record[CP].nextP
        print("]")

    def InsertListValue(self,newV):
        if self.freeP != NP:
            newP = self.freeP
            self.record[newP].listV = newV
            self.freeP = self.record[self.freeP].nextP
            prevP = NP
            currP = self.startP
            while currP != NP and self.record[currP].listV < newV:
                prevP = currP
                currP = self.record[currP].nextP
            if prevP == NP:
                self.record[newP].nextP = self.startP
                self.startP = newP
            else:
                self.record[newP].nextP = self.record[prevP].nextP
                self.record[prevP].nextP = newP

l = List()

l.InsertListValue(5)
l.InsertListValue(25)
l.InsertListValue(15)
l.InsertListValue(35)

l.OutputRecord()
l.OutputList()
