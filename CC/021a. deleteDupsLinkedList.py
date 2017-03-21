"""
Remove duplicate elements from a list using a tmp buffer O(n)
"""

import LinkedList_All as l

def delete_dups_with_tmp_buffer(list):
	
	my_dict = {}
	
	# empty list
	if not list.head:
		return
		
	prev = None
	curr = list.head

	while(curr != None):
	
		# duplicate!
		if curr.data in my_dict:
			prev.next = curr.next
		
		# not a duplicate, insert data into dictionary
		else:
			my_dict[curr.data] = True
			prev = curr
		
		curr = curr.next
		

list = l.LinkedList()
print 'Before Deletion...'
list.add_first(1)
list.add_first(1)
list.add_first(2)
list.add_first(1)
list.add_first(3)
list.add_first(3)
list.print_list()

delete_dups_with_tmp_buffer(list)

print 'After Deletion...'
list.print_list()
		

