#Complex Number Cracker
#S3 Opt3 Stefan Yuzhao Heng, Matthew Yubo Rao 
#This program aim to solve 3 mindless typical complex number questions 
#Which are to to simplify [sin/cos(θ)]^n; simplify sin/cos(nθ); to get nth roots of an integer z. 

from fractions import Fraction

class Expoential():
	def __init__(self,trigType,expo):
		self.trigType = trigType
		self.expo = expo
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
		print("["+str(self.trigType)+"(θ)]^"+str(self.expo)+" =",end=" ")
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
	def __init__(self,trigType,coef):
		self.trigType = trigType
		self.coef = coef
		self.termNoTotal = self.coef + 1 #Total number of terms, real & imaginary 
		self.termNoSub = None
		self.coefListTot = [] #Coefficient list, of Re&Im  
		self.coefListCos = [] #Coef list, of Re parts 
		self.coefListSin = [] #Coef list, of Im parts 
		self.coefListA = [] #Coef list with joint variable: sin&cos, initially/Coef list at numerator for tan
		self.coefListB = [] #Coef list with simplified, sole variable, finally/Coef list at denominator for tan

	def GetCoefListSub(self):
		dCoefSign = {1:1,2:1,3:-1,0:-1}
		for i in range(self.termNoTotal):
			self.coefListTot.append(dCoefSign[(i+1)%4]*Combination(self.coef,i))
		dGoTrig = {"cos":self.GetCoefListCos,"sin":self.GetCoefListSin,"tan":self.GetCoefListTan}
		dGoTrig[self.trigType]()


	def GetCoefListCos(self):
		for i in range(0,self.termNoTotal,2):
			self.coefListCos.append(self.coefListTot[i])
		self.coefListA = self.coefListCos

	def GetCoefListSin(self):
		for i in range(1,self.termNoTotal,2):
			self.coefListSin.append(self.coefListTot[i])
		self.coefListA = self.coefListSin

	def GetCoefListTan(self):
		self.GetCoefListCos()
		self.GetCoefListSin()
		self.coefListB = self.coefListSin

	def Output(self):
		print(self.coefListA)
		print(self.coefListB)


	def SubMain(self):
		if (self.trigType == "cos" and self.coef%2 == 1) or (self.trigType == "sin" and self.coef%2 == 0):
			print("Result not supported") #The 2 cases above can not derive an answer as required 
			return
		self.GetCoefListSub()
		self.Output()

class IntegerRoots():
	def __init__(self,intZ,rootD):
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
	print("Welcome to CN Cracker++. Type in the kind of quetions you want to slove.")
	print("1:Expoential; 2:Coefficient; 3:IntegerRoots")
	kind = 2
	dPrompt = {1:"Trignometry; Exponent",2:"Trignometry; Coefficient",3:"Integer Z; Degree of roots"} #Inform variables needed 
	print("Please input the subvariables for type "+str(kind)+": "+dPrompt[kind])
	subKindVar1 = "cos"
	subKindVar2 = 8
	dKind = {1:Expoential,2:Coefficient,3:IntegerRoots} #Return corresponding class procedure for varied question kind
	q = dKind[kind](subKindVar1,subKindVar2)
	q.SubMain() #Subfunctions of same name allowing easy calls

Main()
