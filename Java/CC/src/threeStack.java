/*
 * Algorithm to implement 3 stacks using a single array
 */
public class threeStack {
	
	public static final int stack_size = 5;
	int[] three_stacks;
	int[] stack_top_pointers;
	
	
	public threeStack(){
		three_stacks = new int[15];
		stack_top_pointers = new int[3];
		
		// Important step: Initializing to -1
		for(int i=0; i<3; i++)
			stack_top_pointers[i] = -1;
	}
	
	
	public void push(int stack_no, int item){
		
		//increment top
		stack_top_pointers[stack_no]++;
		int index = stack_no * stack_size + stack_top_pointers[stack_no];
	
		if(index == stack_size - 1)
			System.out.println("Stack is full");
		else{
			three_stacks[index] = item;
		}
	}
	
	
	public int pop(int stack_no){
		int result = 0;
		int index = stack_no * stack_size + stack_top_pointers[stack_no];
		if(index == 0)
			System.out.println("Stack is empty");
		else{
			result = three_stacks[index];
			three_stacks[index] = -1;	//Error: cannot convert from null to int. Hence used -1. This is an important step. Otherwise nothing is really deleted
			stack_top_pointers[stack_no]--;
		}
		
		return result;
	}
	
	
	public boolean isEmpty(int stack_no){
		return stack_top_pointers[stack_no] == 0;
	}
	
	public boolean isFull(int stack_no){
		return stack_top_pointers[stack_no] == stack_size - 1;
	}
	
	public void print_stack(int stack_no){
		
		System.out.println("Printing stack - " + stack_no);
		int start = stack_no * stack_size;
		for(int i = start; i < start + stack_size; i++){
			System.out.print(three_stacks[i]);
		}
		
		System.out.println();
	}
	
	
	public static void main(String[] args) {
		
		threeStack ts = new threeStack();
		
		ts.push(0, 1);
		ts.push(0, 2);
		ts.push(0, 3);
		
		ts.push(2, 3);
		ts.push(2, 2);
		ts.push(2, 1);
		
		ts.print_stack(0);
		ts.print_stack(2);
		
		System.out.println(ts.pop(0));
		System.out.println(ts.pop(0));
		ts.print_stack(0);
		
		
	}

}
