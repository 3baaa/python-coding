package test;

import java.util.*;

/*
 * 정확한 순위
 * 내가쓴 코드
 * 결과값이 나온다
 */
public class _105_코딩문제_JAVA {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n=sc.nextInt();
		int m=sc.nextInt();
		int[][] a = new int[n][n];
		
		
		for(int i=0;i<m;i++) {
			int z1=sc.nextInt();
			int z2=sc.nextInt();
			a[z1-1][z2-1]=1;
		}
		
		for(int i=0;i<n;i++) {
			for(int j=0;j<n;j++) {
				for(int k=0;k<n;k++) {
					if(a[j][i]!=0 && a[i][k]!=0) {
						a[j][k]=1;
					}
				}
			}
		}
		
		for(int i=0;i<n;i++) {
			for(int j=0;j<n;j++) {
				if(a[i][j]==1) {
					a[j][i]=1;
				}
			}
		}
		
		int r=0;
		for(int i=0;i<n;i++) {
			int c=0;
			for(int j=0;j<n;j++) {
				if(a[i][j]==1) {
					c+=1;
				}
			}
			if(c==n-1) {
				r+=1;
			}
		}
		System.out.println(r);
	}

}
