def answer(x, y, z):
	#We want to make a list out of the above three integers.
	#It's much easier to work with arrays rather than sperate variables
	indata = []
	indata.append(x)
	indata.append(y)
	indata.append(z)
	indata.sort()

	#Since we are told that there will never been an incorrect
	#we don't have to check to see if no date is valid.
	#However we must check to make sure the highest value in the array
	#couldn't be the day of the month
	#The masterDays list contains the number of days in each month Jan-Dec (0-11)
	#where 0 is Jan
	masterDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	if(indata[2]<=masterDays[indata[0]-1] and indata[2]!=indata[1]):
		return "Ambiguous"

	if(indata[0]==indata[1] and indata[1] == indata[2] or indata[0]==indata[1]):
		return "%02d/%02d/%02d" %(indata[0], indata[1], indata[2])
		
	#We simply assume that at least one is valid and now 
	#we only need to check to see if there could be some ambiguouty.
	if(indata[1]<=12 and indata[0]<=12):
		return "Ambiguous"

	else:
		return "%02d/%02d/%02d" %(indata[0], indata[1], indata[2])

print answer(19, 19, 3)