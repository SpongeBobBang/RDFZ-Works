from fractions import Fraction
print(Fraction(12,10))
print("---------------------------------")

class hah():
	def __init__(self):
		self.temp = 2
		self.a = {"1":2,2:self.mult}

	def mult(self,n):
		return self.temp*n

class heh():
	def __init__(self):
		self.temp = 3

	def set(self,n):
		return n

dic = {"a":hah,"e":heh}
b = hah()
print(b.a[2](3))

test = dic["a"]()
print(test.mult(4))
print("---------------------------------")

print(5//2,6//2)
print(5%2,6%2)
print("ee"+"aa")
print([None for i in range(5)])
print("---------------------------------")

a=['1','2','3','4','5']
a.reverse()
print(a)
print("---------------------------------")
