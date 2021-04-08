package test;

import java.util.*;

/*
 * 곱하기 혹은 더하기
 * 내가쓴코드
 * 결과값이 나온다
 */
public class _114_코딩문제_JAVA_곱하기혹은더하기 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String s = sc.nextLine();
		int r=0;
		for(int i=0;i<s.length();i++) {
			int t=s.charAt(i)-'0';
			if(t==0 || t==1 || r==0) {
				r+=t;
			}else {
				r*=t;
			}
		}
		System.out.println(r);
	}

}
