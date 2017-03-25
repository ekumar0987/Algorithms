"""
Write an algorithm such that if an element in an MxN matrix is 0, the entire row and columns are set to zero
"""

def fillZeroes(matrix, m , n):
	
	# lists to hold which rows and columns must be set to 0
	rows = []
	cols = []
	
	# loop over all rows and columns
	# for (i, j) in zip(xrange(m), xrange(n)):       # cannot use, this gives diagonal
	for i in xrange(m):
		for j in xrange(n):
			if matrix[i][j] == 0:
				rows.append(i)
				cols.append(j)
			
	# loop over rows that must be set to 0
	for i in rows:
		# all cols
		for j in xrange(n):
			matrix[i][j] = 0
			
	# loop over columns that must be set to 0
	for j in cols:
		# all rows
		for i in xrange(m):
			matrix[i][j] = 0
			
	return matrix
	
# testing
m = [
     [1, 2, 0, 3],
     [4, 5, 6, 4],
	 [7, 8, 9, 7]
	]
	
filled_with_zeroes = fillZeroes(m, 3, 4)

print filled_with_zeroes


"""
Caveats:
- need to create a list to hold the row and column indices that must be set to zero
"""


	