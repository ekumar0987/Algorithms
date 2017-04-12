import datastructures.LinkedList;  //add DS to CC's build path. RC CC --> properties --> build path --> projects --> add
import datastructures.LinkedList.Node;

/*
You have 2 numbers represented by a linked list where each node contains a single digit. 

Part - I: Add the digits and return the sum, if the digits are stored in reverse order
Part - II: Add the digits and return the sum, if the digits are stored in forward order
*/

public class addLinkedListNodes {
	
	int result = 0;
	LinkedList<Integer> result_list = new LinkedList<Integer>();
			
	public void add_reverse_order(Node<Integer> n1, Node<Integer> n2, int carry){
		
		while(n1 != null || n2!= null){
			
			if(n1 != null){
				result += n1.data;
				n1 = n1.next;
			}
			
			if(n2!=null){
				result += n2.data;
				n2 = n2.next;
			}
			
			result += carry;
			
			result_list.addLast(result % 10);
			
			carry = result / 10;
		}
		
		if(carry == 1){
			result_list.addLast(carry);
		}
	}
	
	public void add_forward_order(){
		
	}
	
	public static void main(String[] args) {
		
		LinkedList<Integer> list1 = new LinkedList<Integer>();
		list1.addLast(1);
		list1.addLast(9);
		list1.addLast(9);
		System.out.println("List1..");
		list1.print_list();
		
		LinkedList<Integer> list2 = new LinkedList<Integer>();
		list2.addLast(9);
		System.out.println("List2..");
		list2.print_list();
		
		addLinkedListNodes a = new addLinkedListNodes();
		a.add_reverse_order(list1.head, list2.head, 0);
		System.out.println("Add reverse order output list..");
		a.result_list.print_list();
		
	}

}
