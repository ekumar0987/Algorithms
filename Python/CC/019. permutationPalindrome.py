"""
Given a string write a function to check if it is a permutation of a palindrome
"""

def is_permutation_of_palindrome(str):

	hash_map_char_count = {}
	number_of_chars_with_odd_count = 0
	
	for ch in str:
		
		# add counts to hash map
		if ch not in hash_map_char_count:
			hash_map_char_count[ch] = 1
		else:
			hash_map_char_count[ch] = hash_map_char_count[ch] + 1
		
		# if the current count for ch is odd, increment the odd count variable else decrement it
		if hash_map_char_count[ch] % 2 != 0:
			number_of_chars_with_odd_count = number_of_chars_with_odd_count + 1
		else:
			number_of_chars_with_odd_count = number_of_chars_with_odd_count - 1
			
	
	return number_of_chars_with_odd_count <= 1
	
	
"""
Caveats:
	- All you need is to know how many characters in this entire string have an odd count. For a palindrome, this number_of_chars_with_odd_count
	can atmost be 1
"""