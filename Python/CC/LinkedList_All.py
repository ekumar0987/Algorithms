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
	
	# add elements from a list
	def add_from_list(self, l):
		for i in l:
			self.add_first(i)
			
	# add elements from a list to the end
	def add_from_list_last(self, l):
		for i in l:
			self.add_last(i)
			
	def size(self):
		size = 0
		tmp = self.head
		while tmp != None:
			tmp = tmp.next
			size = size + 1
			
		return size
			
	"""
	# remove an element from the list
	def remove(self, delnode):
		
		# if node is null or list is empty, return
		if not delnode or not list.head:
			return
		
		# head is the element to be deleted
		if list.head.data == delnode.data
			list.head = list.head.next

		prev = list.head
		curr = list.head.next
		
		while(curr != None):
			# data to be deleted
			if(curr.data == delnode.data):
				prev.next = curr.next
			else:
				prev = curr
			
			curr = curr.next
	"""
	
	# print contents of a list
	def print_list(self):
		curr = self.head
		while curr != None:
			print curr.get_data()
			curr = curr.next
		
		