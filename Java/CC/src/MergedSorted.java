/*
 * Given 2 sorted arrays, A and B, where A has a large enough buffer at the end to hold B. Write a method to merge B into A in sorted order
 */
public class MergedSorted {

	public int[] merge(int[] a, int[] b, int lenA, int lenB){
		
		int indexA = lenA - 1;
		int indexB = lenB - 1;
		int indexMerged = lenA + lenB - 1;
		
		/*
		 * (A)Important outer loop only indexB. If we're done with A, we still need to copy over B. So the outer loop goes on till indexB reaches the start of array B.
		 * What if we're done with B? We still don't need to loop over indexA because we're elements into A and the elements are already in the right sorted order
		 */
		while(indexB >= 0){
			
			/*
			 * (B) Check for indexA here. When you're done with A and still left with elements in B, indexA = -1. W/O the check a[indexA] will fail
			 * (C) Insertions done from the end of the array, unlike merge sort where we insert from the start
			 */
			if(indexA >=0 && a[indexA] > b[indexB]){		// > handled here
				a[indexMerged] = a[indexA];
				indexA--;
			}
			else{
				a[indexMerged] = b[indexB];					// <, = handled here
				indexB--;
			}
			
			indexMerged--;
		}
	return a;
	}
	
	public static void main(String[] args) {
		
		MergedSorted m = new MergedSorted();
		
		//Test Case 1
		int[] a1 = {1,3,5,7,9,-1,-1,-1,-1,-1};
		int[] b1 = {2,4,6,8,10};
		
		int[] sorted1 = m.merge(a1, b1, 5, 5);
		
		for(int i=0; i<sorted1.length; i++){
			System.out.print(sorted1[i]);
			System.out.print(",");
		}
		
		System.out.println();
		
		//Test Case 2
		int[] a2 = {4,5,6,7,8,-1,-1,-1,-1,-1};
		int[] b2 = {0,1,2,3,4};
		
		int[] sorted2 = m.merge(a2, b2, 5, 5);
		
		for(int i=0; i<sorted2.length; i++){
			System.out.print(sorted2[i]);
			System.out.print(",");
		}
		
		
	}

}
