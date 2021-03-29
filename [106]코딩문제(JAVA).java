package test;

import java.util.*;
/*
 * 화성탐사
 * 내가쓴 코드
 * 결과값이 나온다
 */
public class _106_코딩문제_JAVA {
	static int[] dx = {-1,1,0,0};
	static int[] dy = {0,0,-1,1};
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int t = sc.nextInt();
		for(int i=0;i<t;i++) {
			int n = sc.nextInt();
			int[][] a = new int[n][n];
			for(int j=0;j<n;j++) {
				for(int k=0;k<n;k++) {
					a[j][k]=sc.nextInt();
				}
			}
			int[][] r = new int[n][n];
			for(int[] b : r) {
				Arrays.fill(b, (int)1e9);
			}
			zz(a,r,n);
			System.out.println(r[n-1][n-1]);
		}
	}
	
	public static void zz(int[][] a,int[][] r,int n) {
		Queue<int[]> q = new LinkedList<int[]>();
		q.offer(new int[]{0,0});
		r[0][0]=a[0][0];
		while(!q.isEmpty()) {
			int[] b = q.poll();
			int x=b[0];
			int y=b[1];
			for(int i=0;i<4;i++) {
				int nx=x+dx[i];
				int ny=y+dy[i];
				if(nx>=0 && nx<n && ny>=0 && ny<n && r[nx][ny]>r[x][y]+a[nx][ny]) {
					q.offer(new int[] {nx,ny});
					r[nx][ny]=r[x][y]+a[nx][ny];
				}
			}
		}
	}

}
