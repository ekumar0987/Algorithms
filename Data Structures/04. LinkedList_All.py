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
		
	def set_data(self, new_data):
		self.data = new_data
		
	def set_next(self, new_next):
		self.next = new_next

class LinkedList:
	
	def __init__(self):
		self.head = None
	
	# add to the begining of the list	
	def add_first(item):
		tmp = LinkedListNode(item)
		tmp.set_next(self.head)
		self.head = tmp
		
	# add to the end of the list
	def add_last(item):
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
	def is_empty():
		return self.head == None
		
		