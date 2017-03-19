"""
Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures
"""

#Without additional data structures
def isUnique1(str):
	return len(str) == len(set(str))


def isUnique2(str):
	for i in xrange(0, len(str)-1):
		for j in xrange(i+1, len(str)):
			if str[i] == str[j]:
				return False
	return True
	

print 'Approach 1 - aaaab: ', isUnique1('aaaab')
print 'Approach 1 - ab: ', isUnique1('ab')


print 'Approach 2 - aaaab: ', isUnique2('aaaab')
print 'Approach 2 - ab: ', isUnique2('ab')

#With additional data structures
def isUnique3(str):
	dict = {}
	for s in str:
		if s in dict:
			return False
		else:
			dict[s] = True
	
	return True
	
print 'Approach 3 - aaaab: ', isUnique3('aaaab')
print 'Approach 3 - ab: ', isUnique3('ab')

#Corner cases - Empty strings are unique
print isUnique3('')
