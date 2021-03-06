import datastructures.LinkedList;  //add DS to CC's build path. RC CC --> properties --> build path --> projects --> add
import datastructures.LinkedList.Node;

/*
You have 2 numbers represented by a linked list where each node contains a single digit. 

Part - I: Add the digits and return the sum, if the digits are stored in reverse order
Part - II: Add the digits and return the sum, if the digits are stored in forward order
*/

public class addLinkedListNodes {
	
	int result = 0;
	LinkedList<Integer> result_list_reverse_order = new LinkedList<Integer>();
	LinkedList<Integer> result_list_forward_order = new LinkedList<Integer>();
			
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
			
			System.out.println(result % 10);
			
			result_list_reverse_order.addLast(result % 10);
			
			carry = result / 10;
			result = 0;				//Always forget to reset result
		}
		
		if(carry == 1){
			result_list_reverse_order.addLast(carry);
		}
	}
	
	public int add_forward_order(Node<Integer> n1, Node<Integer> n2){
		
		int result = 0;
		
		//base case
		if(n1==null && n2==null)
			return 0;
		
		result = n1.data + n2.data + add_forward_order(n1.next, n2.next);
		result_list_forward_order.addFirst(result % 10);
		return result / 10;
	}
	
	// important to take care of last carry if any
	public void add_forward_order_wrapper(Node<Integer> n1, Node<Integer> n2){
		
		int carry =  add_forward_order(n1, n2);
		if(carry == 1){
			result_list_forward_order.addFirst(carry);
		}
	}
	
	public void pad_lists(LinkedList<Integer> l, int len){
		
		while(len > 0){
			l.addFirst(0);
			len--;
		}
	}
		
	public void compare_list_lengths(LinkedList<Integer> l1, LinkedList<Integer> l2 ){
		
		if(l1.size() > l2.size()){
			int diff = l1.size() - l2.size();
			pad_lists(l2, diff); // pad zeroes to shorter list
		}
		else if(l2.size() > l1.size()){
			int diff = l2.size() - l1.size();
			pad_lists(l1, diff);
		}		
	}
	
	public static void main(String[] args) {
		
		// add when lists begin with units digits first
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
		a.result_list_reverse_order.print_list();
		
		// addition when lists do not begin with units digits first
		LinkedList<Integer> list3 = new LinkedList<Integer>();
		list3.addLast(9);
		list3.addLast(9);
		list3.addLast(1);
		System.out.println("List3..");
		list3.print_list();
		
		LinkedList<Integer> list4 = new LinkedList<Integer>();
		list4.addLast(9);
		System.out.println("List4..");
		list4.print_list();
		
		// pad zeroes
		a.compare_list_lengths(list3, list4);
		
		//add
		a.add_forward_order_wrapper(list3.head, list4.head);
		System.out.println("Add forward order output list..");
		list3.print_list();
		list4.print_list();
		a.result_list_forward_order.print_list();
	}

}
