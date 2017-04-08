"""
Algorithm to find the first common ancestor of 2 nodes in a binary tree
"""

import Trees as t

# helper function to find key in a tree with root n
def find(n, key):

	if n == None:
		return False
	elif n.key == key:
		return True
	else:
		return find(n.left, key) or find(n.right, key)

def commonAncestor(root, n1, n2):
	
	if root == None:
		return
		
	# if one of the nodes is parent to the other. CORNER CASE
	if root.key == n1.key or root.key == n2.key:
		return root
		
	# check if these nodes are in the left subtree of root
	is_n1_in_left_tree = find(root.left, n1.key)
	is_n2_in_left_tree = find(root.left, n2.key)
	
	# if one node is in left subtree and other is in the right subtree, we found the ancestor
	if is_n1_in_left_tree != is_n2_in_left_tree:
		return root
		
	# depending on which side both the nodes were found, go to that side. NEED TO ONLY GO ONE SIDE
	if is_n1_in_left_tree and is_n2_in_left_tree:
		return commonAncestor(root.left, n1, n2)
	else:
		return commonAncestor(root.right, n1, n2)
		
"""
Caveats:
	- Common ancestor is the one where one of the nodes is in the left subtree and other in the right
	- Corner case: One of the nodes is parent to the other, parent node is itself the common ancestor
	- Traverse towards the side that has both nodes
Mistakes:
	- Missed corner case #25
	- Used root instead of root.left on #29 and #30
	- Missed the traversing only one side of the tree (in this case looking for both on left) would suffice
"""

# testing
bst = t.Trees()
lst = [2, 5, 7, 27, 14, 8, 13, 35, 12, 59, 32, 37, 78, 70, 84, 17, 9, 26, 1, 98]

for i in lst:
    bst.root = bst.insert(i, bst.root)

bst.print_graph()

root = bst.root

# first check both nodes exist
if (find(root, 8) and find(root, 59)):
	print "Both nodes exist, finding common ancestor..."
else:
	print "Nodes do not exist"

n1 = t.Node(8)
n2 = t.Node(59)

ancestor = commonAncestor(root, n1, n2)

if ancestor:
	print ancestor.key


	

