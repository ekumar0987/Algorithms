/*
 * Implement an algorithm to insert a stream of integers as you read them and get the rank of
 * any number. The rank of a number x, is the number of values less than or equal to x
 */
public class BSTVariation {
	
	Node root;
	int rank;
	
	public BSTVariation(){
		root = null;
		rank = 0;
	}
	
	private class Node{
		int data;
		Node left;
		Node right;
		
		public Node(int data){
			this.data = data;
			this.left = null;
			this.right = null;
		}
	}
	
	public Node insert(Node n,int item){
		
		if(n==null){
			Node newnode = new Node(item);
			if(root == null)
				root = newnode;
			return newnode;
		}
		
		if(item < n.data)
			n.left = insert(n.left, item);
		else if(item > n.data)
			n.right = insert(n.right, item);
		else{
			System.out.println("Duplicate");
			return null;
		}
		
		return n;
	}
	
	public Node find(Node n, int item){
		// item not found
		if(n == null)
			return null;
		
		Node curr = n;
		if(curr.data == item)
			return curr;
		else if(curr.data > item)
			curr = find(curr.left, item);
		else if(curr.data < item)
			curr = find(curr.right, item);
	
		return curr;
	}
	
	/*
	 * (A) Variation of inorder traversal
	 */
	public int getRankOfNumber(Node n, int item){
		
		// base case
		if(n == null)
			return 0;
		
		rank += getRankOfNumber(n.left, item);
		
		if(n.data == item)
			return rank;

		rank++;
		
		rank += getRankOfNumber(n.right, item);
		
		System.out.println("Node:" + n.data);
		System.out.println("Rank:" + rank);
		
		return rank;
		
	}
	
	
	public static void main(String[] args) {
		BSTVariation bst = new BSTVariation();
		int[] input = {2, 5, 7, 27, 14, 8, 13, 35, 12, 59, 32, 37, 78, 70, 84, 17, 9, 26, 1, 98};
		for(int i : input){
			bst.insert(bst.root, i);
		}
		
		Node n = bst.find(bst.root, 14);
		System.out.println("Fetching Rank Of 14:" + bst.getRankOfNumber(n, 14));
	}

}
