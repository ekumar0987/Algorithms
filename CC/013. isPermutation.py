"""
Given 2 strings, write a method to decide if one is a permutation of the other
"""

# Approach 1: No extra data structure used
def isPermutation1 (s1, s2):
	
	# check the lengths and check to see if the sorted strings match
	if(len(s1) != len(s2)) or (sorted(s1) != sorted(s2)):
		return False
	else:
		return True

# True case		
string1 = "abc"
string2 = "bac"
print isPermutation1(string1, string2)
	
# False case
string1 = "abc"
string2 = ""
print isPermutation1(string1, string2)



# Approach 1: Use a hashmap. Iterate over first string and increment counts. Iterate over
# second string and decrement counts. If the strings are permutations, the counts in the endswith
# will all be zeroes
def isPermutation2 (s1, s2):
	
	if len(s1) != len(s2):
		return False
		
	dict_counts = {}
	
	# loop over first string and increase counts
	for s in s1:
		if s in dict_counts:
			dict_counts[s] = dict_counts[s] + 1
		else:
			dict_counts[s] = 1
			
	for s in s2:
		if s in dict_counts:
			dict_counts[s] = dict_counts[s] - 1
			
			# extra character in s2, return false
			if dict_counts[s] < 0:
				return False
			
		# new character in s2 not seen in s1, return false
		else:
			return False
			
	# check final counts
	for value in dict_counts.values():
		if value != 0:
			return False
			
	# counts were all 0s after the last loop, return True
	
	return True
	

			
# True case		
string1 = "abc"
string2 = "bac"
print isPermutation2(string1, string2)
	
# False case
string1 = "abc"
string2 = ""
print isPermutation2(string1, string2)

"""
Caveats:

- There is no built in function called sort. Use sorted. Line 8.
- Extra optimizations on lines 47 - 49
- Avoid loop Line 56 - 58
    
	if not 0 in dict_counts.values():
		return False

"""