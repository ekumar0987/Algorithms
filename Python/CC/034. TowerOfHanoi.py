"""
Tower of Hanoi
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
		 
		 
def moveDisks(n, src, dest, buffer):

	#CRUX base case
	if n <= 0:
		return
		
	# move n-1 disks from src to buffer, using destination as buffer
	moveDisks(n-1, src, buffer, dest)
	
	# move last element to destination
	dest.push(src.pop())
	
	# move n-1 elements from buffer to destination, using source as a buffer
	moveDisks(n-1, buffer, dest, src)
	
"""
Caveats:
	- Base case
"""

"""
Testing
"""
s = Stack()
s.push(6)
s.push(5)
s.push(4)
s.push(3)
s.printStack()

d = Stack()
b = Stack()

moveDisks(4, s, d, b)

d.printStack()