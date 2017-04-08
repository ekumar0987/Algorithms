"""
Algorithm to print all paths which sum at a given value. The algorithm need not start at the root or end at the leaf
"""
import Trees as t

def print_all_paths(n, sum, path, level):

	if n == None:
		return
	
	# add current node to list
	path.insert(level, n.key)
	
	# CRUX
	# iterate backwards from node n up till 0 and check if you see the sum along the path
	runningSum = 0
	for i in xrange(level, -1, -1):
		runningSum = runningSum + path[i]
		if runningSum == sum:
			print_path(path, level, i-1)
			
	print_all_paths(n.left, sum, path, level + 1)
	print_all_paths(n.right, sum, path, level + 1)
	

def print_path(path, start, end):

	for i in xrange(start, end, -1):
		print path[i]
		
	print "\n"
	
"""
Caveats:
	- You have to go backwards level by level up till the root (bottom up basically). We can do a running sum from root to leaf (or top down) because
	  if root to leaf had multiple paths that add up to a sum, you'll only get the first one
		EXAMPLE: 5 - 3 - 1 - (-1) and sum 8 will give path 5 - 3 only and not 5 - 3 - 1 - (-1) because the loop won't go beyond 3 since it found sum 8 at 3
"""

# testing
bst = t.Trees()
lst = [2, 5, 7, 1, -1]

for i in lst:
    bst.root = bst.insert(i, bst.root)

bst.print_graph()

root = bst.root

print_all_paths(root, 2, [], 0)