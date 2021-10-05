package test;

import java.util.*;

public class Test_1 {

	public static int[][] arr1 = {
		{0,1,1,0,0,0},
		{0,1,1,0,1,1},
		{0,0,0,0,1,1},
		{0,0,0,0,1,1},
		{1,1,0,0,1,0},
		{1,1,1,0,0,0}
	};
	
	public static int[][] arr2 = {
		{0,0,0,0},
		{0,0,0,0},
		{0,0,0,0},
		{0,0,0,0}
	};
	
	
	public static int[][] arr3 = {
		{1,0,0,0},
		{1,0,0,0},
		{0,0,0,0},
		{0,0,1,1}
	};
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		t2(6,arr1);
		t2(4,arr2);
		t2(4,arr3);
	}

	public static boolean[][] check;
	public static int[] dx = {-1,1,0,0};
	public static int[] dy = {0,0,-1,1};
	public static int n;
	
	public static void t2(int t_n,int[][] arr) {
		Scanner sc = new Scanner(System.in);
		n = t_n;
		check = new boolean[n][n];
		int count=0;
		
		List<Integer> list = new ArrayList<>();
		
		for(int i=0;i<n;i++) {
			for(int j=0;j<n;j++) {
				if(check[i][j] || arr[i][j]==0) {
					continue;
				}
				count++;
				list.add(t(i,j,arr));
			}
		}
		Collections.sort(list);
		
		System.out.println();
		System.out.println(count);
		if(list.isEmpty()) {
			return;
		}
		for(int i : list) {
			System.out.print(i+" ");
		}
		System.out.println();
	}
	public static int t(int i,int j,int[][] arr) {
		
		Queue<IJ> q = new LinkedList<>();
		int r=1;
		check[i][j]=true;
		q.offer(new IJ(i,j));
		
		while(!q.isEmpty()) {
			IJ ij = q.poll();
			int x = ij.getI();
			int y = ij.getJ();
			
			for(int i2=0;i2<4;i2++) {
				int nx = x + dx[i2];
				int ny = y + dy[i2];
				if(nx<0 || nx>=n || ny<0 || ny>=n) {
					continue;
				}
				if(check[nx][ny] || arr[nx][ny]==0) {
					continue;
				}
				check[nx][ny]=true;
				r++;
				q.offer(new IJ(nx,ny));
				//System.out.println("r= "+r);
			}
		}
		return r;
	}	
}

class IJ{
	int i;
	int j;
	IJ(int i,int j){
		this.i = i;
		this.j = j;
	}
	int getI() {
		return this.i;
	}
	
	int getJ() {
		return this.j;
	}
}
