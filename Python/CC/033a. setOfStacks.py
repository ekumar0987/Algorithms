"""
Set of stacks implementation
"""

class Stack:
	def __init__(self):
		self.items = []
		self.max_size = 5

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
	
	# extra methods
	def isFull(self):
		return len(self.items) == self.max_size
		
	def printStack(self):
		print "Printing stack..."
		for i in self.items:
			print i
	
# customized push and pop operations	
class SetOfStacks:
	def __init__(self):
		self.set_of_stacks = []           
		self.current_stack_no = 0
		
	def isEmpty(self):
		return self.set_of_stacks == []
		 
	def push(self, item):
		
		# set of stacks is empty
		if self.isEmpty():
			# create new stack, push item and add stack to list of stacks
			current_stack = Stack()
			self.current_stack_no = 0
			current_stack.push(item)
			self.set_of_stacks.append(current_stack)
		else:
			# get the current stack and push item
			current_stack = self.set_of_stacks[self.current_stack_no]
			if current_stack.isFull():
				new_stack = Stack()
				new_stack.push(item)
				self.set_of_stacks.append(new_stack)
				self.current_stack_no = self.current_stack_no + 1
			else:
				current_stack.push(item)

	def pop(self):
		
		if self.isEmpty():
			return 
		
		# get current stack and pop item
		current_stack = self.set_of_stacks[self.current_stack_no]
		result = current_stack.pop()
		
		# If the stack has no more elements, delete it from the set of stacks
		if current_stack.isEmpty():
			del self.set_of_stacks[self.current_stack_no]
			self.current_stack_no = self.current_stack_no - 1
			
		return result
			
	def printSetOfStacks(self):
		
		for s in self.set_of_stacks:
			s.printStack()
			print "Next stack..."
			
"""
Caveats:
	- Need a variable to hold the pointer to the current stack
"""
		
"""
Testing
"""

set_of_stacks = SetOfStacks()
set_of_stacks.push(1)
set_of_stacks.push(2)
set_of_stacks.push(3)
set_of_stacks.push(4)
set_of_stacks.push(5)
set_of_stacks.push(6)
set_of_stacks.push(7)
set_of_stacks.push(8)
set_of_stacks.printSetOfStacks()

print set_of_stacks.pop()
print set_of_stacks.pop()
print set_of_stacks.pop()
print set_of_stacks.pop()
set_of_stacks.printSetOfStacks()
