package upload.new_upload;

import java.util.*;

/*
 * 모든 순열
 * 답
 */
public class Baekjoon_10974_A {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] a = new int[n];
		for(int i=0;i<n;i++) {
			a[i] = i+1;
		}
		while(true) {	
			for(int i=0;i<n;i++) {
				System.out.print(a[i]+" ");
			}
			System.out.println();
			if(!next_permutation(a)) {
				break;
			}
		}
	}

	private static boolean next_permutation(int[] a) {
		int i = a.length-1;
		while(i>0 && a[i-1]>=a[i]) {
			i-=1;
		}
		
		if(i<=0) {
			return false;
		}
		
		int j = a.length-1;
		while(a[j]<=a[i-1]) {
			j -= 1;
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
