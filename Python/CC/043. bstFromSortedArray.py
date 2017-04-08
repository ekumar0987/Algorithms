"""
Given a sorted array with unique integer elements write an algorithm to create a binary search tree with minimal height (or balanced BST)
"""

import Trees as t

def create_bst_from_sorted_array(arr, low, high):
	
	if (low > high):
		return None
	
	mid = (low + high) / 2
	
	# create root
	n = t.Node(arr[mid])
	
	# build left subtree from left half of the array
	n.left = create_bst_from_sorted_array(arr, low, mid - 1)
	
	# build right subtree from right half of the array
	n.right = create_bst_from_sorted_array(arr, mid + 1, high)
	
	return n
	
"""
Caveats:
	- http://www.ideserve.co.in/learn/create-a-balanced-bst-from-a-sorted-array
	- Binary Search involved
"""

bst = t.Trees()
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

bst.root = create_bst_from_sorted_array(lst, 0, len(lst) - 1)
	
bst.print_graph()	
	