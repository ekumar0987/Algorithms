"""
Write a method to replace all spaces in a string with %20. You may assume that the string has sufficient space in the endswith
to hold all the characters, and that you're given the true length of the string
"""

def replaceSpaces(charList, length):
	
	# important to compute space count, because we do not know if the string has extra space exactly as needed or more
	spaceCount = 0
	
	# no need to check for length being <= 0 prior to this step because this loop will not evaluate and spacecount will be 0
	# later in the code, checks exist for spacecount being 0
	for i in range(length):
		if charList[i] == ' ':
			spaceCount = spaceCount + 1
			
	# assign 2 pointers - one the true length minus 1, other length with extra space minus 1
	i = length - 1
	j = length + (spaceCount * 2) - 1
	
	# loop until you've not reached the begining of the string or there aren't any more spaces left 
	#(*** space check: extra optimization of the loop***)
	while(i >= 0 and spaceCount):
		if(charList[i] == ' '):
			spaceCount = spaceCount - 1
			charList[j] = '0'
			charList[j - 1] = '2'
			charList[j - 2] = '%'
			j = j - 3
			i = i - 1
		
		else:
			charList[j] = charList[i]
			j = j - 1
			i = i - 1
			
	return "".join(charList)
	

	
# Testing
str = "Mr John Smith                     "
result = replaceSpaces(list(str), 13)
print result


"""
Caveats:
- you need a space count variable because you don't exact know how much extra space the string has
- space count optimization: you can end the loop once there are no more spaces
- you use 2 pointers and start from the END!
"""