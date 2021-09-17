package upload.new_upload;

import java.util.*;

/*
 * 배열 돌리기 1
 * 내가쓴 코드
 */
public class Baekjoon_16926_w {

	static int n,m;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n=sc.nextInt();
		m=sc.nextInt();
		int[][] arr = new int[n][m];
		int r = sc.nextInt();
		for(int i=0;i<r;i++) {
			arr = rotation(arr);
		}
	}
	
	public static int[][] rotation(int[][] arr) {
		int[][] new_arr = new int[n][m];
		boolean[][] check = new boolean[n][m];
		int i_t=0,j_t=1;
		for(int i=0;i<n;i++) {
			for(int j=0;j<m;j++) {
				if(j==m-1) {
					if()
					i_t=1;
					j_t=0;
				}
				new_arr[i][j] = arr[i+i_t][j+j_t];
				m_t-=1;
			}
			i_t=-1;
		}
		return new_arr;
	}
}
