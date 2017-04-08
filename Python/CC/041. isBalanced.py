"""
Implement a function to check if a binary tree is balanced
O(n) implementation
"""

import Trees as t

def isBalanced(n):
	
	if is_height_balanced(n) < 0:
		return False
	else:
		return True
		
def is_height_balanced(n):
	
	if n == None:
		return 0
		
	left_h = is_height_balanced(n.left)
	
	# left is not height balanced, return
	if left_h == -1:
		return left_h
		
	right_h = is_height_balanced(n.right)
	
	# right is not height balanced, return
	if right_h == -1:
		return right_h
		
	if abs (left_h - right_h) > 1:
		return -1
	
	return 1 + max(left_h, right_h)
		
"""
Caveats:
	- Modified post order traversal
	- Two functions needed since one function returns boolean and the other integer
	- https://www.youtube.com/watch?v=TWDigbwxuB4
"""

bst = t.Trees()
lst = [2, 5, 7, 27, 14, 8, 13, 35, 12, 59, 32, 37, 78, 70, 84, 17, 9, 26, 1, 98]

for i in lst:
    bst.root = bst.insert(i, bst.root)
	
bst.print_graph()

print isBalanced(bst.root)	# false


bst2 = t.Trees()
lst2 = [5, 2, 7]

for i in lst2:
    bst2.root = bst2.insert(i, bst2.root)
	
bst2.print_graph()

print isBalanced(bst2.root)	# true

