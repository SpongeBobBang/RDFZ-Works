#Complex Number Cracker
#S3 Opt3 Stefan Yuzhao Heng, Matthew Yubo Rao 
#This program aim to solve 3 mindless typical complex number questions 
#Which are to simplify sin/cos(nθ); to simplify [sin/cos(θ)]^n; to get nth roots of an integer z. 

class QTypes():
	def __init__(self):
		self.type = None
		self.angle = None
		self.expo = None
		self.coef = None
		self.rootNo = None
		self.intZ = None

	def Exponential(self,θ,n):
		self.angle = θ
		self.expo = n

	def Coefficient(self,θ,n):
		self.angle = θ
		self.expo = n

	def IntegerRoots(self,z,n):
		self.intZ = z
		self.rootNo = n

def Main():
	