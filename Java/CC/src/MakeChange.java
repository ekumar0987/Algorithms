/*
 * Given infinite number of quarters(25 cents), dimes(10 cents), nickels(5 cents) and pennies(1 cent) 
 * write code to calculate the number of ways of representing n cents
 */
public class MakeChange {
	
	public static int makechange(int balance, int[] availableDenoms, int currDenomIndex, int[][] cache){
		
		/*
		 * (A) Base case: When the current denomination is 1, there is only 1
		 *     way to make change
		 */
		
		if(cache[balance][currDenomIndex]>0)
			return cache[balance][currDenomIndex];
		
		if(currDenomIndex == availableDenoms.length-1)
			return 1;
		
		int currentDenom = availableDenoms[currDenomIndex];
		
		int ways = 0;  //??
		for(int i=0; i*currentDenom <= balance; i++){
			int remainingBalance = balance - (i * currentDenom);
			//make change on remaining balance with remaining denoms
			ways += makechange(remainingBalance, availableDenoms, currDenomIndex+1, cache);
		}
		
		cache[balance][currDenomIndex] = ways;
		return ways;
	}
	
	public static void main(String[] args) {
		
		int n = 100;
		int[] availableDenoms = {25,10,5,1};
		int[][] cache = new int[n+1][availableDenoms.length];
		System.out.println(makechange(n, availableDenoms, 0, cache));
	}

}