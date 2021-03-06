import datastructures.BinarySearchTrees;
import datastructures.BinarySearchTrees.Node;

public class CommonAncestor {

	public boolean exists(Node n, int item){
		
		if(n == null)
			return false;
		
		if(n.getdata() == item)
			return true;
		else return (exists(n.left, item) || exists(n.right, item));
	
	}
	
	public Node ancestor(Node n, int n1, int n2){
		
		// If n1 and n2 do not exist in the tree at all, return
		if(!exists(n, n1) || !exists(n,n2))
			return null;
		
		boolean n1LeftSubtree = exists(n.left, n1);
		boolean n2LeftSubtree = exists(n.left, n2);
		
		//One node is in the left subtree and other is in the right
		if(n1LeftSubtree != n2LeftSubtree)
			return n;	
		
		//Both nodes in the left subtree, go left to find ancestor
		else if (n1LeftSubtree && n2LeftSubtree)
			return ancestor(n.left, n1, n2);
		
		//Both nodes in the right subtree, go right to find ancestor
		else
			return ancestor(n.right, n1, n2);	
	}
	
	public static void main(String[] args) {
		
		BinarySearchTrees bst = new BinarySearchTrees();
		int[] input = {2, 5, 7, 27, 14, 8, 13, 35, 12, 59, 32, 37, 78, 70, 84, 17, 9, 26, 1, 98};
		for(int i : input){
			// inserting into a tree
			bst.insert(i, bst.root);
		}
		
		CommonAncestor c = new CommonAncestor();
		
		System.out.println("Common Ancestor..");
		System.out.println(c.ancestor(bst.root, 37, 70).getdata());
	}

}
