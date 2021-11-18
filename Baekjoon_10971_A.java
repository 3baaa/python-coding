package upload.new_upload;

import java.util.*;

/*
 * 외판원 순회 2
 * 답
 */
public class Baekjoon_10971_A {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[][] a = new int[n][n];
		for(int i=0;i<n;i++) {
			for(int j=0;j<n;j++) {
				a[i][j] = sc.nextInt();
			}
		}
		int[] d = new int[n];
		for(int i=0;i<n;i++) {
			d[i] = i;
		}
		int ans = Integer.MAX_VALUE;
		
		while(true) {
			boolean ok = true;
			int s = 0;
			for(int i=0;i<n-1;i++) {
				if(a[ d[i] ][ d[i+1] ] == 0) {
					ok = false;
					break;
				}else {
					s+=a[ d[i] ][ d[i+1] ];
				}
			}
			if(ok && a[ d[n-1] ][ d[0] ] != 0) {
				s += a[ d[n-1] ][ d[0] ];
				ans = Math.min(ans, s);
			}
			if(!next_permutation(d)) {
				break;
			}
		}
		
		System.out.println(ans);
	}

	private static boolean next_permutation(int[] a) {
		int i = a.length-1;
		while(i>0 && a[i-1]>=a[i]) {
			i -= 1;
		}
		
		if(i <= 0) {
			return false;
		}
		
		int j = a.length-1;
		while(a[j] <= a[i-1]) {
			j-=1;
		}
		
		int temp = a[i-1];
		a[i-1] = a[j];
		a[j] = temp;
		
		j = a.length-1;
		while(i<j) {
			temp = a[i];
			a[i] = a[j];
			a[j] = temp;
			i += 1;
			j -= 1;
		}
		
		return true;
	}

}
