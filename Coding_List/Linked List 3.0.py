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
        for i in range(10):
            print(self.record[i].listV,self.record[i].nextP)
    
    def OutputList(self):
        currP = self.startP
        print("[",end="")
        while currP != NP:
            print(self.record[currP].listV,end=",")
            currP = self.record[currP].nextP
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

    def FindListValue(self,requestV):
        currP = self.startP
        while currP != NP and self.record[currP].listV != requestV:
            currP = self.record[currP].nextP
        return(currP)

    def DeleteListValue(self,requestV):
        currP = self.startP
        while currP != NP and self.record[currP].listV != requestV:
            prevP = currP
            currP = self.record[currP].nextP
        if currP != NP:
            if currP == self.startP:
                self.startP = self.record[self.startP].nextP
            else:
                self.record[prevP].nextP = self.record[currP].nextP
            self.record[currP].nextP = self.freeP
            self.freeP = currP

l = List()

l.InsertListValue(5)
l.InsertListValue(25)
l.InsertListValue(15)
l.InsertListValue(35)

l.OutputRecord()
l.OutputList()

print(l.FindListValue(2))
print(l.FindListValue(15))

l.DeleteListValue(25)
l.OutputList()
