"""
Implement a function to determine if a linked list is a palindrome
"""

import LinkedList_All as l

def reverselist(ll):

	if ll == None:
		return
		
	prev = None
	curr = ll.head
	
	while(curr):
		# grab the next
		tmp = curr.next
		
		#reverse
		curr.next = prev
		
		prev = curr
		curr = tmp
		
	return prev
	
def isPalindrome(lnkedlst):

	curr = lnkedlst.head
	rCurr = reverselist(lnkedlst.copy())   # send a copy so as to not alter the current list
	
	# both lists have elements
	while curr.data == rCurr.data:	
		curr = curr.next
		rCurr = rCurr.next
		
		# end of list
		if curr == None:
			return True
		
	return False

# testing
llst = l.LinkedList()
llst.add_last(1)
llst.add_last(2)
llst.add_last(2)
llst.add_last(1)

print isPalindrome(llst)

"""
Caveats:
- Linked list reversal
= Line 30 - sending a copy of the list
"""