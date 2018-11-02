#Task 26.02&03
#S3 CS3 Stefan Yuzhao Heng
class CarRecord:
	def __init__(self):
		self.VehicleID = 0
		self.Registration = None
		self.DateOfRegistration = None
		self.EngineSize = 0 
		self.PurchasePrice = 0.00

# def Hash(temp):
# 	return abs(hash(temp))

ThisCar = CarRecord()
ThisCar.VehicleID = 1123

import pickle

CarFile = open("Cars.DAT",'rb+')
Address = hash(ThisCar.VehicleID)
try:
	CarFile.seek(Address)
except:
	CarFile.seek(-Address)
pickle.dump(ThisCar, CarFile)

CarFile.close()

CarFile = open('Cars.DAT','rb')
Address = hash(ThisCar.VehicleID)
try:
	CarFile.seek(Address)
except:
	CarFile.seek(-Address)
ThisCar = pickle.load(CarFile)
CarFile.close()

print(ThisCar.VehicleID)