nullP = -1

class Node:
	def __init__(self):
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
			print("[",self.record[i].listV,self.record[i].nextP,"]")

	def Hash(self,key):
		return key % (self.space)

	def InsertKey(self,newK):
		currP = self.Hash(newK)
		print(currP)
		temp = 0
		while temp < self.space:
			if self.record[currP].listV == "N":
				self.record[currP].listV = newK
				break 
			temp += 1
			currP = self.record[currP].nextP
			if currP == nullP:
				currP = 0

	def findKey(self,requK):
		currP = self.Hash(requK)
		temp = 0
		while temp < self.space:
			if self.record[currP].listV == requK:
				return currP
				break 
			temp += 1
			currP = self.record[currP].nextP
			if currP == nullP:
				currP = 0



l = List()

l.InsertKey(5)
l.InsertKey(7)
l.InsertKey(15)
print()
print(l.findKey(15))