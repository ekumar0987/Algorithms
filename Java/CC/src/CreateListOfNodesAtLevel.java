import datastructures.BinarySearchTrees;
import datastructures.BinarySearchTrees.Node;
import datastructures.LinkedList;
import java.util.*;

public class CreateListOfNodesAtLevel {
	
	ArrayList<LinkedList<Integer>> arrlist = new ArrayList<LinkedList<Integer>>();
	
	public void createLL(Node n, int level){
		
		if(n == null)
			return;
		
		// no linked list exists yet
		if(arrlist.size() == level - 1){
			LinkedList<Integer> lst = new LinkedList<Integer>();
			lst.addFirst(n.getdata());
			arrlist.add(lst);
		}
		// a linked list already exists at this level
		else{
			LinkedList<Integer> lst = arrlist.get(level - 1);   //Used level instead of level - 1
			lst.addFirst(n.getdata());
		}
		
		//Process left
		createLL(n.left, level + 1);
		createLL(n.right, level + 1);
		
	}
	
	public void printAL(){
		
		for(int i = 0; i < arrlist.size(); i++){
			System.out.print("Printing list at level.." + i+1);
			arrlist.get(i).print_list();
		}
	}
	
	public static void main(String[] args) {
		
		BinarySearchTrees bst = new BinarySearchTrees();
		
		int[] input = {2, 5, 7, 27, 14, 8, 13, 35, 12, 59, 32, 37, 78, 70, 84, 17, 9, 26, 1, 98};
		for(int i : input){
			bst.insert(i, bst.root);
		}
		
		CreateListOfNodesAtLevel c = new CreateListOfNodesAtLevel();
		c.createLL(bst.root, 1); //level starts at 1
		c.printAL();
	}

}
