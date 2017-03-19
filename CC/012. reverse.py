"""
Implement a function to reverse a null terminated string
"""

def reverseString(str):
	
	l = []
	
	#convert string to a list because strings are immutable
	l = list(str)
		
	for (i,j) in zip(xrange(0, len(l)), xrange(len(l) - 1, -1, -1)):	#zip, 3 optional argument to go backwards
		if(i >= j):
			#convert result back to string and return
			return "".join(l)
			
		tmp = l[i]
		l[i] = l[j]
		l[j] = tmp
	
print reverseString('apple')
print reverseString('')