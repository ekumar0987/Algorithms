import java.util.*;

/*
 * Implement an algorithm to determine if a string has all unique characters
 */
public class isUnique {

	/*
	 * Approach 1: Use of hash sets. O(n)
	 */
	public boolean isStringUniqueBuffer(String s){
		
		HashSet<Character> set = new HashSet<Character>();
		for(int i=0; i<s.length(); i++){
			if (set.contains(s.charAt(i)))
				return false;
			else
				set.add(s.charAt(i));
		}
		
		return true;
	}
	
	
	/*
	 * Approach 2: Use of 2 pointers. O(n2)
	 */
	public boolean isStringUniqueNoBuffer(String s){
		
		for(int i=0; i < s.length()-1; i++){
			for(int j = i+1; j < s.length(); j++){
				if (s.charAt(i) == s.charAt(j))
					return false;
			}
		}
		
		return true;
	}
	
	/*
	 * Testing
	 */
	public static void main(String[] args) {
		
		isUnique u = new isUnique();
		
		System.out.println(u.isStringUniqueBuffer("aaaac"));
		System.out.println(u.isStringUniqueBuffer("abc"));
		
		System.out.println(u.isStringUniqueNoBuffer("aaaac"));
		System.out.println(u.isStringUniqueNoBuffer("abc"));

	}

}
