package test;

import java.util.*;

/*
 * 모험가 길드
 * 내가쓴 코드
 * 결과값이 나온다
 */
public class _114_코딩문제_JAVA_모험가길드 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n=sc.nextInt();
		int[] a = new int[n];
		for(int i=0;i<n;i++) {
			a[i]=sc.nextInt();
		}
		
		Arrays.sort(a);
		int t=0;
		int r=0;
		for(int i : a) {
			t+=1;
			if(t==i) {
				r+=1;
				t=0;
			}
		}
		System.out.println(r);
	}

}
