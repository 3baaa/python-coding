package upload.new_upload;

import java.util.*;

/*
 * 배열 돌리기 1
 * 내가쓴 코드
 * 결과 = 맞았습니다!!
 */
public class Baekjoon_16926 {

	static int n,m;
	static int[] dx = {1,0,-1,0};
	static int[] dy = {0,1,0,-1};
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n=sc.nextInt();
		m=sc.nextInt();
		int[][] arr = new int[n][m];
		int r = sc.nextInt();
		sc.nextLine();
		for(int i=0;i<n;i++) {
			StringTokenizer st = new StringTokenizer(sc.nextLine()," ");
			for(int j=0;st.hasMoreTokens();j++) {
				arr[i][j]=Integer.valueOf(st.nextToken());
			}
		}
		for(int i=0;i<r;i++) {
			arr = rotation(arr);
		}
		
		for(int[] i : arr) {
			for(int j : i) {
				System.out.print(j+" ");
			}
			System.out.println();
		}
	}
	
	public static int[][] rotation(int[][] arr) {
		int[][] new_arr = new int[n][m];
		int t=-1;
		for(int i=0,j=0;;i++,j++) {
			if(i>=n || j>=m || new_arr[i][j]!=0) {
				break;
			}
			int x=i,y=j;
			t++;
			int tn=n,tm=m;
			for(int i2=0;i2<4;i2++) {
				int nx,ny;
				while(true) {
					nx = x+dx[i2];
					ny = y+dy[i2];
					if(nx<t || nx>=tn || ny<t || ny>=m || new_arr[nx][ny]!=0) {
						break;
					}
					new_arr[nx][ny]=arr[x][y];
					x=nx;
					y=ny;
				}
			}
		}
		return new_arr;
	}
}
