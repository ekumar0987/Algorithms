/*
 * A magic index in an array A[1...n-1] is defined to be an index such that A[i] = i.
 * Given a sorted array of distinct integers, write a method to find a magic index, if
 * one exists. What if the values are not distinct
 */
public class MagicIndex {
	
	// array elements are distinct
	public int mindex(int[] arr, int left, int right){
		if(left > right)
			return -1;
		
		int mid = (left + right)/2;
		if(mid == arr[mid])
			return mid;
		
		/*
		 * (A) Knowing which side the magic index could potentially fall on
		 */
		if(mid < arr[mid])	// magic index could only be on the left
			return mindex(arr, left, mid-1);
		else
			return mindex(arr, mid+1, right);
	}
	
	// array elements are not distinct
	
	
	public static void main(String[] args) {
		MagicIndex m = new MagicIndex();
		int[] arr = {-40,-20,-1,1,2,3,5,7,9,12,13};
		
		System.out.println("The magic index is: " + m.mindex(arr, 0, arr.length-1));	
	}
}
