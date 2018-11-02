import threading
import time 
import random

n = 30

def doWork(name):
	global n
	print(name,"marking exam",n)
	n -= 1
	time.sleep(random.randint(1,4))

class MyThread(threading.Thread):
	def __init__(self,name,count):
		threading.Thread.__init__(self)
		self.name = name
		self.count = count

	def run(self):
		print("Starting thread",self.name)
		while(self.count > 0):
			doWork(self.name)
			self.count -= 1
		print("Exiting thread",self.name)

daniel = MyThread("Daniel",10)
lulu = MyThread("Lulu",20)

daniel.start()
lulu.start()