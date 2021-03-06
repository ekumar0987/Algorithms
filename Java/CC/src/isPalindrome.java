import datastructures.LinkedList;  //add DS to CC's build path. RC CC --> properties --> build path --> projects --> add
import datastructures.LinkedList.Node;

public class isPalindrome {
	
	public boolean isPalin(Node<Integer> lsthead, Node<Integer> rlsthead){
		
		Node<Integer> curr = lsthead;
		//Node<Integer> rCurr = reverse(l.head);  //PROBLEM: you're modifying the original list
		Node<Integer> rCurr = rlsthead; 
		
		while (curr != null && rCurr != null){
			
			System.out.print(curr.data);
			System.out.println(rCurr.data);
			
			if(curr.data != rCurr.data){
				return false;
			}
			else{
				curr = curr.next;
				rCurr = rCurr.next;
			}
		}
	
	if (curr != null || rCurr != null){
		System.out.println("here");
		return false;
	}
	
	return true;
		
	}
	
	public static Node<Integer> reverse(Node<Integer> head){
		
		Node<Integer> curr = head;
		Node<Integer> prev = null;
		
		while(curr!=null){
			Node<Integer> tmp = curr.next;
			curr.next = prev;
			prev = curr;
			curr = tmp;
		}
	return prev;  //new head
	}
	

	public static void main(String[] args) {
		
		LinkedList<Integer> list1 = new LinkedList<Integer>();
		LinkedList<Integer> list1_copy = new LinkedList<Integer>();
		
		// add when lists begin with units digits first
		list1.addLast(1);
		list1.addLast(9);
		list1.addLast(1);
		
		list1_copy = list1.copy(list1.head);
		
		isPalindrome i = new isPalindrome();
		System.out.println(i.isPalin(list1.head, reverse(list1_copy.head)));  //Very important that reverse is given a copy, else original linked list will be affected
	}

}
