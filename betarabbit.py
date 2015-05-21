def convertToBase(n, i):
    digits = []
    while n:
        digits.append(int(n % i))
        n /= i
    return digits[::-1]


def answer(numin):

	counter = 3
	#first do a simple base 2
	if(bin(int(numin))[2:] == bin(int(numin))[2:][::-1]):
		return 2
	while(counter<1000):
		base =  ''.join(str(x) for x in convertToBase(numin, counter))
		if(base==base[::-1]):
			return counter
		counter = counter + 1
	return -1

#POC
print answer(0)
print answer(42)