import datastructures.BinarySearchTrees;
import datastructures.BinarySearchTrees.Node;

/*
 * Find the inorder successor of a node in the tree
 */
public class InOrderSuccessor {
	
	public Node inordersucc(int item, Node n){
		
		Node succ = null;
		Node curr = n;
		
		while(curr!=null){						//Missed this while loop
			if(curr.getdata() < item)
				curr = curr.right;
			
			/*
			 * ****Important - Mark the left subtree parent****
			 */
			else if(curr.getdata() > item){
				succ = curr;
				curr = curr.left;
			}
			
			// item found
			else{
				// If item has a right subtree, find the leftmost child
				if(curr.right != null){
					Node tmp = curr.right;
					while(tmp.left != null)
						tmp = tmp.left;
					System.out.println("here");
					succ = tmp;
					return succ;					//Missed this return. W/o this there is an infinite loop because curr is not null and will never be since we don't change it here
				}
				else{
					return succ;					//Missed this return. W/o this again, the loop will not exit since curr is not updated
				}
			}
			
		}
		
		return succ; 
	}
	
	public static void main(String[] args) {
		
		BinarySearchTrees bst = new BinarySearchTrees();
		int[] input = {2, 5, 7, 27, 14, 8, 13, 35, 12, 59, 32, 37, 78, 70, 84, 17, 9, 26, 1, 98};
		for(int i : input){
			// inserting into a tree
			bst.insert(i, bst.root);
		}
		
		InOrderSuccessor i = new InOrderSuccessor();
		
		if(i.inordersucc(5, bst.root) != null)
			System.out.println(i.inordersucc(9, bst.root).getdata());
		else
			System.out.println("No successor");
	}

}
