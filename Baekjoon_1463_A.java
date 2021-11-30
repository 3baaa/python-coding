package upload.new_upload;

import java.util.*;

/*
 * 1로 만들기
 * 답
 */
public class Baekjoon_1463_A {
	public static int[] d;
	public static int go(int n) {
		if(n==1) {
			return 0;
		}
		if(d[n] > 0) {
			return d[n];
		}
		d[n] = go(n-1) + 1;
		if(n%2 == 0) {
			int temp = go(n/2)+1;
			if(d[n] > temp) {
				d[n] = temp;
			}
		}
		if(n%3 == 0) {
			int temp = go(n/3)+1;
			if(d[n] > temp) {
				d[n] = temp;
			}
		}
		return d[n];
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		d = new int[n+1];
		System.out.println(go(n));
	}

}
