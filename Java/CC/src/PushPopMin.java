import datastructures.Stack;  

/*
 * Implement a stack in which push, pop and min can be completed in O(1) time
 */
public class PushPopMin {
	
	Stack<Integer> regular_stack = new Stack<Integer>(10);
	Stack<Integer> min_stack = new Stack<Integer>(10);
	
	public int min(){
		if(min_stack.isEmpty())
			return Integer.MAX_VALUE;
		else
			return min_stack.peek();
	}
	
	
	public void push(int item){
		if(item < min()){
			min_stack.push(item);
		}
		
		regular_stack.push(item);
	}
	
	
	public int pop(){
		
		int result = regular_stack.pop();
		if(result == min_stack.peek())
			min_stack.pop();
			
		return result;
	}
	
	public static void main(String[] args) {
		
		PushPopMin p = new PushPopMin();
		
		p.push(2);
		p.push(3);
		p.push(4);
		p.push(5);
		p.push(1);
		
		System.out.println(p.min());
		System.out.println(p.pop());
		System.out.println(p.min());
		
		
		

	}

}
