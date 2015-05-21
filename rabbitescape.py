def answer(x):
	if (sum(x) % len(x) == 0):
		return len(x)
	else:
		return len(x)-1

print answer([2,1])