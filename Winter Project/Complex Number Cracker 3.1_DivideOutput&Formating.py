#Complex Number Cracker
#S3 Opt3 Stefan Yuzhao Heng, Matthew Yubo Rao 
#This program aim to solve 3 mindless typical complex number questions 
#Which are to simplify sin/cos(nθ); to simplify [sin/cos(θ)]^n; to get nth roots of an integer z. 

class Expoential():
	def __init__(self):
		self.angle = None
		self.expo = None
		self.subType= None

	def Set(self,trig,n):
		self.expo = n
		self.subType = trig
		self.termNo = self.expo//2+1 #Nuber of terms including potential constant value term
		self.variedTermNo = (self.expo+1)//2 #Number of terms except potential constant value term
		self.constList = [] #Value in front of trig 
		self.coefList = []  #Value inside trig 
		self.termList = []
		self.heading = ""
		self.constValue = None

	def GetConstant(self):
		start = self.variedTermNo
		if self.termNo != self.variedTermNo: #There's a constant value term 
			self.constValue = int(GetTermSign(self.subType,self.expo,self.expo/2)*Combination(self.expo,self.expo/2))
			start += 1
		for i in range(self.variedTermNo):
			self.constList.append(int(GetTermSign(self.subType,self.expo,start+i)*2*Combination(self.expo,start+i)))

	def GetCoefficient(self):
		for i in range(self.variedTermNo):
			self.coefList.append(self.expo-2*i)
		self.coefList.reverse()

	def GetHeading(self):
		dHeadingI = {0:False,1:True} #Whether there's a 'i'; Divivded by 2
		dHeadingSign = {0:"",1:"",2:"-",3:"-"} #Whether the number of 'i's makes up a -1; Divided by 4
		if dHeadingI[self.expo%2]: #'i' present
			self.heading = dHeadingSign[self.expo%4]+"i"+"·"
		else:
			self.heading = dHeadingSign[self.expo%4]

	def GetTerm(self):
		self.termList.append(self.heading)
		if self.termNo != self.variedTermNo: #There's a constant value term
			self.termList.append(str(self.constValue))
		for i in range(self.variedTermNo):
			self.termList.append(str(self.constList[i])+"cos"+str(self.coefList[i])+"θ")

	def Output(self):
		dDeviation = {0:2,1:1}
		print(self.termList)
		print(self.heading+" {",end="")
		for i in range(self.variedTermNo):
			if self.constList[i] > 0:
				print("+"+self.termList[i+dDeviation[self.expo%2]],end=" ")
			else:
				print(self.termList[i+dDeviation[self.expo%2]],end=" ")
		print("}")

	def SubMain(self):
		self.GetHeading()
		print(self.heading)
		self.GetConstant()
		print(self.constList)
		self.GetCoefficient()
		print(self.coefList)
		self.GetTerm()
		self.Output()

class Coefficient():
	def __init__(self):
		self.angle = None
		self.coef = None

	def Set(self,θ,n):
		self.angle = θ
		self.coef = n

class IntegerRoots():
	def __init__(self):
		self.intZ = None
		self.rootNo = None

	def Set(self,z,n):
		self.intZ = z
		self.rootNo = n

#External Functions for kind = 1
def Factorial(x):
	if x == 1 or x == 0:
		return 1
	return x*Factorial(x-1)

def Combination(a,b):
	return Factorial(a)/(Factorial(b)*Factorial(a-b))

def GetTermSign(subType,a,b):
	dSinSign = {0:1,1:-1}
	if subType == "cos":
		return 1
	elif subType == "sin":
		return dSinSign[(a-b)%2]
#--------------------------------
def InitializeName():
	global dKind, dTrig
	dKind = {1:Expoential,2:Coefficient,3:IntegerRoots}
	dExpoCoef = {1:1,0:2}

def Main():
	InitializeName()
	kind = 1
	subType = "sin"
	n = 7
	q = dKind[kind]()
	q.Set(subType,n)
	q.SubMain()

Main()
