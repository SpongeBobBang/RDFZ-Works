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

		self.termNoTotal = self.coef + 1 #Total term number, real & imaginary 
		self.termNoA = None #Term number for cos or sin, with integer in output/Term No at numerator for tan 
		self.termNoB = None #Term No at denominator for tan 
		self.constListTot = [] #Constant list, of Re & Im  
		self.constListCos = [] #Const list, of Re parts 
		self.constListSin = [] #Const list, of Im parts 
		self.constListA = [] #Const list with joint trigonometry: cos & sin, initially/Const list at numerator for tan
		self.constListB = [] #Const list with simplified, sole trig, finally/Const list at denominator for tan
		self.expoListA = [] #Exponent list for sin & cos/Expo list for numerator for tan 
		self.expoListB = [] #Expo list for denominator for tan 

	def GetTermNo(self):
		self.termNoA = len(self.constListA)

	def GetConstListA(self):
		dConstSignA = {1:1,2:1,3:-1,0:-1}
		for i in range(self.termNoTotal):
			self.constListTot.append(dConstSignA[(i+1)%4]*Combination(self.coef,i))
		dGoTrig = {"cos":self.GetConstListCosA,"sin":self.GetConstListSinA,"tan":self.GetConstListTanA}
		dGoTrig[self.trigType]()

	def GetConstListCosA(self):
		for i in range(0,self.termNoTotal,2):
			self.constListCos.append(self.constListTot[i])
		self.constListA = self.constListCos

	def GetConstListSinA(self):
		for i in range(1,self.termNoTotal,2):
			self.constListSin.append(self.constListTot[i])
		self.constListSin.reverse()
		self.constListA = self.constListSin

	def GetConstListTanA(self):
		self.GetConstListCos()

	def GetConstListB(self):
		dGoTrig = {"cos":self.GetConstListCSB,"sin":self.GetConstListCSB,"tan":self.GetConstListTanB}
		dGoTrig[self.trigType]()

	def GetConstListCSB(self): #For cos&sin, to eliminate the other trig
		dConstSignB = {0:1,1:-1}
		for i in range(self.termNoA):
			temp = 0
			t = 0 
			for j in range(i,self.termNoA):
				temp += dConstSignB[t%2]*Combination(j,i)*self.constListA[j]
				t += 1
			self.constListB.append(temp)

	def GetConstListTanB(self):
		self.GetConstListSin()
		self.constListB = self.constListSin

	def GetCoefList(self):
		for i in range(self.termNoA):
			self.expoListA.append(self.coef - i*2)


	def Output(self):
		print(self.constListA)
		print(self.constListB)

	def SubMain(self):
		if (self.trigType == "cos" and self.coef%2 == 1) or (self.trigType == "sin" and self.coef%2 == 0): #Case check
			print("Result not supported") #The 2 cases above can not derive an answer as required 
			return
		self.GetConstListA()
		self.GetTermNo()
		self.GetConstListB()
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
	subKindVar1 = "sin"
	subKindVar2 = 5
	dKind = {1:Expoential,2:Coefficient,3:IntegerRoots} #Return corresponding class procedure for varied question kind
	q = dKind[kind](subKindVar1,subKindVar2)
	q.SubMain() #Subfunctions of same name allowing easy calls

Main()
