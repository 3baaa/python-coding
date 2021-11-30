package test;

import java.util.*;

/*
 * 1로 만들기
 * 답2 작성후 다시 풀었다 (바텀 업)
 */
public class Baekjoon_1463_R2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] d = new int[n+1];
		d[1] = 0;
		for(int i=2; i<=n; i++) {
			d[i] = d[i-1] + 1;
			if(i%2 == 0 && d[i] > d[i/2] + 1) {
				d[i] = d[i/2] + 1;
			}
			if(i%3 == 0 && d[i] > d[i/3] + 1) {
				d[i] = d[i/3] + 1;
			}
		}
		System.out.println(d[n]);
	}

}
