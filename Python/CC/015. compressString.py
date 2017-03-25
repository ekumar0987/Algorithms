"""
Implement a method to perform string compression. If the compressed string is not smaller than
the original string return the original string
"""

# returns the length of the compressed string
def compressedListLength(charList):
	
	# total length
	strLength = 0
	
	# starts at 1 so as to not undercount
	charCount = 1
	
	for i in range(len(charList)):
		
		# special case for END OF STRING. Without this charList[i + 1] will fail
		if (i == len(charList) - 1) or (charList[i] != charList[i + 1]):
			strLength = strLength + len(str(charCount)) + 1               # 1 for the actual character
			charCount = 1
		# current character is the same as the next character, increment count
		else:
			charCount = charCount + 1
	
	return strLength
			

# compresses string		
def compressString(charList):
	
	compressedList = []			    # use list because it is mutable
	charCount = 1					# start at one, so as to not undercount
	
	# compress not needed
	if (len(charList) < (compressedListLength(charList))):    
		return "".join(charList)
	
	# compress needed
	else:
		for i in range(len(charList)):
			
			# special case for END OF STRING. Without this charList[i + 1] will fail in the next step
			if (i == len(charList) - 1) or (charList[i] != charList[i + 1]):
				compressedList.append(charList[i])
				compressedList.append(str(charCount))	       # append count as string, else "".join fails
				charCount = 1		# reset			
			else:
				charCount = charCount + 1
		
		return "".join(compressedList)
				
# testing
s = "aaaaaaaaaaabbccd"
compressedString = compressString(list(s))
print compressedString

s = "abcd"
compressedString = compressString(list(s))
print compressedString

"""
Caveats:
- This cannot be done in place. Example: In abcccccccc, in the first iteration a1 will overwrite ab 
- There is special logic when you reach end of the string
- You cannot find the length of an integer directly like this len(charCount). You must convert it to a 
  string first len(str(charCount))
- You need a method to get the compressed string length
- Compare current character (i) with next (i + 1). If there is a match, increment counts else append to list
"""