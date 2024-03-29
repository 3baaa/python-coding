package upload.new_upload;

import java.util.*;

/*
 * 다음 순열
 * 다시 풀었다
 */

public class Baekjoon_10972_R {
	public static boolean next_permutation(int[] a) {
		int i = a.length-1;
		while(i>0 && a[i-1] >= a[i]) {
			i-=1;
		}
		
		if(i<=0) {
			return false;
		}

		int j = a.length-1;
		while(a[i-1]>=a[j]) {
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
			i++;
			j--;
		}
		
		return true;
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] a = new int[n];
		for(int i=0;i<n;i++) {
			a[i] = sc.nextInt();
		}
		if(next_permutation(a)) {
			for(int i=0;i<n;i++) {
				System.out.print(a[i]+" ");
			}
			System.out.println();
		}else {
			System.out.println("-1");
		}
	}

}
