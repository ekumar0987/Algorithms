"""
Algorithm to implement 3 stacks using single array
"""

class threeStack():
	size = 3
	topPointers = [-1, -1, -1]
	arr = [None] * size * 3			# list with initial capacity

	def push(self, item, stackNo):
		
		if self.topPointers[stackNo] == self.size - 1:   #self needed else error "global name 'topPointers' is not defined"
			print "Stack Full"
			return
			
		self.topPointers[stackNo] = self.topPointers[stackNo] + 1    
		index = stackNo * self.size + self.topPointers[stackNo]
		
		self.arr[index] = item

	def pop(self, stackNo):
		
		if self.topPointers[stackNo] == -1:
			print "Stack Empty"
			return
			
		index = stackNo * self.size + self.topPointers[stackNo]
		result = self.arr[index]
		self.topPointers[index] = self.topPointers[index] - 1
		return result
	
"""
Testing
"""
stk = threeStack()
stk.push(1,0)
stk.push(2,0)
stk.push(3,0)
print stk.pop(0) # prints 3

stk.push(1,1)
stk.push(2,1)
stk.push(3,1)
stk.push(4,1)  #stack full error
	