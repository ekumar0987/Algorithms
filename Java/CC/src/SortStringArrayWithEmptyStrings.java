/*
 * Given a sorted array of strings interspersed with empty strings write a method to find the location of a given string
 * Considerations: What if someone searches for an empty string?
 */
public class SortStringArrayWithEmptyStrings {
	
	public int search(String[] sArr, int left, int right, String x){
		
		if(left > right)
			return -1;
		
		int mid = (left + right) / 2;
		
		/*
		 * (A) If mid is empty, move right to find non empty mid. If you reach the end of the array there
		 *     look left to find a non empty mid
		 */
		if(sArr[mid].isEmpty()){
			
			/*
			 * (B) New indices that go left and right looking for non empty mid
			 */
			int midleft = mid - 1;
			int midright = mid + 1;
			
			while(true){
				
				if(midleft < left && midright > right)
					return -1;
				
				// look for a nonempty mid on the right
				if(midright <= right && !sArr[midright].isEmpty()){
					mid = midright;
					break;
				}
				
				// look for a non empty mid on the left
				else if (midleft >= left && !sArr[midleft].isEmpty()){
					mid = midleft;
					break;
				}
				
				// increment/decrement pointers as we didn't find a non empty mid on this iteration
				midright++;
				midleft--;
			}
		}
		
		if(sArr[mid].equals(x))
			return mid;
		else if (sArr[mid].compareTo(x) < 0)			// search right
			return search(sArr, mid+1, right, x);
		else											// search left
			return search(sArr, left, mid-1, x);
	}
	
	public static void main(String[] args) {
		
		SortStringArrayWithEmptyStrings s = new SortStringArrayWithEmptyStrings();
		
		// Test Case 1:
		String[] s1 = {"", "abc", "def","","","","ghi","jk","","","","zzz"};
		int r1 = s.search(s1, 0, s1.length-1, "zzz");
		System.out.println("Index:"+r1);
		
		System.out.println();
		
		// Test Case 2:
		String[] s2 = {"", "abc", "def","","","","ghi","jk","","","","zzz"};
		int r2 = s.search(s2, 0, s2.length-1, "adg");
		System.out.println("Index:"+r2);
		
		System.out.println();
		
		// Test Case 3:
		String[] s3 = {"", "abc", "def","","","","ghi","jk","","","","zzz"};
		int r3 = s.search(s3, 0, s3.length-1, "abc");
		System.out.println("Index:"+r3);
		
		System.out.println();
	}
}
