# Exam-Style Questions 
S3CS3 Stefan Yuzhao Heng

## 1 
a. 
![](./草图1.png 'e')

b.
```Python 
class bankAccount:
	def __init__(self,i):
		self.__accountHolderName = ''
		self.__IBAN = i

	def SetAccounrHolderName(self,n):
		self.__accountHolderName = n

	def GetAccountHolderName(self):
		return self.__accountHolderName 

	def GetIBAN(self):
		return self.__IBAN
```

c. 
i. 
Attributes: monthlyFee, overdraftLimit 
Methods: Constuctor, SetOVerdraftLimit, GetOverdraftLimit, GetMonthlyFee 

ii. 
Attributes: interestRate 
Methods: Constructor, GetInterestRate, FindInterestRate 

iii. 
Encapsulation 

## 2
a. 
EmailAddress: STRING 

GetTicketHolderName()
GetEmailAddress()

PRIVATE 
Amount: INTEGER 

PUBLIC 
Contructor(Name:STRING,Email:STRING)
GetAmount()
UpdateAmount()

PRIVATE 
MonthlyFee: INTEGER

PUBLIC
GetMonflyFee()

b. 
i. 
Attributes made private can nly be accessed and set through its class methods only 

ii. 
Private methods so to controll attributes. 

c. 
```Python
NewCustomer = ContractTicketHolder("A. Smith","xyz@abc.com",10)
```

## 3
a. 
Containment 

b. 
```Python 
class NodeClass:
	def __init__(self):
		self.__Data = ""
		self.__Pointer = -1 

	def SetData(self,d):
		self.__Data = d 

	def SetPointer(self,x):
		self.__Pointer = x

	def GetData(self):
		return self.__Data

	def GetPointer(self):
		return self.__Pointer 
```	

c. 
```Python
class QueueClass:
	def __init__(self):
		self.__Queue = [Nodeclass() for i in range(51)]
		self.__Head = -1
		self.__Tail = -1 
```

d. 
```Python 
	def JoinQueue(self,NewItem):
		if self.__Head == -1:
			self.__Head = 0
		self.__Tail += 1
		self.__Queue[i].SetItem(NewItem)
```
