import datastructures.LinkedList;  //add DS to CC's build path. RC CC --> properties --> build path --> projects --> add
import datastructures.LinkedList.Node;

public class kthtoLast {

	public Integer getKthToLast(Node<Integer> n, int k){
		
		if (n==null || k <0 )
			return -1;
		
		Node<Integer> tmp = n;
		for(int i=0; i<k; i++){
			tmp = tmp.next;
			
			//k > size of list
			if(tmp == null)
				return -1;
		}
		
		Node<Integer> kthtolast = n;
		
		while(tmp.next != null){
			kthtolast = kthtolast.next;
			tmp = tmp.next;
		}
		
	return kthtolast.data;
	
	}
	
	public static void main(String[] args) {
		
		LinkedList<Integer> list = new LinkedList<Integer>();
		for(int i = 0; i < 10; i++){
			list.addLast(i);
		}
		
		list.print_list();
		
		kthtoLast kthtoLast = new kthtoLast();
		
		int kthtoLastNumber = kthtoLast.getKthToLast(list.head, 2);
		
		System.out.println(kthtoLastNumber);
		
	}
}
