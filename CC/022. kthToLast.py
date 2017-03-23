import LinkedList_All as l

def kthToLast(ll, k):
	if ll == None:
		return None
	elif k <=0:
		return None
	else:
		tmp = ll.head
		
		# loop through list k times and you've not reached the end of the list
		while (k > 0 and tmp):
			tmp = tmp.next
			k = k - 1
		
		## k was larger than the length of the list
		if not tmp:
			return None
		
		kth = ll.head
		
		# loop until end of the list
		while(tmp.next):
			kth = kth.next
			tmp = tmp.next

		return kth
	
	
list = l.LinkedList()
list.add_first(1)
list.add_first(1)
list.add_first(2)
list.add_first(1)
list.add_first(3)
list.add_first(3)

kToLast = kthToLast(list, 1)
print kToLast.data

kToLast = kthToLast(list, 2)
print kToLast.data

kToLast = kthToLast(list, -1)
if kToLast:
	print kToLast.data

kToLast = kthToLast(list, 10)
if kToLast:
	print kToLast.data
