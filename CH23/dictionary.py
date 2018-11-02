nullP = -1

class Node:
	def __init__(self):
		self.listK = "N"
		self.listV = "N"
		self.nextP = nullP

class List:
	def __init__(self):
		self.space = 10
		self.record = []

		for i in range(self.space):
			newN = Node()
			newN.nextP = i+1
			self.record.append(newN)
		newN.nextP = nullP

	def OutputRecord(self):
		for i in range(10):
			print("[",self.record[i].listK,self.record[i].listV,self.record[i].nextP,"]")

	def Hash(self,value):
		temp = 0
		tempV = str(value)
		for i in range(len(tempV)):
			temp += ord(str(tempV[i]))
		return temp % (self.space)

	def InsertKey(self,newK,newV):
		currP = self.Hash(newV)
		print(currP)
		temp = 0
		while temp < self.space:
			if self.record[currP].listK == "N":
				self.record[currP].listK = newK
				self.record[currP].listV = newV
				break 
			temp += 1
			currP = self.record[currP].nextP
			if currP == nullP:
				currP = 0

	def findKey(self,requK):
		currP = self.Hash(requK)
		temp = 0
		while temp < self.space:
			if self.record[currP].listK == requK:
				return self.record[currP].listV
				break 
			temp += 1
			currP = self.record[currP].nextP
			if currP == nullP:
				currP = 0

l = List()

l.InsertKey(5,"ff")
l.InsertKey("e","sfds")
l.InsertKey(15,"d")
print()
l.OutputRecord()
print(l.findKey("e"))
