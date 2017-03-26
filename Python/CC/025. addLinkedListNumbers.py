"""
You have 2 numbers represented by a linked list where each node contains a single digit. 

Part - I: Add the digits and return the sum, if the digits are stored in reverse order
Part - II: Add the digits and return the sum, if the digits are stored in forward order
"""

import LinkedList_All as l

"""
PART - I
"""
def add_reverse_order(n1, n2, rlist):
	result = 0
	carry = 0
	
	# CRUX Line: as long as there is one node
	while n1 or n2:
	
		if n1:
			result = result + n1.data
			n1 = n1.next
			
		if n2:
			result = result + n2.data
			n2 = n2.next
			
		result = result + carry
		
		rlist.add_last(result % 10)			# add_last for PART I
		
		carry = result / 10
		result = 0				            # forgot to reset initially
		
	return rlist
	
# testing
lst1 = [6, 1, 7]
lst2 = [6, 9]

ll1 = l.LinkedList()
ll1.add_from_list_last(lst1)

ll2 = l.LinkedList()
ll2.add_from_list_last(lst2)

print "The 2 lists being added are.."
ll1.print_list()
ll2.print_list()

print "The result is.."
ll_sum = add_reverse_order(ll1.head, ll2.head, l.LinkedList())
ll_sum.print_list()
	
"""
Caveats:
- No recursion needed, you add n1 and n2 data separately. Add result to list
"""

"""
PART - II
"""
def add_forward_order(n1, n2, rlist):

	result = 0
	
	if n1 == None and n2 == None:
		return 0						# base case carry value
		
	else:
		print "adding..", str(n1.data) + " ," + str(n2.data)
		result = n1.data + n2.data + add_forward_order(n1.next, n2.next, rlist)		#recursive call for carry
		rlist.add_first(result % 10)	# add_first for PART II
		return result / 10			    # carry for other cases
	
def padlist(ll):
	ll.add_first(0)
	
def equate_list_lengths(ll1, ll2):
	len_difference = ll1.size() - ll2.size()
	
	if len_difference > 0:        		#ll1 is longer than ll2
		while len_difference:
			ll2.add_first(0)	  		# pad shorter list with 0s
			len_difference = len_difference - 1
	elif len_difference < 0: 
		len_difference = abs(len_difference)
		while len_difference:
			ll1.add_first(0)	  		
			len_difference = len_difference - 1

# testing

lst1 = [7, 1, 6]
lst2 = [9, 6]

ll3 = l.LinkedList()
ll3.add_from_list_last(lst1)

ll4 = l.LinkedList()
ll4.add_from_list_last(lst2)

print "The sizes are.."
print ll3.size()
print ll4.size()

print "Padding shorter list with 0.."
equate_list_lengths(ll3, ll4) # pad lists

print "The updated sizes are.."
print ll3.size()
print ll4.size()

print "The 2 lists being added are.."
ll3.print_list()
ll4.print_list()

print "The result is.."
rlist = l.LinkedList()
add_forward_order(ll3.head, ll4.head, rlist )
rlist.print_list()

"""
Caveats:
- Lists must be of equal length, we hence need to pad zeroes
- At any point in time we are 2 numbers plus the carry, the carry is where recursion happens and we keep
  moving to the right (unit's place). 
"""
