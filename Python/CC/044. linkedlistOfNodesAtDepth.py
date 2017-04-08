"""
Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth (For e.g. if you have a tree with depth D, you'll have D linkled lists)
"""

import LinkedList_All as l
import Trees as t

list_of_linkedlists = []

def create_linkedlist_of_nodes_at_each_depth(n, level):
	
	if n == None:
		return
		
	# there is no linked list yet at this level, 
	# create a new linked list, add node to begining of linked list, add linked list to list of linked lists
	if level + 1 > len(list_of_linkedlists):
		
		linkedlist = l.LinkedList()
		
		# add tree node to the begining of list
		new_node = l.LinkedListNode(n.key)
		new_node.next = linkedlist.head 
		linkedlist.head = new_node
		
		# add linkedlist to list of linked_of_linkedlists at level
		list_of_linkedlists.insert(level, linkedlist)
	
	# a linked list already exists at this level, fetch it and add the tree node
	else:
	
		linkedlist = list_of_linkedlists[level]
		new_node = l.LinkedListNode(n.key)
		new_node.next = linkedlist.head 
		linkedlist.head = new_node
		
	
	create_linkedlist_of_nodes_at_each_depth(n.left, level + 1)
	create_linkedlist_of_nodes_at_each_depth(n.right, level + 1)
	

"""
Caveats:
	- preorder traversal
	- list of linked lists data structure
"""
	
bst = t.Trees()
lst = [2, 5, 7, 27, 14, 8, 13, 35, 12, 59, 32, 37, 78, 70, 84, 17, 9, 26, 1, 98]

for i in lst:
    bst.root = bst.insert(i, bst.root)
	
bst.print_graph()

create_linkedlist_of_nodes_at_each_depth(bst.root, 0)

for list in list_of_linkedlists:
	list.print_list()
	print "\n"

