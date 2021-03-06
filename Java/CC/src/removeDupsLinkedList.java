import java.util.HashSet;
import datastructures.LinkedList;  //add DS to CC's build path. RC CC --> properties --> build path --> projects --> add
import datastructures.LinkedList.Node;

public class removeDupsLinkedList {
	static HashSet<Integer> set = null;
	
	public void removeDupsWithHashMap(LinkedList<Integer> l){
		
		set = new HashSet<Integer>(l.size());
		
		Node<Integer> prev = null;
		Node<Integer> curr = l.head;
				
		while(curr != null){
			if(set.contains(curr.data)){
				//delete
				prev.next = curr.next;
			}
			else{
				//insert
				set.add(curr.data);
				prev = curr;
			}
		curr = curr.next;
		}
	}
	
	public static void main(String[] args) {
		
		removeDupsLinkedList r = new removeDupsLinkedList();
		LinkedList<Integer> l = new LinkedList<Integer>();
		
		l.addFirst(6);
		l.addFirst(6);
		l.addFirst(5);
		l.addFirst(5);
		l.addFirst(4);
		l.addFirst(1);
		
		l.print_list();
		r.removeDupsWithHashMap(l);
		l.print_list();
	}
}