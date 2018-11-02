#Recursion-2
#S3Opt3 Stefan Yuzhao Heng

def groupSum(start,nums,target):
	if start+1 > len(nums):
		return target == 0

	return groupSum(start+1,nums,target) or groupSum(start+1,nums,target-nums[start])

def groupSum6(start,nums,target):
	if start+1 > len(nums):
		return target == 0

	if nums[start] == 6:
		return groupSum6(start+1,nums,target-6)
	return groupSum6(start+1,nums,target) or groupSum6(start+1,nums,target-nums[start])

def groupNoAdj(start,nums,target):
	if start+1 > len(nums):
		return target == 0

	return groupNoAdj(start+1,nums,target) or groupNoAdj(start+2,nums,target-nums[start])

def groupSum5(start,nums,target):
	if start+1 > len(nums):
		return target == 0 

	if nums[start]%5 == 0 and nums[start+1] == 1:
		return groupSum5(start+2,nums,target-nums[start])
	elif nums[start]%5 == 0:
		return groupSum5(start+1,nums,target-nums[start])
	return groupSum5(start+1,nums,target) or groupSum5(start+1,nums,target-nums[start])

def groupSumClump(start,nums,target):
	if start+1 > len(nums):
		return target == 0 

	if start < len(nums)-1: 
		if nums[start] == nums[start+1]:
			i = start
			while i < len(nums)-1 and nums[i] == nums[i+1]:
				i += 1
			i += 1
			return groupSumClump(i,nums,target) or groupSumClump(i,nums,target-(i-start)*nums[i-start])
	return groupSumClump(start+1,nums,target) or groupSumClump(start+1,nums,target-nums[start])

def splitArray(nums,start=0,l=0,r=0):
	if start == len(nums):
		return l == r

	return splitArray(nums,start+1,l+nums[start],r) or splitArray(nums,start+1,l,r+nums[start])

def splitOdd10(nums,start=0,l=0,r=0):
	if start == len(nums):
		return (l%10 == 0 and r%2 == 1) or (l%2 == 1 or r%10 == 0)
	
	return splitOdd10(nums,start+1,l+nums[start],r) or splitOdd10(nums,start+1,l,r+nums[start])

def split53(nums,start=0,l=0,r=0):
	if start == len(nums):
		return l == r

	if nums[start]%3 == 0:
		return split53(nums,start+1,l+3,r)
	if nums[start]%5 == 0:
		return split53(nums,start+1,l,r+5)
	return split53(nums,start+1,l+nums[start],r) or split53(nums,start+1,l,r+nums[start])

#print(11%5==0)
print(groupSum(0,[2,4,8],12))
print(groupSum6(0,[5,6,2],7))
print(groupNoAdj(0,[2,5,10,4],14))
print(groupSum5(0,[2,5,10,1],16))
print(groupSumClump(0,[2,4,4,4,3,4],15))
print(splitArray([2,3,5]))
print(splitOdd10([5,5,6,1]))
print(split53([3,5,6,10,5,5,3,3]))