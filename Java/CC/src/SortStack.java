import datastructures.Stack; 
/*
 * Sort a stack in ascending order with biggest items on top. You may use one additional stack to hold items but no other data structure
 */
public class SortStack {
	
	Stack<Integer> descending_stack;
	Stack<Integer> tmp_stack;
	
	public SortStack(){
		descending_stack = new Stack<Integer>(5);
		tmp_stack = new Stack<Integer>(5);
	}
	
	public void push(int item){
		
		// Missed condition "!descending_stack.isEmpty()"  here and got stack empty error
		if(!descending_stack.isEmpty() && item > descending_stack.peek()){
			descending_stack.push(item);
		}
		else{
			// Missed condition "!descending_stack.isEmpty()"  here and got stack empty error
			while(!descending_stack.isEmpty() && item < descending_stack.peek())   //Note: If using generics: if ((Comparable<Anytype> e).compareTo(descending_stack.peek())<0)
				tmp_stack.push(descending_stack.pop());
			
			//insert item into appropriate location
			descending_stack.push(item);
			
			while(!tmp_stack.isEmpty())
				descending_stack.push(tmp_stack.pop());
		}
	}
	
	public static void main(String[] args) {
		
		SortStack s = new SortStack();
		s.push(5);
		s.push(8);
		s.push(1);
		s.push(2);
		s.push(0);
		
		while(!s.descending_stack.isEmpty())
			System.out.println(s.descending_stack.pop());

	}

}
