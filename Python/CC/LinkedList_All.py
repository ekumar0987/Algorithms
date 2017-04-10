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
		self.tail = None
	
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
	
	# get the length of the list
	def size(self):
		size = 0
		tmp = self.head
		while tmp != None:
			tmp = tmp.next
			size = size + 1
			
		return size
		
	def copy(self):
		
		copy = LinkedList()
		curr = self.head
		
		while curr!= None:
			copy.add_last(curr.data)
			curr = curr.next
			
		return copy
			
	# remove an element from the list
	def remove(self, delnode):
		
		# if node is null or list is empty, return
		if not delnode or not list.head:
			return
		
		# head is the element to be deleted
		if list.head.data == delnode.data:
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
	
	# insert an element into an appropriate position in the sorted linked list
	def sorted_insert(self, new_node):
		
		if self.head == None or self.head.data > new_node.data:
			new_node.next = self.head
			self.head = new_node
			return
			
		prev = None
		curr = self.head
		
		while curr and curr.data < new_node.data:
			prev = curr
			curr = curr.next
		
		prev.next = new_node
		new_node.next = curr
		
	# InsertSort() function which given a list, rearranges its nodes so they are sorted in
    # increasing order. It should use SortedInsert().
	def insert_sort(self, sorted_list):
		
		curr = self.head
		while(curr != None):
			item = curr
			curr = curr.next
			sorted_list.sorted_insert(item)
	
	# given a list, split it into 2 sublists - one for the front half, and other for the back half.
	# if the number of elements is odd, the extra element should go in the front list
	def front_back_split(self):
		back_list_head = None
		
		if self.head == None or self.head.next == None:
			return back_list_head
		
		slow = self.head
		fast = self.head.next
		
		# use 2 pointers. when fast reaches the end, slow is at the mid element
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next # IMP: fast set to one step ahead
			
		# set the back list head
		back_list_head = slow.next
		slow.next = None
			
		return back_list_head
			
	
	# hard
	# move node: Takes 2 lists, removes the front node from the second list and pushes it
	# to the front of the first
	def move_node(self, list_to_delete_head):
		
		if list_to_delete_head == None:
			return None
		
		# grab front node from listed to be deleted
		curr = list_to_delete_head
		list_to_delete_head = list_to_delete_head.next
		
		# set tmp to point to first list's head and make it head
		curr.next = self.head
		self.head = curr
		
		return list_to_delete_head
	
	# hard
	# alternating split
	def alternating_split(self, resultlist1, resultlist2):
		
		# list in which you;re iterating i.e. source
		curr = self.head
		
		# IMP
		while curr:
			# move curr to result list 1. move node will increment and return the next head element
			curr = resultlist1.move_node(curr)
			
			# move curr to result list 2 (alternating). move node will increment and return the next head element
			curr = resultlist2.move_node(curr)

	
	# move to tail - add a node to the end of the list using a "tail pointer". tail pointer needed so that you dont have to traverse the list each time
	def move_node_tail(self, node_to_insert):
		
		if node_to_insert == None:
			return
			
		if self.head == None:
			self.head = node_to_insert
			self.tail = node_to_insert
		else:
			self.tail.next = node_to_insert
			self.tail = self.tail.next
		
		# remove node's connection to the old list and return new head
		next_head = node_to_insert.next
		node_to_insert.next = None
		return next_head
	
	# given 2 lists merge their nodes together to make one list
	def shuffle_merge(self, sub_list_1_head, sub_list_2_head):
		
		curr1 = sub_list_1_head
		curr2 = sub_list_2_head
		
		while curr1 and curr2:
			
			# add both nodes one after another
			# curr1 = curr1.next and curr2 = curr2.next is not needed since the increment happens inside move_node_tail
			curr1 = self.move_node_tail(curr1)
			curr2 = self.move_node_tail(curr2)
			
		# elements still exist in the first list
		while curr1:
			curr1 = self.move_node_tail(curr1)
		
		# elements still exist in the second list
		while curr2:
			curr2 = self.move_node_tail(curr2)
		
		return self.head
	
	# given 2 lists, each of which is sorted in increasing order, merge the two into one sorted list
	def sorted_merge(self, sorted_sub_list_1_head, sorted_sub_list_2_head):
		
		curr1 = sorted_sub_list_1_head
		curr2 = sorted_sub_list_2_head
		
		while curr1 and curr2:
			
			# add smaller of the 2 to the merged list
			if curr1.data <= curr2.data:
				curr1 = self.move_node_tail(curr1)
			else:
				curr2 = self.move_node_tail(curr2)
		
		# elements still exist in the first list
		while curr1:
			curr1 = self.move_node_tail(curr1)
		
		# elements still exist in the second list
		while curr2:
			curr2 = self.move_node_tail(curr2)
		
		return self.head
		
	
	# sort an unsorted linked list
	def merge_sort(self, list_head):
		
		# base case
		if list_head == None:
			return
			
		if list_head.next == None:
			return list_head
		
		left_head = list_head
		self.head = left_head
		right_head = self.front_back_split()
		
		print "Left.."
		self.print_list_from_head(left_head)
		print
		print "Right"
		self.print_list_from_head(right_head)
		
		left_head = self.merge_sort(left_head)
		right_head = self.merge_sort(right_head)
		
		self.head = self.sorted_merge(left_head, right_head)
		
		return self.head
		
		
	# print contents of a list
	def print_list(self):
		curr = self.head
		while curr != None:
			print curr.get_data()
			curr = curr.next
			
	# print contents of a list
	def print_list_from_head(self, list_head):
		curr = list_head
		while curr != None:
			print curr.get_data()
			curr = curr.next
		
		