def answer(x):
	newList = set()
	for y in x:
		if y[::-1] not in newList:
			newList.add(y)
	return len(newList)


print answer(["foo", "bar", "oof", "bar", "yy", "yy", "dd", "yy"])