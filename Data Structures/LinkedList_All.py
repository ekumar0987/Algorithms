"""
Custom Linked List Implementation
"""

class LinkedListNode:
	
	def __init__(self, data):
		self.data = data
		self.next = None
		
	def get_data(self):
		return self.data
		
	def get_next(self):
		return self.next
		

class LinkedList:
	
	def __init__(self):
		self.head = None
	
	# add to the begining of the list	
	def add_first(self, item):
		tmp = LinkedListNode(item)
		tmp.next = self.head
		self.head = tmp
		
	# add to the end of the list
	def add_last(self, item):
		tmp = LinkedListNode(item)
		
		# if the list is empty
		if(self.head == None):
			self.head = tmp
			return
		
		prev = self.head
		curr = self.head
		
		while(curr != None):
			prev = curr
			curr = curr.next
			
		prev.next = tmp
		
	# check if a list is empty
	def is_empty(self):
		return self.head == None
		
	# search an element in the list
	
	# remove an element from the list
	def remove(self, node, startNode):
		
		# if starting node is null, return
		if not startNode:
			return

		# if starting node is the node to be deleted
		if startNode.data == node.data:
			startNode = startNode.next
			
		prev = startNode
		curr = startNode.next
		
		while(curr != None):
			# data to be deleted
			if(curr.data == node.data):
				prev.next = curr.next
			else:
				prev = curr
			
			curr = curr.next
	
	# print contents of a list
	def print_list(self):
		curr = self.head
		while curr != None:
			print curr.get_data()
			curr = curr.next
		
		