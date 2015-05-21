from math import log

def answer(x):
    options = []
    steps = int(log(x * 2, 3)) + 1
    for y in range(steps):
    	offset = (3 ** y - 1) / 2
    	leftover = int((x + offset)/3**y)
        options.append(['-', 'R', 'L'][leftover%3])
    return options

print answer(2)