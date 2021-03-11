package test;

import java.util.Arrays;
import java.util.Scanner;
import java.util.*;
/*
 * 금광
 * 내가쓴 코드
 * 결과값이 나온다
 */
public class _91_코딩문제_JAVA {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t= sc.nextInt();
		sc.nextLine();
		for(int i=0;i<t;i++) {
			String[] nm=sc.nextLine().split("\\s");
			int n = Integer.parseInt(nm[0]);
			int m = Integer.parseInt(nm[1]);
			int[] r = new int[n];
			int[][] a = new int[n][m];
			String[] str = sc.nextLine().split("\\s");
			int k=0;
			for(int j=0;j<n;j++) {
				r[j]=Integer.parseInt(str[k]);
				for(int l=0;l<m;l++) {
					a[j][l]=Integer.parseInt(str[k]);
					k++;
				}
			}
			int[] dx= {1,0,-1};
			for(int ii=0;ii<n;ii++) {
			int x=ii,y=0;
			int tx=ii,ty=0;
			for(int j=1;j<m;j++) {
				int z=0;
				for(int k2=0;k2<3;k2++) {
					int nx=x+dx[k2];
					int ny=y+1;
					if(nx>=0 && nx<n && z<a[nx][ny]) {
						z=a[nx][ny];
						tx=nx;
						ty=ny;
					}
				}
				r[ii]+=z;
				x=tx;
				y=ty;
			}
		}
		Arrays.sort(r);
		System.out.println(r[r.length-1]);
		}
		}
}
