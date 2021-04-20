package test;

/*
 * 단지번호붙이기
 * 내가쓴 코드
 * 결과 = 맞았습니다!!
 */

import java.util.*;

public class _117_코딩문제_JAVA_단지번호붙이기 {
	
	static int c=0;
	static int r1=0;
	static int n;
	static boolean[][] v;
	static int[][] a;
	static int[] dx = {-1,1,0,0};
	static int[] dy = {0,0,-1,1};
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n=sc.nextInt();
		sc.nextLine();
		List<Integer> r2 = new ArrayList<Integer>();
		a=new int[n][n];
		v=new boolean[n][n];
		for(int i=0;i<n;i++) {
			String[] s = sc.nextLine().split("");
			for(int j=0;j<s.length;j++) {
				a[i][j]=Integer.parseInt(s[j]);
			}
		}
		
		for(int i=0;i<n;i++) {
			for(int j=0;j<n;j++) {
				if(a[i][j]==0) {
					continue;
				}
				if(!v[i][j]) {
					r1+=1;
					b(i,j);
					r2.add(c);
					c=0;
				}
			}
		}
		
		System.out.println(r1);
		Collections.sort(r2);
		for(int i : r2) {
			System.out.println(i);
		}
	}

	static void b(int n1,int n2) {
		Queue<ZZ> q = new LinkedList<ZZ>();
		q.add(new ZZ(n1,n2));
		v[n1][n2]=true;
		a[n1][n2]=r1;
		c+=1;
		
		while(!q.isEmpty()) {
			ZZ z = q.poll();
			int x=z.getX();
			int y=z.getY();
			for(int i=0;i<4;i++) {
				int nx=x+dx[i];
				int ny=y+dy[i];
				if(nx>=0 && nx<n && ny>=0 && ny<n && a[nx][ny]==1) {
					if(! v[nx][ny]) {
						v[nx][ny]=true;
						a[nx][ny]=r1;
						c+=1;
						q.offer(new ZZ(nx,ny));
					}
				}
			}
		}
		
	}
}

class ZZ {
	private int x;
	private int y;
	
	public ZZ(int x,int y) {
		this.x=x;
		this.y=y;
	}

	public int getX() {
		return x;
	}

	public int getY() {
		return y;
	}
	
	
}