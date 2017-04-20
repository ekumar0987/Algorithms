package datastructures;

public class BinarySearchTrees {

	Node root;
	
	public BinarySearchTrees(){
		root = null;
	}
	
	/*
	 * 1 - Recursive Insert
	 */
	public Node insert(int item, Node n){
		
		// new nodes are created at the leaf where n is null
		if(n == null){
			Node newnode = new Node(item);
			
			if(root == null)
				root = newnode;
			
			return newnode;
		}
		
		Node curr = n;
		if(curr.data == item){
			System.out.println("Duplicate Entry");
			return null;
		}
		else if(curr.data < item)
			curr.right = insert(item, curr.right);
		else if(curr.data > item)
			curr.left = insert(item, curr.left);
		
		return curr;
	}
	
	/*
	 * 2 - Recursive Find
	 */
	public boolean find(int item, Node n){
		boolean result = false;
		
		// item not found
		if(n == null)
			return false;
		
		Node curr = n;
		if(curr.data == item)
			result = true;
		else if(curr.data > item)
			result = find(item, curr.left);
		else if(curr.data < item)
			result = find(item, curr.right);
	
		return result;
	}
	
	/*
	 * 3 - FindMin
	 */
	public Node findmin(Node n){
		if(n == null)
			return null;
		
		if(n.left == null)
			return n;
		else
			return findmin(n.left);
	}
	
	/*
	 * 4 - FindMax
	 */
	public Node findmax(Node n){
		if(n == null)
			return null;
		
		if(n.right == null)
			return n;
		else
			return findmax(n.right);			
	}
	
	/*
	 * 5 - Delete - Base at the end + 3 recursive delete calls - tricky!
	 */
	public Node delete(int item, Node n){
		
		//nothing to delete
		if(n == null)
			return null;
		
		Node curr = n;
		if(curr.data > item)
			curr.left = delete(item, curr.left);				// Similar for inserts and deleted
		else if (curr.data < item)
			curr.right = delete(item, curr.right);
		//found the key
		else{
			//leaf
			if (curr.left == null && curr.right == null)
				curr = null;
			//has right child
			else if (curr.left == null)
				curr = curr.right;
			//has left child
			else if (curr.right == null)
				curr = curr.left;
			//has both left and right
			else{
				Node succ = findmin(curr.right);
				curr.data = succ.data;								//Replace curr with succ data
				curr.right = delete(succ.data, curr.right);		//Another recursive call to delete the succ node
			}
		}
		return curr;
	}
	
	
	public class Node{
		
		int data;
		Node left;
		Node right;
		
		public Node(int data){
			this.data = data;
			this.left = null;
			this.right = null;
		}
		
		public int getdata(){
			return this.data;
		}
		
	}
	
	// Generating the tree with graph viz
	// Copy paste code into C:\Users\Eshitha\tree
	// Run this in cmd - dot tree.dot | neato -n -Tpng -o treejavaoutput.png
	// Output is in C:\Users\Eshitha\
	public static String getDotFile(Node rt){
		  StringBuilder sb = new StringBuilder();
		  sb.append("digraph G {\n");
		  sb.append("graph [ dpi = 150 ]\n"); 
		  sb.append("nodesep=0.3;\n");
		  sb.append("ranksep=0.2;\n");
		  sb.append("margin=0.1;\n");
		  sb.append("node [shape=circle];\n");
		  sb.append("edge [arrowsize=0.8];\n");
		  
		  StringBuilder treeContent = getDotTreeContent(new StringBuilder(), rt, 1);
		  sb.append(treeContent);
		  
		  sb.append("}");
		  
		  return sb.toString();
		}

		private static StringBuilder getDotTreeContent(StringBuilder sb, Node n, int i){
		  sb.append(String.format("node%d [label=\"%d\"];\n", i, n.data));
		  int lChild = 2*i;
		  int rChild = 2*i + 1;
		  
		  if(n.left  != null){
		    sb.append(String.format("node%d -> node%d;\n", i, lChild));
		    getDotTreeContent(sb, n.left, lChild);
		  }
		  if(n.right != null){
		    sb.append(String.format("node%d -> node%d;\n", i, rChild));
		    getDotTreeContent(sb, n.right, rChild);
		  }
		  return sb;
		}
	
	public static void main(String[] args) {
		
		BinarySearchTrees bst = new BinarySearchTrees();
		System.out.println("here");
		
		int[] input = {2, 5, 7, 27, 14, 8, 13, 35, 12, 59, 32, 37, 78, 70, 84, 17, 9, 26, 1, 98};
		for(int i : input){
			// inserting into a tree
			bst.insert(i, bst.root);
		}
		
		//System.out.println(getDotFile(bst.root));
		
		// searching a tree
		System.out.println(bst.find(2, bst.root));
		System.out.println(bst.find(5, bst.root));
		
		//deleting
		Node deleted = bst.delete(2, bst.root);
		System.out.println(deleted.data);
		System.out.println(getDotFile(bst.root));
	}

}
