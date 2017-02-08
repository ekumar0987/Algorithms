"""
Given a roman numeral, convert it to an integer.
Input is guaranteed to be within the range from 1 to 3999.

Algorithm to convert Roman Numerals to Integer Number :

Split the Roman Numeral string into Roman Symbols (character).
Convert each symbol of Roman Numerals into the value it represents.
Take symbol one by one from starting from index 0:
If current value of symbol is greater than or equal to the value of next symbol, then add this value to the running total.
else subtract this value by adding the value of next symbol to the running total.

Roman numerals are based on below symbols.
'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000

"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        roman_symbol_value = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        roman_str = str(s)
        runningSum = 0
        
        #for i in range(len(roman_str)) #Cannot use the for loop because increment i does not help. It will still go through the entire range
        
        i = 0
        while i < len(roman_str):
            
            #print runningSum
            #print i
            
            #Add the last value
            if(i == (len(roman_str) - 1)):
				runningSum += roman_symbol_value[roman_str[i]]
				break
            
            elif roman_symbol_value[roman_str[i]] >= roman_symbol_value[roman_str[i+1]]:
                runningSum += roman_symbol_value[roman_str[i]]
                i += 1
            
            else:
                runningSum += roman_symbol_value[roman_str[i+1]] - roman_symbol_value[roman_str[i]]
                i += 2
                
        return runningSum
		
"""
Notes:
1. For loop did not work because incrementing i inside for loop did nothing to the loop iteration.
2. Creating and accessing dictionary values
"""