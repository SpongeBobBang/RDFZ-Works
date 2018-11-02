#Complex Number Cracker
#S3 Opt3 Stefan Yuzhao Heng, Matthew Yubo Rao 
#This program aim to solve 3 mindless typical complex number questions 
#Which are to to simplify [sin/cos(θ)]^n; simplify sin/cos(nθ); to get nth roots of an integer z. 

from fractions import Fraction

class Expoential():
	def __init__(self,trig,expo):
		self.expo = expo
		self.trigType = trig
		self.termNo = self.expo//2+1 #Nuber of terms including potential constant value term
		self.variedTermNo = (self.expo+1)//2 #Number of terms except potential constant value term
		self.constList = [] #Value in front of trig 
		self.coefList = []  #Value inside trig 
		self.termList = []
		self.heading = ""
		self.constValue = None

	def GetHeading(self):
		dHeadingI = {0:False,1:True} #Whether there's a 'i'; Divivded by 2
		dHeadingSign = {0:"",1:"",2:"-",3:"-"} #Whether the number of 'i's makes up a -1; Divided by 4
		if dHeadingI[self.expo%2]: #'i' present
			self.heading = dHeadingSign[self.expo%4]+"i"+"·"
		else:
			self.heading = dHeadingSign[self.expo%4]

	def GetTermSign(self,trigType,a,b):
		dSinSign = {0:1,1:-1} #For sins, a negative sign between brackets result in signs dependent on individual exponent
		if trigType == "cos":
			return 1
		elif trigType == "sin":
			return dSinSign[(a-b)%2]

	def GetConstant(self):
		start = self.variedTermNo
		if self.termNo != self.variedTermNo: #There's a constant value term 
			self.constValue = Fraction(int(self.GetTermSign(self.trigType,self.expo,self.expo/2)*Combination(self.expo,self.expo/2)),Power(2,self.expo))
			start += 1
		for i in range(self.variedTermNo):
			self.constList.append(Fraction(int(self.GetTermSign(self.trigType,self.expo,start+i)*2*Combination(self.expo,start+i)),Power(2,self.expo)))

	def GetCoefficient(self):
		for i in range(self.variedTermNo):
			self.coefList.append(self.expo-2*i)
		self.coefList.reverse()

	def GetTerm(self):
		self.termList.append(self.heading)
		if self.termNo != self.variedTermNo: #There's a constant value term
			self.termList.append(str(self.constValue))
		for i in range(self.variedTermNo):
			self.termList.append(str(self.constList[i])+"cos"+str(self.coefList[i])+"θ")

	def Output(self):
		dDeviation = {0:2,1:1} #To correspond constant index to term index dependent on presence of contant value 
		print(self.heading+"{",end="")
		if self.termNo != self.variedTermNo: #There's a constant value term
			print(self.termList[1],end=" ")
		for i in range(self.variedTermNo):
			if self.constList[i] > 0:
				print("+"+self.termList[i+dDeviation[self.expo%2]],end=" ")
			else:
				print(self.termList[i+dDeviation[self.expo%2]],end=" ")
		print("}")

	def SubMain(self):
		self.GetHeading()
		self.GetConstant()
		self.GetCoefficient()
		self.GetTerm()
		self.Output()

class Coefficient():
	def __init__(self):
		self.angle = None
		self.coef = None

	def Set(self,trig,coef):
		self.angle = θ
		self.coef = coef

class IntegerRoots():
	def __init__(self):
		self.intZ = None
		self.rootNo = None

	def Set(self,intZ,rootD):
		self.intZ = intZ
		self.rootD = rootD

#External Functions for kind = 1
def Factorial(x):
	if x == 1 or x == 0:
		return 1
	return x*Factorial(x-1)

def Combination(a,b):
	return Factorial(a)/(Factorial(b)*Factorial(a-b))

def Power(base,expo):
	if expo == 0:
		return 1
	else:
		return base*Power(base,expo-1)
#--------------------------------
def Main():
	print("Welcome to Complex Number Cracker. Type in the kind of quetions you want to slove.")
	print("1:Expoential; 2:Coefficient; 3:IntegerRoots")
	kind = 1
	dPrompt = {1:"Trignometry; Exponent",2:"Trignometry; Coefficient",3:"Integer Z; Degree of roots"} #Inform variables needed 
	print("Please input the subvariables for type "+str(kind)+":"+dPrompt[kind])
	subKindVar1 = "sin"
	subKindVar2 = 6
	dKind = {1:Expoential,2:Coefficient,3:IntegerRoots} #Return corresponding class procedure for varied question kind
	q = dKind[kind](subKindVar1,subKindVar2)
	q.SubMain() #Subfunctions of same name allowing easy calls

Main()
