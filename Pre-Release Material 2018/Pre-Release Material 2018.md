Pre-Release Material 2018
===
S3 CS3 Stefan Yuzhao Heng 

Task 1
--- 
1.1 
A structure set up based on structure of data the intended program is to handle. 
It can consist of elementary compenents and composite components. 

1.2 
- None: Sequence  
- Star: Repeated input, interation  
- Circle: Choice, selection  

1.3 
NOT EOF("Staff.txt")   
Salary > 50   
Salary >= 90   
Project manager    
Lead developer   
Manager   

1.4
... 
![](./草图1.png 'e')
...

1.5
...   
IF Salary >= 90   
	THEN    
		Role ← ProjectManager   
	ELSE   
		IF Salary > 70   
			THEN   
				Role ← Consultant   
			ELSE   
				Role ← LeadDeveloper   
		ENDIF   
ENDIF   
...    

1.6 
```Python
def FindRole(salary):
	if salary >= 90:
		return "Project Manager"
	elif salary > 70:
		return "Consultant"
	elif salary > 50:
		return "Lead Developer"
	else:
		return "Manager"
```

Task 2 
---
2.1 & 2.2
![](./草图2.png 'e')

Inheritance   
Where all attributes and methods of base class are copied to subclass 

2.3 
```Python 
class Toy:
	def __init__(self):
		self.__Name = ""
		self.__ID = ""
		self.__Price = 0
		self.__MinimumAge = 0

	def GetName(self):
		return self.__Name

	def GetID(self):
		return self.__ID

	def GetPrice(self):
		return self.__Price

	def GetMinimumAge(self):
		return self.__MinimumAge 

	def SetName(self,n):
		self.__Name = n

	def SetID(self,i):
		self.__ID = i 

	def SetPrice(self,p):
		self.__Price = p

	def SetMinimumAge(self,m):
		self.__MinimumAge = m
```

2.4 
```Python 
class ComputerGame:
	def __init__(self):
		Toy.__init__(self)
		self.__Category = ""
		self.__Console = ""

	def GetCategory(self):
		return self.__Category

	def GetConsole(self):
		return self.__Console 

	def SetCategory(self,c):
		self.__Category = c

	def SetConsole(self,c):
		self.__Console = c

class Vehicle:
	def __init__(self):
		Toy.__init__(self)
		self.__Type = ""
		self.__Height = 0
		self.__Length = 0
		self.__Weight = 0 

	def GetType(self):
		return self.__Type 

	def GetHeight(self):
		return self.__Height

	def GetLength(self):
		return self.__Length

	def GetWeight(self):
		return self.__Weight 

	def SetType(self,t):
		self.__Type = t

	def SetHeight(self,h):
		self.__Height = h

	def SetLength(self,l):
		self.__Length = l 

	def SetWeight(self,w):
		self.___Weight = w
```

2.5 
```Python
class Toy:
	def SetMinimumAge(self,m):
		while type(m) != int or (m>18 or m<0):
			m = input("Input minimum age: ")
		self.__MinimumAge = m

class ComputerGames:
	def SetCategory(self,c):
		while type(c) != str:
			c = input("Input category: ")
		self.__Category = c

class Vehicle:
	def SetHeight(self,h):
		while type(h) != int and type(h) != float:
			h = input("Input height: ")
		self.__Height = h

	def SetLength(self,l):
		while type(l) != int and type(l) != float:
			l = input("Input length: ")
		self.__Length = l

	def SetWeight(self,w):
		while type(w) != int and type(w) != float:
			w = input("Input weight: ")
		self.__Weight = w
```

2.6 
```Python
toyArray = []
newToy = Vehicle()
newToy.SetName("Red Sports Car")
newToy.SetID("RSC13")
newToy.SetMinimumAge(6)
newToy.SetType("Car")
newToy.SetHeight(3.3)
newToy.SetLength(12.1)
newToy.SetWeight(0.08)
toyArray.append(newToy)
```

2.7
```Python
class Toy:
	def PrintInfo(self):
		print(" Name:",self.__name)
		print(" ID:",self.__ID)
		print(" Price:",self.__Price)
		print(" Minimum age:",self.__MinimumAge)

class ComputerGame(self):
	def PrintInfo(self):
		print("Computer game:")
		toy.PrintInfo(self)
		print(" Category:",self.__Category)
		print(" Console:",self.__Console)

class Vehicle(self):
	def PrintInfo(self):
		print("Vehicle:")
		toy.PrintInfo(self)
		print(" Type:",self.__Type)
		print(" Height:",self.__Height)
		print(" Length:",self.__Length)
		print(" Weight:",self.__Weight)

def FindToy(ID):
	for i in toyArray:
		if i.GetID == ID:
			i.PrintInfo()
			break
	print("Requested toy not found")
```

2.8
```Python
import random 
class Toy:
	def Discount(self,d):
		self.__Price *= 1-d/100

def DiscountAll(d):
	toys = []
	for i in range(10):
		toys.append(ComputerGamme())
	for i in range(10):
		toys.append(Vehicle())
	for i in range(len(toys)):
		toys[i].setPrice(random.randint(1,200))
	for i in toys:
		i.Discount(d)

DiscountAll(10)
for i in range(len(toys)):
	i.PrintInfo()

```

2.9   
Bubble sort is a sort method where adjacent pairs of values are compared & swapped.    
Insertion sort is a sort method where values a inserted into a stack one by one.   
In insertion sort elements are bubbled into the sorted section, while in bubble sort the maximums are bubbled out of the unsorted section.   

2.10 
```Python 
sortedToys = [0 for i in range(len(toys))]
sortedToys[0] = toys[0]
for i in range(1,len(toys)):
	newToy = toys[i]
	currP = currP - 1
	while sortedToy[currP].GetPrice() > newToy.GetPrice() and currP >= 0:
		sortedToy[currP+1] = sortedToy[currP]
		currP = currP -1
	sortedToy[currP+1] = newToy
for i in sortedToys:
	i.PrintInfo()
```

Task 3
---
3.1 
```Prolog
character(habib).
charcater_type(habib,explorer).
has_skill(habib,timetravel).
pet(habib,fish).
```

3.2
```Prolog
onlyPet(C,P) :-
	character(C),animal(P).
```

3.3
```Prolog
character(stefan).
character(elena).
animal(cat).
animal(dog).
pet(stefan,cat).
pet(elena,dog).
has_skill(stefan,heal).
has_skill(elana,dance).
```

3.4
```Prolog
True.
X = princess.
X = jim.
X = invisibility.
X = jim.
```

3.5
```Prolog
pet(jim,X).
has_skill(X,fly).
skill(X).

type_pet(T,P) :-
	character_type(C,T),pet(C,P).

type_pet(princess,X).
```
