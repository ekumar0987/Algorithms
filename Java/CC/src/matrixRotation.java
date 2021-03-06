/*
 * Implement a method to rotate a NxN matrix
 */
public class matrixRotation {
	
	public int[][] transposeMatrix(int[][] m){
		
		int tmp;
		for(int i=0; i<m.length; i++){
			for(int j=0; j<i; j++){
				tmp = m[i][j];
				m[i][j] = m[j][i];
				m[j][i] = tmp;
			}
		}
	return m;
	}
	
	public int[][] rotateMatrix(int[][] m){
		
		int[][] transpose = transposeMatrix(m);
		int tmp;
		
		for(int i=0; i<m.length; i++){
			for(int j=0; j<m.length/2; j++){
				tmp = transpose[i][j];
				transpose[i][j] = transpose[i][m.length-1-j];
				transpose[i][m.length-1-j] = tmp;
			}
		}
	return transpose;
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
		
		int[][] m = {{1,2,3},{4,5,6},{7,8,9}};
		
		matrixRotation mr = new matrixRotation();
		
		mr.print(m);
		
		System.out.println();
		
		int[][] rotated = mr.rotateMatrix(m);
		
		mr.print(rotated);
		
	}

}
