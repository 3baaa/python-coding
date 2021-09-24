package upload.new_upload;

import java.util.*;

/*
 * 주사위 굴리기
 * 내가쓴 코드
 */

public class Baekjoon_14499_w {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt(),m=sc.nextInt(),x=sc.nextInt(),y=sc.nextInt(),k=sc.nextInt();
		int[][] arr = new int[n][m];
		int[] karr= new int[k];
		int[] dice = new int[6];
		for(int i=0;i<n;i++) {
			StringTokenizer st = new StringTokenizer(sc.nextLine()," ");
			for(int j = 0;st.hasMoreTokens();j++) {
				arr[i][j]=Integer.valueOf(st.nextToken());
			}
		}
		for(int i=0;i<k;i++) {
			karr[i]=sc.nextInt();
		}
		
	}

}
