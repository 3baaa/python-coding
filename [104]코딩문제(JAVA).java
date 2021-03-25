package test;

import java.util.*;

/*
 * 플로이드
 * 내가쓴 코드
 * 결과값이 나온다
 */
public class _104_코딩문제_JAVA {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		int[][] a = new int[n][n];
		
		for(int[] i : a) {
			Arrays.fill(i, 200001);
		}
		
		for(int i=0;i<n;i++) {
			a[i][i]=0;
		}
		
		for(int i=0;i<m;i++) {
			int n1 = sc.nextInt();
			int n2 = sc.nextInt();
			int n3 = sc.nextInt();
			a[n1-1][n2-1]=Integer.min(a[n1-1][n2-1], n3);
		}
		
		for(int i=0;i<n;i++) {
			for(int j=0;j<n;j++) {
				for(int k=0;k<n;k++) {
					a[j][k]=Integer.min(a[j][k], a[j][i]+a[i][k]);
				}
			}
		}
		
		for(int i=0;i<n;i++) {
			for(int j=0;j<n;j++) {
				if(a[i][j]==200001) {
					System.out.print(0+" ");
				}else {
					System.out.print(a[i][j]+" ");
				}
			}
			System.out.println();
		}
	}

}
