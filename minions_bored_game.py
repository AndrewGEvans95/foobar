import itertools
import math

def answer(t,n):
	numOfPossibilities = 0
	dieRolls = []
	tmpSum = 0
	for x, i in enumerate(itertools.product([-1,0,1], repeat=t)):
		for z, y in enumerate(i):
			if(tmpSum == n-1 and y!=0):
				tmpSum = -10000000000000
				break
			tmpSum = tmpSum + y
			if(tmpSum < 0 or tmpSum > n-1):
				tmpSum = -10000000000000
				break
		if(tmpSum == n-1):
			#print "This will work: %s, sum: %s" %(list(i), sum(i))
			numOfPossibilities = numOfPossibilities + 1
			dieRolls.append(list(i))
		tmpSum = 0
	return numOfPossibilities
print answer(8,3)

#3
#6/2

#4
#12/3

#5
#20/4

#6
#30/5

print math.factorial(8)/math.factorial(8-3)/(8-3)

n = 10
p = 3

print (math.factorial(n + (p - 1)) / math.factorial(n) / math.factorial(p - 1))-1

