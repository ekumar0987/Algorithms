"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the 
input string is valid.

The brackets must close in the correct order, "()", "()[]{}", "({})" are all valid 
but "(]", "([)]", "{" and ")]" are not.

"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        
        #Cannot directly return true for '['
        return stack == []

"""
Notes: Stacks and Queues in Python can be implemented using lists
https://docs.python.org/2/tutorial/datastructures.html
"""