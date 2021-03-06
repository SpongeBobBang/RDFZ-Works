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
        self.prevEndP = 0
        self.currEndP = 0 
        self.record = []
        
        for i in range(10):
            newNode = Node()
            newNode.nextP = i+1
            self.record.append(newNode)
        newNode.nextP = NP

    def AdministratorUpdateListValue(self,index,temp):
        self.record[index].listV = temp

    def OutputListPointer(self):
        print(self.startP,self.freeP,self.currEndP)
    
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
            self.record[currP].nextP = NP
            if currP != 0: #not for the first element
                self.prevEndP = self.currEndP
                self.record[self.currEndP].nextP = currP
                self.currEndP = currP

    def ListPop(self):
        self.record[self.prevEndP].nextP = NP
        

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
l.ListPop()
l.ListPop()
l.OutputList()
