"""
Linked List Tester Class
"""

import LinkedList_All as l

### sorted_insert
lst = [4,1,6,2,8,3,9,0]

llist = l.LinkedList()

for i in lst:
	new_node = l.LinkedListNode(i)
	llist.sorted_insert(new_node)
	
llist.print_list()
print "\n"

### insert_sort
lst2 = [4,1,6,2,8,3,9,0]

llist2 = l.LinkedList()
sorted_list = l.LinkedList()

for i in lst2:
	llist2.add_first(i)
	
llist2.print_list()
print "\n"

llist2.insert_sort(sorted_list)
sorted_list.print_list()
print


### front back split - 3 scenarios: even no of elements in list, odd no of elements in list, no element/one element in list
# 1
lst3 = [4,1,6,2,8,3,9,0]		
front_list = l.LinkedList()
front_list.add_from_list_last(lst3)
front_list.print_list()
print 

back_list = l.LinkedList()
back_list.head = front_list.front_back_split()

front_list.print_list()
print
back_list.print_list()

# 2
lst3 = [4,1,6,2,8,3,9]		
front_list = l.LinkedList()
front_list.add_from_list_last(lst3)
front_list.print_list()
print 

back_list = l.LinkedList()
back_list.head = front_list.front_back_split()

front_list.print_list()
print
back_list.print_list()
print

# 3
lst3 = [4]		
front_list = l.LinkedList()
front_list.add_from_list_last(lst3)
front_list.print_list()
print 

back_list = l.LinkedList()
back_list.head = front_list.front_back_split()

front_list.print_list()
print
back_list.print_list()


### move node to head
lst4 = [4,1,6,2]		
lst5 = [0,0]	
first_list = l.LinkedList()
second_list = l.LinkedList()

first_list.add_from_list_last(lst4)
first_list.print_list() 
print
second_list.add_from_list_last(lst5)
second_list.print_list() 
print

second_list.head = first_list.move_node(second_list.head)

first_list.print_list() 
print
second_list.print_list() 
print


# alternating split
lst6 = [4,1,6,2,8,3,9]	
source_list = l.LinkedList()
source_list.add_from_list_last(lst6)

result_list_1 = l.LinkedList()
result_list_2 = l.LinkedList()

source_list.print_list()
print

source_list.alternating_split(result_list_1, result_list_2)

result_list_1.print_list()
print
result_list_2.print_list()
print


# shuffle merge
print "Shuffle merge"
lst7 = [4,1,6,2]
lst8 = [8,3,9]
source_list1 = l.LinkedList()
source_list1.add_from_list_last(lst7)
source_list2 = l.LinkedList()
source_list2.add_from_list_last(lst8)

source_list1.print_list()
print
source_list2.print_list()
print

merged_list = l.LinkedList()
merged_list.head = merged_list.shuffle_merge(source_list1.head, source_list2.head)
merged_list.print_list()
print


# sorted merge
print "Sorted merge"
lst9 = [1,2,4,6]
lst10 = [3,8,9]
source_list1 = l.LinkedList()
source_list1.add_from_list_last(lst9)
source_list2 = l.LinkedList()
source_list2.add_from_list_last(lst10)

source_list1.print_list()
print
source_list2.print_list()
print

sorted_merged_list = l.LinkedList()
sorted_merged_list.head = sorted_merged_list.sorted_merge(source_list1.head, source_list2.head)
sorted_merged_list.print_list()
print

# merge sort
print "Merge sort"
lst = [4,1,6,2,8,3,9]	
source_list = l.LinkedList()
source_list.add_from_list_last(lst)
print "Before Merge Sort.."
source_list.print_list()
print "After Merge Sort.."
sorted_list.head = sorted_list.merge_sort(source_list.head)
sorted_list.print_list()






	