import java.util.HashMap;
import datastructures.LinkedList;  //add DS to CC's build path. RC CC --> properties --> build path --> projects --> add

public class removeDupsLinkedList {
	
	public void removeDupsWithHashMap(){
		HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
		
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
		
		l.print(l.head);
	}

}
