"""
Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method
to rotate the image by 90 degrees. Can you do this in place.
"""

# swap elements other than the diagnoal
def transposeMatrix(m):
	# loop over row indices
	for row in range(len(m)):
		# loop over column indices for each row
		for col in range(len(m)):
			if row < col:
				tmp = m[row][col]
				m[row][col] = m[col][row]
				m[col][row] = tmp
				
	return m
	
# swap columns - clockwise rotate
def swapColumns(t):
	# loop over rows
	for row in t:
		# swap first element with last, second with last but one and so on
		# i iterates forward, j iterates backward
		for (i, j) in zip(range(0, len(row), 1), range(len(row) - 1, -1, -1)):
			if i < j:
				tmp = row[i]
				row[i] = row[j]
				row[j] = tmp
				
	return t
	

# testing
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print matrix

transpose = transposeMatrix(matrix)
print transpose

clockwiseRotatedMatrix = swapColumns(transpose)
print clockwiseRotatedMatrix


"""
Caveats:
- In tranpose, you must loop over indices and not
	for row in m:
		for col in m[row]:
			~swap everything other than the diagonal
			
  because you're comparing list item (row) to an integer item (col) 	
  
- Line 14, use row < col and not row != col because in the later case NOTHING CHANGES. You swap it once
  and then swap it back.
  
- clockwise rotate: transpose and then swap columns
- anticlockwise rotate: swap columns first and then transpose
"""