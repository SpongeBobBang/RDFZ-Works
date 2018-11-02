from fractions import Fraction

class hah():
	def __init__(self):
		self.temp = 2
		self.a = {"1":2,"ee":self.mult}

	def mult(self,n):
		return self.temp*n

print(Fraction(12,10))
b = hah()
print(b.a["ee"](3))