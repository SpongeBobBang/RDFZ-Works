print(8%4)
print(7%4)
print("---------------------------------")

class Try():
	def __init__(self):
		self.a = "sin"

	def GoCos(self):
		print("GoCos")

	def GoSin(self):
		print("GoSin")

	def Go(self):
		dGoTrig = {"cos":self.GoCos,"sin":self.GoSin}
		dGoTrig[self.a]()

t = Try()
t.Go()
print("---------------------------------")

def TryPrint():
	print("a")
	return 
	print("b")

TryPrint()
print("---------------------------------")

print(9//2)
print(10//2)
print("---------------------------------")

