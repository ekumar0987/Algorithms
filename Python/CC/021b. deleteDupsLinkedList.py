"""
Remove duplicate elements from a list without using a tmp buffer O(n2)
"""

import LinkedList_All as l

def delete_dups_without_tmp_buffer(list):
	
	# empty list
	if not list.head:
		return
	
	outer = list.head
	
	while outer.next != None:
	
		prev = outer
		curr = outer.next
		
		while curr != None:
		
			# duplicate!
			if curr.data == outer.data:
				# delete!
				prev.next = curr.next
			
			else:
				prev = curr
				
			curr = curr.next
	
		outer = outer.next

list = l.LinkedList()
print 'Before Deletion...'
list.add_first(1)
list.add_first(1)
list.add_first(2)
list.add_first(1)
list.add_first(3)
list.add_first(3)
list.print_list()

delete_dups_without_tmp_buffer(list)

print 'After Deletion...'
list.print_list()
		

