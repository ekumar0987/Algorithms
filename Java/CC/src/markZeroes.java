import java.util.ArrayList;

public class markZeroes {

	public int[][] markAllZeroes(int[][] m){
		ArrayList<Integer> row = new ArrayList<Integer>(m.length);
		ArrayList<Integer> col = new ArrayList<Integer>(m.length);
		
		//Add indices that contains zeroes
		for(int i=0; i<m.length; i++){
			for(int j=0; j<m[i].length; j++){
				if(m[i][j] == 0){
					row.add(i);
					col.add(j);
				}
			}
		}
			
		//Loop over row indices, mark all columns 0
		for (int i=0; i<row.size(); i++){
			for(int j=0;j<m[i].length; j++){
				m[row.get(i)][j] = 0;
			}
		}
		
		//Loop over col indices, mark all rows 0
		for (int j=0; j<col.size(); j++){
			for(int i=0; i<m.length; i++){
				m[i][col.get(j)] = 0;
			}
		}
		
	return m;
	}
	
	
	public void print(int[][] m){
		for(int i=0; i<m.length; i++){
			for(int j=0; j<m[i].length; j++){
				System.out.print(m[i][j]);
			}
		System.out.println();
		}
	}
		
	public static void main(String[] args) {
		
		int[][] m = {{1,2,0},{4,5,6},{7,8,9}};
		
		markZeroes mz = new markZeroes();
		
		mz.print(m);
		
		int[][] markedMatrix = mz.markAllZeroes(m);
		
		System.out.println();
		
		mz.print(markedMatrix);
	}

}
