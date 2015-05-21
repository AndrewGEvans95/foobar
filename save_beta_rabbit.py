zombfood = {}
def myRecursion(food, grid, x, y):
	#Save some processing by creating variables
	xlen = (len(grid)-1)
	ylen = (len(grid)-1)
	if food < 0:
		return "1056 nix nix!"
	if x == xlen and y == ylen:
		return food
	elif x == xlen:
		return myRecursion(food-grid[x][y+1], grid, x, y+1)
	elif zombfood.get(str(x)+" "+str(y)+" "+str(food)) != None:
		return zombfood.get(str(x)+" "+str(y)+" "+str(food))
	elif y == ylen:
		return myRecursion(food-grid[x+1][y], grid, x+1, y)
	else:
		lowestfood = min(myRecursion(food-grid[x+1][y], grid, x+1, y), myRecursion(food-grid[x][y+1], grid, x, y+1))
		zombfood[str(x)+" "+str(y)+" "+str(food)] = lowestfood;
		return lowestfood

def answer(food, grid):
	#We need to use recursion in order to prevent using
	#an obscene amount of for loops and scanning
	#We start at 0,0

	myanswer = myRecursion(food, grid, 0, 0)
	if(myanswer == "1056 nix nix!"):
		return -1
	return myanswer

print answer(7, [[0, 2, 5], [1, 1, 3], [2, 1, 1]])
