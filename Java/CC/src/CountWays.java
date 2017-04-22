/*
 * A child is running up a staircase with n steps and can hop either
 * 1, 2 or 3 steps at a time. Implement an algorithm to count how
 * many possible ways a child can run up stairs
 */
public class CountWays {

	public int count(int n){
		
		if(n < 0)
			return 0;       // no way
		
		if(n == 0)
			return 1;		// 1 way
		
		return count(n-1) + count(n-2) + count(n-3);
	}
	
	/*
	 * DP memoization
	 */
	public int countDP(int n, int[] map){
		if(n < 0)
			return 0;
		if(n == 0)
			return 1;
		if(map[n] > -1)
			return map[n];
		else{
			map[n] = countDP(n-1, map) + countDP(n-2, map) + countDP(n-3, map);
		    return map[n];
		}
	}
	
	public static void main(String[] args) {
		CountWays c = new CountWays();
		int [] map = new int[100];
		for(int i=0; i<map.length; i++)
			map[i] = -1;				// 0 by default
			
		System.out.println("Count for 1 step:" + c.countDP(1, map));
		System.out.println("Count for 2 step:" + c.countDP(2, map));
		System.out.println("Count for 3 step:" + c.countDP(3, map));
		System.out.println("Count for 4 step:" + c.countDP(4, map));
		System.out.println("Count for 5 step:" + c.countDP(5, map));
	}
}

/*
 * Issues: Number of ways will overflow the bounds of an integer by the time you get to just n=37
 */