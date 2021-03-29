package test;

import java.util.*;
/*
 * 화성탐사
 * 파이썬의 답 보고 쓴코드
 */
public class _106_코딩문제2_JAVA {
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
		PriorityQueue<Z> pq = new PriorityQueue<Z>();
		pq.offer(new Z(a[0][0],0,0));
		r[0][0]=a[0][0];
		while(!pq.isEmpty()) {
			Z b = pq.poll();
			int d=b.getD();
			int x=b.getX();
			int y=b.getY();
			if(r[x][y]<d) {
				continue;
			}
			for(int i=0;i<4;i++) {
				int nx=x+dx[i];
				int ny=y+dy[i];
				if(nx>=0 && nx<n && ny>=0 && ny<n) {
					int c = d+a[nx][ny];
					if(c<r[nx][ny]) {
						r[nx][ny]=c;
						pq.offer(new Z(c,nx,ny));
					}
				}
			}
		}
	}

}

class Z implements Comparable<Z>{
	int d;
	int x;
	int y;
	Z(int d,int x,int y) {
		this.d=d;
		this.x=x;
		this.y=y;
	}
	@Override
	public int compareTo(Z d) {
		return this.d-d.d;
	}
	public int getD() {
		return d;
	}
	public int getX() {
		return x;
	}
	public int getY() {
		return y;
	}
	
	
}
