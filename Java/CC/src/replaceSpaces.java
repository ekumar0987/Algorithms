/*
 * Implement an algorithm to replace all spaces with %20
 */
public class replaceSpaces {
	
	public String replaceSpacesInString(String s, int trueLength){
		
		int spaceCount = spaceCount(s);
		char[] cArray = s.toCharArray();
		
		/*Set indexes on the string*/
		int i = trueLength - 1;
		int j = trueLength + (spaceCount*2) - 1;
		
		while(i>=0 && spaceCount!=0){
			
			if(cArray[i] == ' '){
				cArray[j] = '0';
				cArray[j-1] = '2';
				cArray[j-2] = '%';
				j = j-3;
				spaceCount--;
			}
			else{
				cArray[j] = cArray[i];
				j--;
			}	
			
			i--;	
		}
		
		return new String(cArray);
	}
	
	/*
	 * Count number of spaces in the string
	 */
	public int spaceCount(String s){
		
		int spaceCount = 0;
		char[] cArray = s.toCharArray();
		for(int i=0; i<cArray.length; i++){
			if(cArray[i] == ' ')
				spaceCount++;
		}
		
		return spaceCount;
	}
	
	/*
	 * Testing
	 */
	public static void main(String[] args) {
		
		replaceSpaces r = new replaceSpaces();
		
		String s = "This is good\0\0\0\0\0\0\0\0\0\0\0\0\0";  /*Use a different character at the end to prevent it from counting as spaces*/
		System.out.println("The string is " + s);
		System.out.println("The replaced string is " + r.replaceSpacesInString(s, 12));

	}

}
