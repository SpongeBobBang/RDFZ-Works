#Complex Number Cracker
#S3 Opt3 Stefan Yuzhao Heng, Matthew Yubo Rao 
#This program aim to solve 3 mindless typical complex number questions 
#Which are to simplify sin/cos(nθ); to simplify [sin/cos(θ)]^n; to get nth roots of an integer z. 

class Expoential():
	def __init__(self,θ,n):
		self.angle = None
		self.expo = None

	def set(self,θ,n):
		self.angle = θ
		self.expo = n
		

class Coefficient():
	def __init__(self,θ,n):
		self.angle = None
		self.coef = None

	def set(self,θ,n):
		self.angle = θ
		self.coef = n

class IntegerRoots():
	def __init__(self):
		self.intZ = None
		self.rootNo = None

	def set(self,z,n):
		self.intZ = z
		self.rootNo = n

def Main():
	type = 1
	if type == 1:

