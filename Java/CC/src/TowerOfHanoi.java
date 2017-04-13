import datastructures.Stack;  
/*
 * Tower Of Hanoi implementation
 */
public class TowerOfHanoi {

	public void movedisks(int n, Stack<Integer> source, Stack<Integer> buffer, Stack<Integer> dest){
		
		// Important, made a mistake here. checked for n==1 intially which is wrong
		if(n <= 0){
			return;
		}
		
		//n-1 disks from source to buffer
		movedisks(n-1, source, dest, buffer);
		dest.push(source.pop());
		//n-1 disks from buffer to dest
		movedisks(n-1, buffer, source, dest);
	}
	
	public static void main(String[] args) {
		
		TowerOfHanoi t = new TowerOfHanoi();
		
		Stack<Integer> s = new Stack<Integer>(5);
		Stack<Integer> b = new Stack<Integer>(5);
		Stack<Integer> d = new Stack<Integer>(5);
		
		s.push(5);
		s.push(4);
		s.push(3);
		
		t.movedisks(3,s,b,d);
		
		for(int i=0; i< 3; i++){
			System.out.println(d.pop());
		}
		
	}

}
