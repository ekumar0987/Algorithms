"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

The input is assumed to be a 32-bit signed integer. 
Your function should return 0 when the reversed integer overflows

"""

class Solution(object):
    
	#Result
    result = ''
    
	#Flag to indicate if the number is positive or negative
	neg = 0
    
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
		#this block runs only once if the number is negative
        if(x < 0 and self.neg == 0):
            
			#self needed to access any class variable
			self.neg = 1
            self.result = '-'
            x = abs(x)
            
        if(x >= 10):
            self.result += str(x % 10)
            x = x / 10
			
			#recursive call. notice the use of self
            return self.reverse(x)
            
        else:
			#convert rhs to a string because you cannot concatenate strings and integers
            self.result += str(x % 10)
            if ( int(self.result) > (2 ** 31) or int(self.result) < ((2 ** 31) * -1)):
                return 0
            else:
                return int(self.result)
				
				
"""
Notes:

- Signed integers range from  - 2 ^ 31 to 2 ^ 31. The last one bit is used for the sign 
- Unsigned integers range from  - 2 ^ 32 to 2 ^ 32

- Accessing class members and functions requires the use of self
"""