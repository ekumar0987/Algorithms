package datastructures;

public class Stack<Anytype> {
	
	public int top;
	Anytype[] arr;
	private static final int initial_capacity = 20;
	int size;
	
	@SuppressWarnings("unchecked")
	public Stack(int size){
		if(size <= 0)
			arr = (Anytype[]) new Object[initial_capacity];
		else
			arr = (Anytype[]) new Object[size];
		
		top = -1;
		this.size = size;
	}
	
	
	public void push(Anytype item){
		
		if(isFull()){
			System.out.println("Stack Empty");
			return;
		}
		arr[++top] = item;
	}
	
	public Anytype pop(){
		Anytype result = null;	//local variables must always be initialized
		
		if(isEmpty()){
			System.out.println("Stack is empty");
		}
		else{
			result = arr[top];
			arr[top] = null;
			top--;
		}	
	return result;
	}
	
	public Anytype peek(){
		
		if(isEmpty()){
			System.out.println("Stack is empty");
			return null;
		}
		else
			return arr[top];
	}
	
	public boolean isEmpty(){
		return top == -1;
	}
	
	public boolean isFull(){
		return top == size - 1;	
	}
}
