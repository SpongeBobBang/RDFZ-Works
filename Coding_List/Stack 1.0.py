#Stack:LIFO
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
        self.lastEndP = 0
        self.record = []
        
        for i in range(10):
            newNode = Node()
            newNode.nextP = i+1
            self.record.append(newNode)
        newNode.nextP = NP

    def AdministratorUpdateListValue(self,index,temp):
        self.record[index].listV = temp

    def OutputListPointer(self):
        print(self.startP,self.freeP,self.lastEndP)
    
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

    def ListPush(self,newV):
        self.startP = 0
        if self.freeP != NP:
            currP = self.freeP
            self.freeP = self.record[self.freeP].nextP
            self.record[currP].listV = newV
            print(self.record[currP].nextP)
            self.record[currP].nextP = NP
            print(self.record[currP].nextP)
            if currP != 0: #not for the first element
                print(self.lastEndP)
                self.record[self.lastEndP].nextP = currP
                self.lastEndP = currP

l = List()

l.OutputListPointer()
l.OutputRecord()
print()
#l.OutputList()
l.ListPush(3)
l.OutputListPointer()
l.OutputRecord()
print()
l.ListPush(27)
l.ListPush(10)
l.ListPush(6)
l.OutputListPointer()
l.OutputRecord()
l.OutputList()
