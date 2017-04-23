/*
 * Fill all surrounding areas starting with a point outward till 
 * the entire area changes color
 */
public class PaintFill {

public static String[][] paintfill(String[][] screen, int x, int y, String oldc, String newc){
		
		//Base case - If you've reached the end of the matrix on any side return
		//(A) >= else you will get index out of bounds exception
		if(x<0 || x >= screen[0].length || y<0 || y >= screen.length)    
			return screen;
		
		if(screen[y][x]==oldc){
			screen[y][x] = newc;
			
			paintfill(screen, x-1, y, oldc, newc);	   //Recursively fill to the left of the point
			paintfill(screen, x+1, y, oldc, newc);     //right
			paintfill(screen, x, y-1, oldc, newc);     //up
			paintfill(screen, x, y+1, oldc, newc);     //down
		}
		
		return screen;
	}
	
	public static void main(String[] args) {
		
		String[][] s = {{"Red","Red","Red"},{"Red","Red","Red"},{"Red","Red","Red"}};

		s = paintfill(s,0,0,"Red","Yellow");
		
		//Printing results
		for(int i=0;i<s[0].length;i++){
			for(int j=0;j<s.length;j++){
				System.out.print(s[i][j]);
			}
		}
	}
}
