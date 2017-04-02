"""
Implement a stack in which push, pop and min can be completed in O(1)
"""
import sys
class Stack:
	
	def __init__(self):
         self.items = []
		 
	def push(self, item):
		
		self.items.append(item)
		
	def pop(self):
		return self.items.pop()
	
	def peek(self):
         return self.items[len(self.items)-1]
	
	def isEmpty(self):
		return self.items == []

# wrapper class needed for customized push and pop operations
class Wrapper:
			
	stack = Stack()
	minStack = Stack()
	
	def push(self, item):
		if item < self.min():
			self.minStack.push(item)
		
		self.stack.push(item)
		
	def pop(self):
		if self.stack.peek() == self.minStack.peek():
			self.minStack.pop()
			
		return self.stack.pop()
		
	def min(self):
		if self.minStack.isEmpty():
			return sys.maxint
		else:
			return self.minStack.peek()
		
w = Wrapper()
w.push(5)
w.push(1)
w.push(9)
w.push(3)

print w.min()

w.pop()
w.pop()
w.pop()

print w.min()
