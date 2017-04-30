/*
 * Find the longest increasing subsequence in an array
 */
public class LongestIncreasingSubsequence{
	static int bestEnd = 0;
	
	/*
	 * O(n2) complexity DP
	 */
	public static int[] LISDP(int[] array){
		int maxLength = 1;
		//int bestEnd = 0;
		
		int[] DP = new int[array.length];
		int[] prev = new int[array.length];
		
		DP[0] = 1;
		prev[0] = -1;
	
		// (A) Outer iteration over input string starting at 1
		for (int i = 1; i < array.length; i++)
		{
		   // initial values
		   DP[i] = 1;
		   prev[i] = -1;
		   
		   // (B) Inner iteration backwards from i-1
		   for (int j = i - 1; j >= 0; j--)
		      if (DP[j] + 1 > DP[i] && array[j] < array[i])
		      {
		         DP[i] = DP[j] + 1;
		         prev[i] = j;
		      }
	
		   if (DP[i] > maxLength)
		   {
		      bestEnd = i;
		      maxLength = DP[i];
		   }
		}
		return prev;
	}
	
	/*
	 * O(nlogn) complexity
	 */

	public static void main(String[] args) {
		int[] arr = {3,1,5,2,6,4,9};
		int[] prev = LISDP(arr);
		
		System.out.println("The longest increasing subsequence is..");
		int i = bestEnd;
		while(i >=0){
			System.out.print(arr[i]+",");
			i = prev[i];
		}
	}
}
