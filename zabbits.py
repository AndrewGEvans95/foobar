def answer(population,y,x,strength):

	#list comprehension
	#creates list of (x,y) cords of all rabbits with resistance <= strength
	risk_population = [(x_cord,y_cord) for x_cord,j in enumerate(population) for y_cord,i in enumerate(j) if population[x_cord][y_cord]<=strength]
	
	if (x,y) not in risk_population: return population
	zombie = [(x,y)]
	
	#function that generates a list of possible rabbit movements, given a list of cords of rabbits infected
	simulate = lambda p: [(i[0]+[1,-1,0,0][h],i[1]+[1,-1,0,0][::-1][h]) for h in range(4) for i in p]
	
	#loop through to create list of shared locations between infected rabbits and vulnerable rabbits
	for x in risk_population:
		infect = list(set(simulate(zombie)))
		zombie.extend(set(infect)-(set(infect)-set(risk_population)))
	
	#change infected rabbits to -1 in population array using 2d pos
	for xcord,ycord in list(set(zombie)):
		population[xcord][ycord] = -1
	return population

population = [[1, 2, 7], [1, 2, 7]]
print answer(population, 2, 1, 5)