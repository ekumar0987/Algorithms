
/*
 * Implement an algorithm to reverse a null terminated string
 */
public class reverseString {

	public String reverseNullTerminatedString(String s){
		
		char[] cArray = s.toCharArray();
		
		int i = 0;
		int j = cArray.length-1;
		
		while(i < j){
			char tmp = cArray[i];
			cArray[i] = cArray[j];
			cArray[j] = tmp;
			i++;
			j--;
		}
		
		return new String(cArray);
	}
	
	/*
	 * Testing
	 */
	public static void main(String[] args) {
		
		reverseString r = new reverseString();
		
		String s = "happystring";
		String reversed = r.reverseNullTerminatedString(s);
		
		System.out.println("The String is: " + s);
		System.out.print("The Reversed String is: " + reversed);
		
	}

}
