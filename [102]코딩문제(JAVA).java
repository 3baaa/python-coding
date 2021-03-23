package test;

import java.util.Scanner;

public class _102_코딩문제_JAVA {
	
	/*
	 * 못생긴 수
	 * 내가쓴 코드
	 * 결과값이 나온다
	 */
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		
		int z=1;
		int t=1;
		while(true) {
			z+=1;
			if(z%2==0 || z%3==0 || z%5==0) {
				t+=1;
			}
			if(t==n) {
				break;
			}
		}
		System.out.println(z);
	}

}
