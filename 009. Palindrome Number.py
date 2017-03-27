"""
Determine whether an integer is a palindrome. Do this without extra space.
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        result = str(x)
		
		#create pointers to the start and end of the string
        i = 0
        j = len(result) - 1
        
		#as long as i is less than j, run the loop to compare
        while (i < j):
            print 'i=' + str(i) +',j='+ str(j)
            if(result[i] != result[j]):
                return False
            else:
                #i++    #cannot do this because integers are immutable in Python 
                i += 1
                j -= 1
                
        return True
		
"""
Notes:
i++ is not valid in Python
Notice keywords True and False to return booleans
"""