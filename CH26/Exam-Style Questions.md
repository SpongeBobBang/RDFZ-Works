Exam-Style Questions 
===
S3CS3 Stefan Yuzhao Heng 

1
---
a. 
i. 
```Python 
class costomerRecord:
	def __init__(self):
		customerID = 0
		customerName = ""
		PhoneNo = 0
		orderValue = 0
```

ii. 
```Python 
costomerData = [costomerRecord for i in range(1000)]
```

b. 
i. 
```Python 
def Hash(ID):
	return ID % 1000
```

ii. 
```Python
def AddRecord(costomer):
	address = Hash(costomer.customerID)
	while costumerData[address].customerID != 0:
		address += 1
		if address == 1000:
			address = 0
	costomerData[address] = costomer 
```

iii. 
```Python 
def FindRecord(costomerID):
	address = Hash(costomerID)
	while costomerData[address].costomerID != costomerID:
		address += 1
		if address == 1000:
			address = 0
	return address
```

c. 
```Python 
import pickle 

def StoreRecord():
	costomerFile = open("CustomerData.DAT","wb")
	for i in range(1000):
		pickle.dump(customerData[i],costomerFile)
	costomerFile.close()
```

d. 
They need to set up records in fixed length and saved them to a random file. 
AddRecord and FindRecord needs access to the file, which both take calculations to get to correct address location; StoreRecord isn't needed. 

2
---
```Python 
requFile = input("Which file do you want to use? ")
try:
	file = open(requFile,"rb+")
except:
	print("File not found")
```
