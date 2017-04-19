import java.util.*;
import datastructures.Stack;  
/*
 * Set of stacks implementation - pop from a specific stack and move all elements to left
 */
public class SetOfStacksVariation {
	
	ArrayList<Stack<Integer>> sos;  				//Need an array list of stacks only! It is very hard to track stack pointers of individual stacks otherwise
	int currentstack;
	
	public SetOfStacksVariation(){
		
		sos = new ArrayList<Stack<Integer>>();
		Stack<Integer> s = new Stack<Integer>(5);	//Stack size is 5
		
		sos.add(s);
		currentstack = 0;
	}
	
	public void push(int item){
		
		Stack<Integer> s = sos.get(currentstack);
		
		if(s.isFull()){
			Stack<Integer> newstack = new Stack<Integer>(5);
			newstack.push(item);
			sos.add(newstack);
			currentstack++;
		}
		else{
			s.push(item);
		}
	}
	
	public int pop(int stacknum){
		
		if(sos.size() == 0){
			System.out.println("Set of Stacks Empty!");
			return -1;
		}
		
		Stack<Integer> s = sos.get(stacknum);
		int result = s.pop();								//Pop from the stack requested
		
		moveelements(stacknum);								//helper method that removes holes
		
		return result;
	}
	
	public void moveelements(int stacknum){
		
		for(int i = stacknum; i < sos.size() - 1; i++){			//Important: iterating only till size - 1 because we access next stack i.e. stack + 1
			Stack<Integer> nextstack = sos.get(stacknum+1);
			Stack<Integer> tmp = new Stack<Integer>(5);
			
			//move next stack elements to tmp
			while(!nextstack.isEmpty()){
				tmp.push(nextstack.pop());
			}
			
			//copy 1 element from tmp to stack with hole
			sos.get(stacknum).push(tmp.pop());
			
			//copy remaining elements from tmp back to next stack
			while(!tmp.isEmpty()){
				sos.get(stacknum+1).push(tmp.pop());
			}
		}
	}
	
	public void print(){
		for(int i = 0; i <= currentstack; i++){
			System.out.println("Printing stack.." + i);
			Stack<Integer> s = sos.get(i);
			
			System.out.println("Printing stack contents..");
			while(!s.isEmpty()){
				System.out.print(s.pop());
			}
			System.out.println();
		}	
	}
	
	public static void main(String[] args) {
		
		SetOfStacksVariation sos = new SetOfStacksVariation();
		for(int i = 0; i < 10; i++){
			sos.push(i);
		}
		
		//sos.print();
		
		System.out.println("Popped an element.." + sos.pop(0));
		
		sos.print();

	}

}
