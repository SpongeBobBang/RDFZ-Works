def go(x):
	if x <= 10:
		print(x)
		go(x+2)

go(2)