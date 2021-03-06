import java.util.Arrays;

/*
 * Given 2 string determine if one string is a permutation of the other
 */
public class isPermutation {

	public boolean isPermuationStrings(String s1, String s2){
		
		if (s1.length()!=s2.length() || !(sort(s1).equals(sort(s2))))
			return false;
		else
			return true;
	}
	
	public String sort(String s){
		
		char[] cArray = s.toCharArray();
		Arrays.sort(cArray);
		return new String(cArray);
	}
	
	public static void main(String[] args) {
		
		isPermutation p = new isPermutation();
		String s1 = "abc";
		String s2 = "cab";
		String s3 = "dad";
		
		System.out.println(p.isPermuationStrings(s1, s2));
		System.out.println(p.isPermuationStrings(s1, s3));

	}

}
