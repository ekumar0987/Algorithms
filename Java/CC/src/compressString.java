/*
 * Implement an algorithm to compress a string. Return original or compressed string depending on what is shorter
 */
public class compressString {

	public int compressedStringLength(String s){
		
		int length = 0;
		int charCount = 0;
		char[] cArray = s.toCharArray();
		
		for(int i = 0; i < cArray.length; i++){
			//2 checks: If it is the end of the array or the subsequent characters are not equal
			if(i == cArray.length-1 || cArray[i]!= cArray[i+1]){
				length = length + 1 + String.valueOf(charCount).length();
				charCount = 0;
			}
			else{
				charCount++;
			}
		}
	return length;
	}
	
	public String compressedString(String s){
		
		StringBuilder sb = new StringBuilder();                //Use of string builder to append
		
		if (s.length() < compressedStringLength(s))
			return s;
		else{
			
			char[] cArray = s.toCharArray();
			int charCount = 1;									//Very important! else in example 1, you'll see a5b0
			
			for(int i=0; i<cArray.length;i++){
				if(i == cArray.length-1 || cArray[i] != cArray[i+1]){   //2 checks here in 1 statement
					sb.append(cArray[i]);
					sb.append(String.valueOf(charCount));      //integer to string conversion
					charCount = 1;
				}
				else{
					charCount++;
				}
			}
		}
	return sb.toString();				
					
	}
	
	public static void main(String[] args) {
	
		compressString c = new compressString();
		System.out.println(c.compressedStringLength("aaaaab"));
		System.out.println(c.compressedString("aaaaab"));
		
		System.out.println(c.compressedStringLength("aaaaaaaaaaaaaaaaaaaabbb"));
		System.out.println(c.compressedString("aaaaaaaaaaaaaaaaaaaabbb"));
		
		System.out.println(c.compressedStringLength("ab"));
		System.out.println(c.compressedString("ab"));

	}

}
