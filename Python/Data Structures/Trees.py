"""
Tree implementations using recursion
"""
import os

class Node:
	
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None
		
class Trees:
	
	def __init__(self):
		self.root = None
		
	def find(self, key, n):
		
		# not found
		if n == None:
			return 0
		# found
		if n.key == key:
			return 1
		# need to go left
		elif n.key > key:
			return find(key, n.left)
		# need to go right
		else:
			return find(key, n.right)
			
	def insert(self, key, n):
		
		# first time insertion
		if n == None:
			new_node = Node(key)
			return new_node
			
		if n.key == key:
			return
		# go left
		elif n.key > key:
			n.left = self.insert(key, n.left)
		else:
			n.right = self.insert(key, n.right)
		
		##### REM THIS###		
		return n
		
	# leftmost node of the tree
	def find_min(self, n):
	
		if n == None:
			return
		
		# base case
		if n.left == None:
			return n
		else:
			return self.find_min(n.left)
		
	# rightmost node of the tree
	def find_max(self, n):
		if n == None:
			return
		
		# base case
		if n.right == None:
			return n
		else:
			return self.find_max(n.right)
	
		# base case in else clause
	def delete(self, key, n):
	
		# nothing to delete
		if n == None:
			return
		
		# node to be deleted is on the right
		if n.key < key:
			n.right = self.delete(key, n.right)
		# node to be deleted is on the left
		elif n.key > key:
			n.left = self.delete(key, n.left)
		# found key to be deleted!!
		else:
			# leaf node
			if n.left == None and n.right == None:
				return None
			# has left child
			elif n.left != None and n.right == None:
				return n.left
			# has right child
			elif n.right != None and n.left == None:
				return n.right
			# has 2 children
			else:
				right_child = n.right
				successor = self.find_min(right_child)	# successor is the leftmost child of the right subtree
				n.key = successor.key					# overwrite n with successor
				n.right = self.delete(successor.key, n.right)	# like a separate recursion where we delete the successor node
		
		return n	# w/o this 2 --> 1
	
	# depth of the tree. If only the root node is present, depth is 1
	def depth(self, n):
		if n == None:
			return 0
		else:
			return 1 + max(self.depth(n.left), self.depth(n.right))
	
	# number of nodes in a tree
	def size(self, n):
		if n == None:
			return 0
		else:
			return 1 + self.size(n.left) + self.size(n.right)
	
	# tree traversals (always relative to the root) - in order, pre order, post order
	def print_post_order(self, n):
		if n == None:
			return
		self.print_post_order(n.left)
		self.print_post_order(n.right)
		print n.key
		
	# returns true if the specified sum is present in the root to leaf paths. 
	# base case is when sum becomes 0 that way we do not track running sum
	def has_path_sum(self, sum, n):		
		# A must appear before B
		#A
		if n == None and sum == 0:
			return True
		#B
		if n == None:
			return False
		
		# decrement the current node value from sum
		# pre-order: process the root, go to the leaf
		sum = sum - n.key
		print sum
		return self.has_path_sum(sum, n.left) or self.has_path_sum(sum, n.right) 
	
	# Tricky	
	# print all paths from root to leaf. Another pre-order traversal
	def print_paths(self, n, list_of_nodes, index):
		# just return. Can't print when n is none because it will print path to leaf twice
		# once because the left node of the leaf was null, other because the right node was null
		if n == None:
			return

		# first add this node to list
		# list_of_nodes.append(n.key)         # list is a mutable DS passed by reference here so if you append that value will stay
										      # when traversing to the right as well
		list_of_nodes.insert(index, n.key)	  # right node overwrites the left node on the same level in the path
		index = index + 1					  # use insert instead of list_of_nodes[index] = n.key because initially the list is [] and this will result in index out of bounds
		
		# hit a leaf node?
		if n.left == None and n.right == None:
			# print the path. DO NOT ITERATE OVER ENTIRE LIST because it can contain old nodes esp if left and right are not of the same depth.
			# index is what indicates up to which value to print
			print list_of_nodes[:index]
			print "\n"
		
		# if not, continue iterating left and then right. Preorder traversal
		self.print_paths(n.left, list_of_nodes, index)
		self.print_paths(n.right, list_of_nodes, index)
		
	# print all nodes at a given level	
	def print_nodes_on_level(self, n, list_of_lists, level):
		"""
		Use a list of lists. Every level is an index in the list of lists. Traverse the tree
		and add nodes to a list for that level
		"""
		if n == None:
			return
		
		# add this node to the appropriate list
		# check if a list exists for this level, if not create a new list and add item
		if level + 1 > len(list_of_lists):
			list = []
			list.append(n.key)
			list_of_lists.insert(level, list)
		# get the appropriate list for this level and add element
		else:
			list = list_of_lists[level]
			list.append(n.key)
		
		#go left
		self.print_nodes_on_level(n.left, list_of_lists, level + 1)
		self.print_nodes_on_level(n.right, list_of_lists, level + 1)
	
	
	# see C:\Users\Eshitha\output
	def print_graph(self):
        #bfile = open(r"F:\Projects\Algorithms\Python\Data Structures\bst.viz", "w")
		bfile = open(r"bst.dot", "w")
		bfile.write('digraph "bst" {\n')
		self._print_graph(bfile, self.root)
		bfile.write('}')
		bfile.close()
		#os.system(r"C:\Program Files (x86)\Graphviz2.38\bin\dot F:\Projects\Algorithms\Python\Data Structures\bst.viz -Tpng -o F:\Projects\Algorithms\Python\Data Structures\bst.png")
		os.system("dot -Tpng bst.dot > output.png")

	def _print_graph(self, bfile, node):
		if not node:
			return

		if node.left:
			bfile.write('\t"' + str(node.key) + '" -> "' + str(node.left.key) + '"\n')
			self._print_graph(bfile, node.left)
		if node.right:
			bfile.write('\t"' + str(node.key) + '" -> "' + str(node.right.key) + '"\n')
			self._print_graph(bfile, node.right)

"""
Caveats:
- Node gets passed as a parameter in recursion
- hasPathSum
	- pre order traversal (see image)
	- decrement sum as you go deeper
"""