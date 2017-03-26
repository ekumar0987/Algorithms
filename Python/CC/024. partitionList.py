"""
Write code to partition a linkedlist around a value x, such that all nodes less than x comes before
all nodes greater than or **EQUAL** to x
"""

import LinkedList_All 

def partitionList(ll, value):

	if ll == None:
		return
		
	prev = None
	curr = ll.head
	
	while(curr):
		# the first node itself is less than value, do nothing. the check for head is needed
		# because at this point prev is still None and we cannot delete data using prev
		if (curr == ll.head) or (curr.data >= value):
			prev = curr
			curr = curr.next
		# add node to the begining of the list and delete it from the current position
		else:
			###### CRUX ########
			prev.next = curr.next
			curr.next = ll.head
			ll.head = curr
			curr = prev.next
	
	return ll
			
# testing
lst = [10, 9, 7, 6, 8]
linkedlst = LinkedList_All.LinkedList()
linkedlst.add_from_list_last(lst)

print linkedlst.print_list()
#10 - 9 - 7 - 6 - 8

partionedlst = partitionList(linkedlst, 8)

print partionedlst.print_list()
# 6 - 7 - 10 - 9 - 8

"""
Caveats:
- add smaller elements to the begining of the list instead of adding larger elements to the end 
  of the list because add last will be o(n2)
- the above algo is in place. Another approach would be to create 2 lists that hold smaller and larger 
  elements and then join the 2 but that is not in place
"""
				
