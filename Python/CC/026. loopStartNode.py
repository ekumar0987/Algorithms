"""
Given a circular linked list implement an algorithm thaat returns a node at the begining of the loop
"""

def loop_start_node(n):

	if n == None:
		return
		
	slow = n.head
	fast = n.head
	
	while (fast != None and fast.next != None):
		slow = slow.next
		fast = fast.next.next
		
		if slow == fast
			break
	
	# no meeting poing
	if fast == None or fast.next == None:
		return
	
	slow = n.head
	
	while slow != fast:
		slow = slow.next
		fast = fast.next
		
	return fast