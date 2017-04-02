"""
Sort a stack in ascending order with biggest items on top. You may use one additional stack
to hold items but no other data structure
"""

class Stack:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)
	
	def printStack(self):
		print "Printing stack..."
		for i in self.items:
			print i
			
# s1 is the original stack, s2 the stack with greatest elements on top
def sortDecending(s1, s2):
	
	while not s1.isEmpty():
		tmp = s1.pop()
	
	# Find the right place for tmp in s2. 
		while not s2.isEmpty() and s2.peek() > tmp:
			s1.push(s2.pop())
		
		s2.push(tmp)
	
	return s2

"""
Testing
"""

source = Stack()
source.push(7)
source.push(0)
source.push(9)
source.push(10)
source.push(3)
source.push(8)
source.printStack()

result = Stack()
result = sortDecending(source, result)

result.printStack()
	
"""
Caveat:
 - First only put in tmp and find a spot for tmp in s2
"""

