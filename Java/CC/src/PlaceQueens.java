/*
 * Algorithm to print all ways of arranging 8 queens on a 8 * 8 board so that
 * none of them share the same row, column or diagonal. In this case "diagonal"
 * means all diagonals, not just the 2 that bisect the board
 * 
 * 4x4:
 * { 0,  1,  0,  0}
 * { 0,  0,  0,  1}
 * { 1,  0,  0,  0}
 * { 0,  0,  1,  0}
 */
public class PlaceQueens {
	
	    /*
	     *  (A) Array whose index corresponds to rows and values in any given index correspond to the column where a queen is placed for that row
	     *      E.g. queenPlaced[0] = 0 means a queen is placed in the 1st row and 1st column
	     */
		static int GRID_SIZE = 4;
		static Integer[] queenPlaced = new Integer[GRID_SIZE];
		
		// Loop through column after column (i.e. 1st for loop loop below). For each column recursively iterate row after row
		public boolean placeQueens(int row){
			
			//Base case - Reached the last row
			if(row==GRID_SIZE){
				return true;
			}
			else{
				for(int col=0;col<GRID_SIZE;col++){
					
					if(checkValid(row,col)){
						queenPlaced[row] = col;
						
						if(placeQueens(row+1)==true)
							return true;
						else
							queenPlaced[row]=-1;
					}
				}
		return false;
		}
	}
		
	// row1 & column1 is the cell that we want to see whether a queen can be inserted
	public static boolean checkValid(int row1,int column1){
		
		// For are rows that are seen before the current row row 1, check if the same column or diagonal has been used before
		for(int row2=0; row2<row1;row2++){
			int column2 = queenPlaced[row2];
			if((column2 == column1) || ( Math.abs(column2-column1)==Math.abs(row2-row1) ))
				return false;
		}
		
		return true;
	}
	
	public static void main(String[] args) {
		//Initialize array to all -1
		for(int i=0;i<GRID_SIZE;i++){
			queenPlaced[i] = -1;
		}
		
		PlaceQueens q = new PlaceQueens();
		
		q.placeQueens(0); //Start with row 0
		
		//Print
		for(int i=0;i<GRID_SIZE;i++){
			System.out.println(queenPlaced[i]);
		}
	}

}


