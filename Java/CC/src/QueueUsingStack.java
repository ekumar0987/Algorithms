import datastructures.Stack; 

public class QueueUsingStack {
	
	Stack<Integer> s1;
	Stack<Integer> s2;
	
	public QueueUsingStack(){
		s1 = new Stack<Integer>(5);
		s2 = new Stack<Integer>(5);
	}
	
	// nothing new here
	public void enqueue(int item){
		s1.push(item);
	}
	
	// dequeue requires a second stack
	public int dequeue(){
		
		if(s1.isEmpty() && s2.isEmpty())
			return -1;
		
		if(s2.isEmpty()){
			while(!s1.isEmpty())
				s2.push(s1.pop());
		}
		
		return s2.pop();
	}
	
	
	public static void main(String[] args) {
		
		QueueUsingStack q = new QueueUsingStack();
		q.enqueue(5);
		q.enqueue(4);
		q.enqueue(3);
		q.enqueue(2);
		q.enqueue(1);
		
		System.out.println(q.dequeue());

	}

}
