from fractions import gcd
def answer(vertices):
	#Frist get the area of the triangle
	area = .5*abs((vertices[0][0]-vertices[2][0])*(vertices[1][1]-vertices[0][1])-(vertices[0][0]-vertices[1][0])*(vertices[2][1]-vertices[0][1]))
	#Second get the number of integer points on the boundaries
	b = gcd(abs(vertices[0][0]-vertices[1][0]), abs(vertices[0][1]-vertices[1][1]))+gcd(abs(vertices[1][0]-vertices[2][0]), abs(vertices[1][1]-vertices[2][1]))+gcd(abs(vertices[2][0]-vertices[0][0]), abs(vertices[2][1]-vertices[0][1]))
	#Third apply Pick's Theorem
	i = area - b/2 + 1
	
	return int(i)

answer([[91207,89566],[-88690,-83026],[67100,47194]])