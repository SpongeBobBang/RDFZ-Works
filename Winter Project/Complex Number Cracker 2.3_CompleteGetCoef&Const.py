#Complex Number Cracker
#S3 Opt3 Stefan Yuzhao Heng, Matthew Yubo Rao 
#This program aim to solve 3 mindless typical complex number questions 
#Which are to simplify sin/cos(nθ); to simplify [sin/cos(θ)]^n; to get nth roots of an integer z. 

class Expoential():
	def __init__(self):
		self.angle = None
		self.expo = None
		self.subType= None
		print("e")

	def Set(self,θ,n,trig):
		self.angle = θ
		self.expo = n
		self.subType = trig
		self.resuNo = n//2+1
		self.numList = []
		self.coefList = []

	def GetConstant(self,args): #Get value in front of trig 
		if self.expo % 2 == 0:
			self.numList.append(Combination(self.expo,self.expo/2))
			self.resuNo -= 1
		for i in range(self.resultNo):
			self.numList.append(GetTermSign(subType,self.expo,self.resuNo+i+1)2*Combination(self.expo,self.resuNo+1+i))

	def GetVariedTerms(expo): #Number of terms except potential constant term
		return (expo+1)//2

	def GetCoefficient(self,args): #Get value inside trig 
		for i in range(GetVariedTerms(self.expo)):
			self.coefList.append(self.expo-2*i)
		self.coefList.reverse()

	def Output(self,args):
		if self.expo == 2:

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

def Factorial(x):
	if x == 1 or x == 0:
		return 1
	return x*Factorial(x-1)

def Combination(a,b):
	return Factorial(a)/(Factorial(b)*Factorial(a-b))

def GetTermSign(subType,a,b):
	dSinSign = {0:1,1:0}
	if subType == "cos":
		return 1
	elif subType == "Sin":
		return dSinSign[(a-b)%2]
	else:
		print("Error")

def InitializeName():
	global dKind, dTrig
	dKind = {1:Expoential,2:Coefficient,3:IntegerRoots}
	dExpoNum = {"cos":1,"sin":-1}
	dExpoCoef = {1:1,0:2}
	dComplexI = {0:False,1:True} #Whether there's a 'i'; Divivded by 2
	dComplexValue = {0:1,1:0,2:-1,3:-1} #Whether the number of 'i's makes up a -1; Divided by 4

def Main():
	InitializeName()
	kind = 1
	subType = "sin"
	q = dKind[kind]()

print(Combination(5,0))
Main()
