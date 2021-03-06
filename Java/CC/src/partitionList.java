import datastructures.LinkedList;  //add DS to CC's build path. RC CC --> properties --> build path --> projects --> add
import datastructures.LinkedList.Node;

public class partitionList {
	
	public Node<Integer> partitionList(Node<Integer> n, int pivot){
		
		Node<Integer> prev = n;
		Node<Integer> curr = n;
		Node<Integer> tmp = null;
				
		while(curr != null){
			
			// for numbers larger than the pivot, keep iterating
			if(curr.data >= pivot){
				prev = curr;
				curr = curr.next;
			}
			else{
				tmp = curr;
				
				//delete smaller element from list
				prev.next = curr.next;
				curr = curr.next;
				
				//add tmp to the beginning of the list
				tmp.next = n;
				n = tmp;
						
			}
		}
	return n;	
	}
	
	public static void main(String[] args) {
		
		LinkedList<Integer> list = new LinkedList<Integer>();
		for(int i = 10; i > 0; i--){
			list.addLast(i);
		}
		
		int pivot = 7;
		
		System.out.println("Before partition..");
		list.print_list();
		
		partitionList p = new partitionList();
		list.head = p.partitionList(list.head, pivot);
		
		System.out.println("After partition..");
		list.print_list();
		
	}

}
