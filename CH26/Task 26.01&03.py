#Task 26.01&03
#S3 CS3 Stefan Yuzhao Heng
class CarRecord:
	def __init__(self):
		self.VehicleID = ""
		self.Registration = ""
		self.DateOfRegistration = None
		self.EngineSize = 0 
		self.PurchasePrice = 0.00

Car = []
for i in range(10):
	newCar = CarRecord()
	newCar.EngineSize = 2500
	Car.append(newCar)
Car[9].EngineSize = 123

import pickle

CarFile = open('Cars.DAT','wb')
for i in range(10):
	pickle.dump(Car[i],CarFile)
CarFile.close()

CarFile = open('Cars.DAT','rb')
Car = []
Eof = False
while not Eof:
	try: 
		Car.append(pickle.load(CarFile))
	except:
		Eof = True
CarFile.close()

for i in range(10):
	print(Car[i].VehicleID,Car[i].Registration,
		Car[i].DateOfRegistration,Car[i].EngineSize,Car[i].PurchasePrice)
