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