"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

"""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        rows = []
        for i in range(numRows):
            rows.append([])
            
        currentrow = 0 
        reverse = 0
        nextindex = 0
        result = ""
        
        #Corner case
        if numRows == 1:
            return s
        
        #Iterate through the string
        for letter in s:
            
            #Traverse reverse?
            if reverse == 1:
                rows[nextindex].append(letter)
                nextindex = nextindex - 1
                
                if nextindex < 0:
                    reverse = 0
                    currentrow = 1
            
            else:
                rows[currentrow].append(letter)
                currentrow = currentrow + 1
            
                if currentrow == numRows:
                    reverse = 1
                    nextindex = numRows - 2
        
        #Concatenate all the letters        
        #i is also a list
        for i in rows:
            #j is characters in list i
            for j in i:
                result += j

        return result