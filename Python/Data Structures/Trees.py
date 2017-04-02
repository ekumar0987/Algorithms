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
	
	# depth of the tree. If only the root node is present, depth is 1
	def depth(self, n):
		if n == None:
			return 0
		else:
			return 1 + max(self.depth(n.left), self.depth(n.right))
	
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
"""