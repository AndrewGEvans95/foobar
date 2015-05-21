def decode(d, previous):
	z = 0
	while True:
		remainder = ((d ^ previous) + z * 256) % 129
		if(remainder == 0):
			return ((d ^ previous) + z * 256) / 129
		else:
			z = z + 1

def answer(digest):
	decoded = []
	for i, d in enumerate(digest):
		#Can't begin decoding without the first character!
		if(i==0):
			decoded.append(decode(d,0))
		else:
			decoded.append(decode(d,decoded[-1]))
	return decoded

print answer([0, 129, 5, 141, 25, 137, 61, 149, 113, 145, 53, 157, 233, 185, 109, 165])
