import java.util.*;
/*
 * Set of stacks implementation. When a stack gets full, create a new stack and push to that. If a stack is empty after popping an element, remove the stack from
 * the set of stacks
 */
public class SetOfStacks {
	
	ArrayList<ArrayList<Integer>> sos;
	int currentstack;
	int stacktop;
	static final int stacksize = 5;
	
	// Important initialization
	public SetOfStacks(){
		sos = new ArrayList<ArrayList<Integer>>();
		ArrayList<Integer> s = new ArrayList<Integer>();
		sos.add(s);											//Missed adding the first stack to the set!
		currentstack = 0;
		
		//This pointer needed if I have "arraylist of arraylist" and not "arraylist of stack" 
		//arraylist remove method needs an index. w/o this which element will you remove?
		stacktop = -1;
	}
	
	public void push(int item){
		ArrayList<Integer> s = sos.get(currentstack);
		System.out.println("Stack size before insert is.." + s.size());
		
		//Stack is full? Create a new stack and add items there
		if(s.size() == stacksize){
			ArrayList<Integer> newstack = new ArrayList<Integer>();
			stacktop = -1;									//Missed initializing top pointer for a new stack. This leads
			
			stacktop++;
			newstack.add(item);
			sos.add(newstack);
			currentstack++;
		}
		//Add item to existing stack
		else{
			stacktop++;
			s.add(item);
		}
	}
	
	public int pop(){
		if(sos.size() == 0){
			System.out.println("Set of Stacks Empty!");
			return -1;
		}	
		
		ArrayList<Integer> s = sos.get(currentstack);
		int result = s.remove(stacktop);
		stacktop--;
		//Stack empty? Remove from set of stacks
		if(s.size() == 0){
			sos.remove(currentstack);
			currentstack--;
		}
		
	return result;
		
	}
	
	public void print(){
		for(int i = 0; i <= currentstack; i++){
			System.out.println("Printing stack.." + i);
			ArrayList<Integer> s = sos.get(i);
			
			System.out.println("Printing stack contents..");
			for(int j = 0; j <= stacktop; j++){
				System.out.print(s.get(j));
			}
			
			System.out.println();
		}
		
	}
	
	public static void main(String[] args) {
		
		SetOfStacks sos = new SetOfStacks();
		for(int i = 0; i < 10; i++){
			sos.push(i);
		}
		
		sos.print();
		
		System.out.println("Popped an element.." + sos.pop());
		
		sos.print();

	}

}
