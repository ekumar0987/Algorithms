package datastructures;

import java.util.Iterator;

/**
 * Singly Linked List Class (1 of 3)
 * @author Eshitha
 *
 * @param <Anytype>
 */
public class LinkedList<Anytype> implements Iterable<Anytype> {
	
	public Node<Anytype> head;
	
	public LinkedList(){
		head = null;
	}
	
	/**
	 * Node Class (2 of 3)
	 * @author Eshitha
	 *
	 * @param <Anytype>
	 */
	private static class Node<Anytype> {
		Anytype data;
		Node<Anytype> next;
		
		public Node(Anytype data, Node<Anytype> next){
			this.data = data;
			this.next = null;
		}
	}
	
	/* Iterable interface method - Mandatory */
	public Iterator<Anytype> iterator(){
		return new SinglyLinkedListIterator();
	}
	
	/**
	 * Singly Linked List Iterator Class (3 of 3)
	 * @author Eshitha
	 *
	 */
	private class SinglyLinkedListIterator implements Iterator<Anytype>{
		private Node<Anytype> nextNode;
		
		SinglyLinkedListIterator(){
			nextNode = head;
		}
		
		public boolean hasNext(){
			return nextNode != null;
		}
		
		public Anytype next(){
			if (!hasNext())
				return null;
			
			Anytype result = nextNode.data;
			nextNode = nextNode.next;
			return result;
		}
		
		public void remove(){
			
		}
	}
	
	/**
	 *  Linked List Methods: addFirst, addLast, insertAfter, insertBefore, remove
	 */
	public void addFirst(Anytype item){
		head = new Node<Anytype>(item, head);
	}
	
	public void addLast(Anytype item){
		if (head == null)
			addFirst(item);
		
		Node<Anytype> tmp = head;
		while (tmp.next != null)
			tmp = tmp.next;
		
		tmp.next = new Node<Anytype>(item, null);
	}
	
	public void insertAfter(Anytype item, Anytype key){
		if (head == null)
			return;
		
		Node<Anytype> tmp = head;
		
		while(tmp!=null && !tmp.data.equals(key))
			tmp = tmp.next;
		
		//key not found
		if (tmp==null)
			return;
				
		tmp.next = new Node<Anytype>(item, tmp.next);
	}
	
	public void insertBefore(Anytype item, Anytype key){
		if (head == null)
			return;
		
		if (head.data.equals(key)){
			addFirst(item);
			return;
		}
		
		Node<Anytype> prev = null;
		Node<Anytype> curr = head;
		
		while(curr!=null && !curr.data.equals(key)){
			prev = curr;
			curr = curr.next;
		}
		
		if(curr!=null)
			prev.next = new Node<Anytype>(item,curr);
	}
	
	public void remove(Anytype item){
		if (head == null)
			return;
		
		if(head.data.equals(item))
			head = null;
		
		Node<Anytype> prev = null;
		Node<Anytype> curr = head;
		
		while(curr!=null && !curr.data.equals(item)){
			prev = curr;
			curr = curr.next;
		}
		
		if(curr==null){
			//item not found
		}
		else
			prev.next = curr.next;
		
	}
	
	public void print(Node<Anytype> n) {
        String result = "";
        Node<Anytype> current = n;
        while(current != null){
            result += current.data + ", ";
            current = current.next;
        }
        System.out.println("List: " + result);
}
	
	
}