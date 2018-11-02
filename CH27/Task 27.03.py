#Task 27.03
#S3CS3 Stefan Yuzhao Heng

class borrower:
	def __init__(self):
		self.__borrowerName = ""
		self.__emailAddress = ""
		self.__borrowerID = None 
		self.__itemsOnLoan = 0 

	def __repr__(self):
		return "Name: %s; Addr: %s; ID: %s; onLoan: %d" %(self.__borrowerName, self.__emailAddress, self.__borrowerID, self.__itemsOnLoan)

	def GetBorrowerName(self):
		return self.__borrowerName

	def GetEmailAddress(self):
		return self.__emailAddress

	def GetBorrwerID(self):
		return self.__borrowerID

	def GetItemsOnLoan(self):
		return self.__itemsOnLoan 

	def UpdateItemsOnLoan(self):
		self.__itemsOnLoan += 1

	def PrintDetails(self):
		print(self.__borrowerName,"")


a = borrower()
a.UpdateItemsOnLoan()
print(a)
