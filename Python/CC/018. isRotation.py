"""
Assume you have a method isSubstring which checks if one word is a substring of another. Given 2 
strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to substring
"""

s1 = "erbottlewat"
s2 = "waterbottle"

if s2 in s1 + s1:
	print "yes"
