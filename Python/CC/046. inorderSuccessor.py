"""
Write an algorithm to find the next node (i.e. in order successor) of a given node in a binary search tree

2 approaches:
- Iterative
- Every node has a link to its parent
"""

import Trees as t

def inorder_successor(n, key):

	succ = None
	curr = n
	
	# traverse through the tree until you find key
	while curr:
		
		if curr.key < key:
			curr = curr.right
		
		# crux
		elif curr.key > key:
			#MARK THE STARTING NODE OF LEFT SUBTREE
			succ = curr
			curr = curr.left
		
		# found the key
		else:
			
			# key has a right subtree, successor is the leftmost child of right subtree
			if curr.right:
				rightnode = curr.right
				tmp = rightnode.left
				while tmp:
					tmp = tmp.left
					
				return tmp
			
			# succersor is the node, that marked the begining of the left subtree where key was found
			else:
				return succ
	
	# did not find the key
	return succ  # i.e. None
	
"""
Caveats:
	- In order SUCCESSOR is either the leftmost child of the right subtree OR the latest node of the left subtree where the key resides!
"""

bst = t.Trees()
lst = [2, 5, 7, 27, 14, 8, 13, 35, 12, 59, 32, 37, 78, 70, 84, 17, 9, 26, 1, 98]

for i in lst:
    bst.root = bst.insert(i, bst.root)

bst.print_graph()

in_order_successor = inorder_successor(bst.root, 26)
if in_order_successor:
	print in_order_successor.key
