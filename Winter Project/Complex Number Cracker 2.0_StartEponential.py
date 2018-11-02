#Complex Number Cracker
#S3 Opt3 Stefan Yuzhao Heng, Matthew Yubo Rao 
#This program aim to solve 3 mindless typical complex number questions 
#Which are to simplify sin/cos(nθ); to simplify [sin/cos(θ)]^n; to get nth roots of an integer z. 

class Expoential():
	def __init__(self,θ,n):
		self.angle = None
		self.expo = None
		self.subType= None

	def Set(self,θ,n,trig):
		self.angle = θ
		self.expo = n
		self.subType = trig
		self.resuNo = n//2+1
		self.numList = []

	def Get(self,args):
		if n % 2 == 0:
			self.constantTerm = Combination(n,n/2)
			self.resuNo -= 1
			self.numList.append(constantTerm)
		for i in range(resultNo):
			self.numList.append(Combination(n,i))

class Coefficient():
	def __init__(self,θ,n):
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

def Main():
	kind = 1
	subType = "sin"

print(Combination(5,0))
