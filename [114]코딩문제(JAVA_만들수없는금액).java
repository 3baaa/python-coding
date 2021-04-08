package test;

import java.util.*;

/*
 * 만들 수 없는 금액
 * 내가쓴 코드
 * 결과값이 나온다
 */
public class _114_코딩문제_JAVA_만들수없는금액 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n=sc.nextInt();
		int[] a=new int[n];
		for(int i=0;i<n;i++) {
			a[i]=sc.nextInt();
		}
		Arrays.sort(a);
		
		int t=a[0];
		int r=0;
		if(t>1) {
			r=1;
		}else {
			for(int i=1;i<n;i++) {
				if(a[i]>t+1) {
					r=t+1;
					break;
				}
				t+=i;
			}
		}
		System.out.println(r);
	}

}
