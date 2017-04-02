"""
Implement a queue using 2 stacks
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
		 
class Queue:
	
	def __init__(self):
		self.s1 = Stack()
		self.s2 = Stack()
		
	def enqueue(self, item):
		self.s1.push(item)
		
	def dequeue(self):
		if self.s1.isEmpty() and self.s2.isEmpty():
			return
		
		# if 2nd stack is empty, move everthing from 1st stack to 2nd
		if self.s2.isEmpty():
		
			while not self.s1.isEmpty():
				self.s2.push(self.s1.pop())
				
		return self.s2.pop()

"""
Testing
"""		

q = Queue()
q.enqueue(5)
q.enqueue(4)
q.enqueue(3)
print q.dequeue()	#5

q.enqueue(2)

print q.dequeue()   #4
print q.dequeue()   #3
print q.dequeue()   #2
print q.dequeue()   # nothing