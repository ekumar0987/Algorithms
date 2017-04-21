import datastructures.BinarySearchTrees;
import datastructures.BinarySearchTrees.Node;
import java.util.*;
/*
 * Print all paths that add up to a number irrespective of the start and end nodes
 */
public class PrintAllPaths {
	
	public void printpaths(Node n, int sum, ArrayList<Integer> path, int level){
		if(n == null)
			return;
		
		//1. Add the node to path array at index level
		path.add(level, n.getdata());
		int runningsum = 0;
		
		//2. Keep iterating backwards from the level you're up to 0 and check if you find a sum along the way If yes, print!
		for(int i=level; i>=0; i--){
			runningsum = runningsum + path.get(i);
			if(runningsum == sum)
				print(path, level, i);	//Found a path from 'level' up to 'i'
		}
		System.out.println();
		
		//3. Do the same for left and right
		printpaths(n.left, sum, path, level+1);
		printpaths(n.right, sum, path, level+1);
	}
	
	public void print(ArrayList<Integer> path, int start, int end){
		for(int i=start; i>=end; i--){
			System.out.println(path.get(i));
		}
	}
	
	public static void main(String[] args) {
		
		BinarySearchTrees bst = new BinarySearchTrees();
		int[] input = {2, 5, 7, 27, 14, 8, 13, 35, 12, 59, 32, 37, 78, 70, 84, 17, 9, 26, 1, 98};
		for(int i : input){
			// inserting into a tree
			bst.insert(i, bst.root);
		}
		
		PrintAllPaths p = new PrintAllPaths();
		ArrayList<Integer> path = new ArrayList<Integer>();
		p.printpaths(bst.root, 14, path , 0);
		
	}

}
