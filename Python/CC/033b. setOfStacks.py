"""
Set of stacks implementation - pop from a specific stack and move all elements to left
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

	def pop(self, stackNo):
		
		if self.isEmpty() or stackNo > self.current_stack_no:
			return 
		
		# get stack indicated by stack no and and pop item
		stack = self.set_of_stacks[stackNo]
		result = stack.pop()
		
		# If the stack has no more elements, delete it from the set of stacks
		if stack.isEmpty():
			del self.set_of_stacks[self.stackNo]
			self.current_stack_no = self.current_stack_no - 1
		
		############################## Extra ###################################
		# Stack not empty, move element from next stack to this stack and so on to fill the hole
		# A tmp stack is used as a buffer 
		else:
			#loop over set of stacks starting from stack no
			start_stack = stackNo
			tmp_stack = Stack()
			
			# loop over all stacks till the end starting from the stack number where the item was deleted
			for i in range(start_stack, len(self.set_of_stacks)):
				
				# copy over not need for the last stack
				if i == len(self.set_of_stacks) - 1:
					break
				
				# get next stack and copy all its elements to tmp
				next_stack = self.set_of_stacks[i + 1]
				
				# push everything from next stack into tmp
				while not next_stack.isEmpty():
					tmp_stack.push(next_stack.pop())
				
				# pop 1 element from tmp into start_stack to fill hole
				self.set_of_stacks[i].push(tmp_stack.pop())
				
				# push remaining items from next stack into tmp
				while not tmp_stack.isEmpty():
					next_stack.push(tmp_stack.pop())
				
				
		return result
			
	def printSetOfStacks(self):
		
		for s in self.set_of_stacks:
			s.printStack()
			print "Next stack..."
			
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
set_of_stacks.push(9)
set_of_stacks.push(10)
set_of_stacks.push(11)
set_of_stacks.push(12)
set_of_stacks.printSetOfStacks()
print "\n"
print set_of_stacks.pop(0)
print "\n"
set_of_stacks.printSetOfStacks()