"""
Write a function to find the longest common prefix string amongst an array of strings.

['Flower', 'Flow', 'Fleet', 'Fling'] would return 'Fl'

"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        #Find the shortest string in the list. The longest common prefix cannot be longer than this
		#Corner case: Length check
        if len(strs) != 0:
            shortest_string = min(strs, key = len)
        else:
            return ''
        
        longest_prefix_length = len(shortest_string)
        longest_common_prefix = ''
        
        #Loop through the list and compare each element with the shortest string
        for s in strs:
            prefix_length = 0
            common_prefix = ''
            
            j = 0
            
            while j < len(shortest_string):
                if shortest_string[j] != s[j]:
                    break
                else:
                    common_prefix += s[j]
                    j += 1
                    prefix_length += 1
            
			#If the current prefix, is shorter than the previous longest prefix, overwrite (In this example 'Fl' instead of the initial 'Flow')
            if prefix_length <= longest_prefix_length:
                longest_prefix_length = prefix_length
                longest_common_prefix = common_prefix
                
        return longest_common_prefix
		
"""
Notes:
L18 - Finding the shortest word in the list using min()
"""