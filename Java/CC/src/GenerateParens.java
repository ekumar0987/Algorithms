/*
 * Implement an algorithm to print all valid combinations of n pairs of parenthesis
 * n = 1: ()
 * n = 2: 
 * Get parens for n=1 i.e. (). Iterate over this and add paren after '('. This gives (())
 * Next add paren at to the beginning which gives ()()
 */
import java.util.*;
public class GenerateParens {

	/*
	 * Very similar to permutations
	 */
	public static HashSet<String> getParens(int n){
		
		HashSet<String> set = new HashSet<String>();
		
		// base case
		if(n == 0){
			set.add("");
			return set;
		}
		
		Set<String> prev = getParens(n-1);
		
		// this loop won't do anything for n=1 since there is no (
		for(String p: prev){
			// add () after each (
			for(int i=0; i<p.length();i++){
				if(p.charAt(i) == '('){
					String prefix = p.substring(0, i+1);
					String suffix = p.substring(i+1);
					set.add(prefix+"()"+suffix);
				}
			}
			// add () before each set of valid parens itself
			set.add("()"+p);
		}	
		return set;
	}
	
	
	public static void main(String[] args) {
		
		HashSet<String> validparens = new HashSet<String>();
		validparens = getParens(3);
		for(String s: validparens)
			System.out.println(s);

	}

}
