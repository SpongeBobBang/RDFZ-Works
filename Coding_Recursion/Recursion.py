#Recursion-1
#S3Opt3 Stefan Yuzhao Heng

def factorial(x):
	if x == 1:
		return 1

	return x*factorial(x-1)

def bunnyEars(bunnies):
	if bunnies == 0:
		return 0

	return bunnyEars(bunnies-1)+2

def fibonacci(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1

	return fibonacci(n-1)+fibonacci(n-2)

def bunnyEars2(bunnies):
	if bunnies == 0:
		return 0

	if bunnies % 2 == 1:
		return bunnyEars2(bunnies-1)+2
	else:
		return bunnyEars2(bunnies-1)+3

def triangle(rows):
	if rows == 0:
		return 0
	elif rows == 1:
		return 1

	return rows+triangle(rows-1)

def sumDigits(n):
	if n == 0:
		return 0

	return n%10+sumDigits(n//10)

def count7(n):
	if n == 0:
		return 0

	if n%10 == 7:
		return 1+count7(int(n/10))
	else:
		return count7(int(n/10))

def count8(n):
	if n == 0:
		return 0

	if n%10 == 8:
		if (n//10)%10 == 8:
			return 2+count8(n//10)
		else:
			return 1+count8(n//10)

	return count8(n//10)

def powerN(base,n):
	if n == 0:
		return 1
	else:
		return base*powerN(base,n-1)

def countX(string):
	if len(string) == 0:
		return 0

	if string[len(string)-1] == "x":
		return 1+countX(string[:-1])
	return countX(string[:-1])

def countHi(string):
	if len(string) == 1:
		return 0

	if string[len(string)-3:len(string)-1] == "hi":
		return 1+countHi(string[:-1])
	return countHi(string[:-1])

def changeXY(string):
	if len(string) == 0:
		return ""

	if string[0] == "x":
		return "y"+changeXY(string[1:])
	return string[0]+changeXY(string[1:])

def changePi(string):
	if len(string) == 1:
		return string

	if string[0:2] == "pi":
		return "3.14"+changePi(string[2:])
	return string[0]+changePi(string[1:])

def noX(string):
	if len(string) == 0:
		return ""

	if string[0] == "x":
		return noX(string[1:])
	return string[0]+noX(string[1:])

def array6(nums,index):
	if nums[index] == 6:
		return True
	elif index+1  == len(nums):
		return False

	return array6(nums,index+1)

def array11(nums,index):
	if index+1 == len(nums):
		return 0

	if nums[index] == 11:
		return 1+array11(nums,index+1)
	return array11(nums,index+1)

def array220(nums,index):
	if index+1 == len(nums):
		return False

	if nums[index]*10 == nums[index+1]:
		return True
	return array220(nums,index+1)

def allStar(string):
	if len(string) == 1:
		return string 

	return string[0]+"*"+allStar(string[1:])

def pairStar(string):
	if len(string) == 1:
		return string

	if string[0] == string[1]:
		return string[0]+"*"+pairStar(string[1:])
	return string[0]+pairStar(string[1:])

def endX(string):
	if len(string) == 0:
		return ""

	if string[0] == "x":
		return endX(string[1:])+"x"
	return string[0]+endX(string[1:])

def countPairs(string):
	if len(string) == 2:
		return 0 

	if string[0] == string[2]:
		return 1+countPairs(string[1:])
	return countPairs(string[1:])

def countAbc(string):
	if len(string) == 2:
		return 0

	if string[0:3] == "abc" or string[0:3] == "aba":
		return 1+countAbc(string[1:])
	return countAbc(string[1:])

def count11(string):
	if len(string) <= 1:
		return 0

	if string[0:2] == "11":
		return 1+count11(string[2:])
	return count11(string[1:])

def stringClean(string):
	if len(string) == 1:
		return string

	if string[0] == string[1]:
		return stringClean(string[1:])
	return string[0]+stringClean(string[1:])

def countHi2(string):
	if len(string) == 1:
		return 0

	if string[0] == "x":
		return countHi2(string[2:])

	if string[0:2] == "hi":
		return 1+countHi2(string[1:])
	return countHi2(string[1:])

def parenBit(string):
	if len(string) == 0:
		return ""

	if string[0] == "(" and string[-1] == ")":
		return string
	if string[0] == "(":
		return parenBit(string[:-1])
	if string[-1] == ")":
		return parentBit(string[1:])
	return parenBit(string[1:-1])

def nestParen(string):
	if len(string) <= 3 and string[0] == "(" and string[-1] == ")":
		return True
	elif len(string) <= 3:
		return False

	if string[0] == "(" and string[-1] == ")":
		return nestParen(string[1:-1])
	return False

def strCount(string,sub):
	if len(sub) > len(string):
		return 0

	if sub == string[:len(sub)]:
		return 1+strCount(string[len(sub):],sub)
	return strCount(string[1:],sub)

def strCopies(string,sub,n):
	if len(sub) > len(string) and n != 0:
		return False
	elif len(sub) > len(string) and n == 0:
		return True

	if sub == string[:len(sub)]:
		return strCopies(string[1:],sub,n-1)
	return strCopies(string[1:],sub,n)

def strDist(string,sub):
	if len(sub) > len(string):
		return 0

	if sub == string[-len(sub):] and sub == string[:len(sub)]:
		return len(string)
	elif sub == string[:len(sub)]:
		return strDist(string[:-1],sub)
	elif sub == string[-len(sub):]:
		return strDist(string[1:],sub)
	return strDist(string[1:-1],sub)

#print("sekmd"[:5])
print(factorial(4))
print(bunnyEars(4))
print(fibonacci(7))
print(bunnyEars2(4))
print(triangle(4))
print(sumDigits(1234))
print(count7(377))
print(count8(88818))
print(powerN(3,4))
print(countX("xxhixx"))
print(countHi("xhixhix"))
print(changeXY("xxhixx"))
print(changePi("xpixe"))
print(noX("abcxx"))
print(array6([1,6,4],0))
print(array11([1,2,11,11,3],0))
print(array220([3,2,20,1],0))
print(allStar("abc"))
print(pairStar("xxyy"))
print(endX("xxre"))
print(countPairs("axbx"))
print(countAbc("ababc"))
print(count11("11111"))
print(stringClean("aaaabbbbcccc"))
print(countHi2("hixhixhi"))
print(parenBit("xyz(abc)123"))
print(nestParen("((x)))"))
print(strCount("catcowcat","cat"))
print(strCopies("catcowcat","cat",1))
print(strDist("cccatcowcatxx","cat"))
print(parenBit("123)123(456"))
print("3456")