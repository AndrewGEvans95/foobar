def answer(intervals):
	#I am a conjurer of cheap tricks
	#Quick and cheap way to flatten a "2d" list
	#But hey, it's only a total of 2 funtion calls for the whole function
	#(Not too shabby)
	intervals = sum(intervals, [])
	intervals.sort()
	return intervals[len(intervals)-1]-intervals[0]