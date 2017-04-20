import datastructures.BinarySearchTrees.Node;

/*
 * Create a binary search tree from a sorted array
 * 
 * The tree is built within this method itself. Hence no BST class methods are needed. Node class is needed though
 */
public class createBST {
	
	public class Node{
		
		int data;
		public Node left;
		public Node right;
		
		public Node(int data){
			this.data = data;
			this.left = null;
			this.right = null;
			}
		}

	public Node createBST(int[] arr, int low, int high){
		
		if(low > high)
			return null;
		
		int mid = (low + high) / 2;
		
		Node n = new Node(arr[mid]); 
		
		n.left = createBST(arr, low, mid-1);
		n.right = createBST(arr, mid+1, high);
		
		return n;
	}
	
	/*
	 * Helper methods
	 */
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
		
		createBST c = new createBST();
		int[] arr = {1,2,3,4,5,6,7};
		
		Node root = c.createBST(arr, 0, arr.length-1);
		
		System.out.println(getDotFile(root));
	}

}
