"""
Implement an algorithm to delete a node in the middle of a singly linked list, 
given access to only that node
"""

import LinkedList_All as l

def deleteMiddle(n):
	n.data = n.next.data
	n.next = n.next.next

	
# testing
lst = [1, 2, 3, 4, 5, 6]
ll = l.LinkedList()
ll.add_from_list(lst)

curr = ll.head
count = 2

while(count):
	curr = curr.next
	count = count - 1

ll.print_list()

deleteMiddle(curr)

ll.print_list()