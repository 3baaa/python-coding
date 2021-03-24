package test;

import java.util.*;

/*
 * 편집 거리
 * 내가쓴 코드
 * 결과값이 나온다
 */
public class _103_코딩문제_JAVA {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String a=sc.nextLine();
		String b=sc.nextLine();
		
		if(a.length()<b.length()) {
			String t;
			t=a;
			a=b;
			b=t;
		}
		
		int r=0;
		int ib=0;
		for(int i=0;i<a.length();i++) {
			if(a.charAt(i)==b.charAt(ib)) {
				ib+=1;
			}else {
				if(b.length()>=a.length()-r) {
					ib+=1;
				}
				r+=1;
			}
		}
		System.out.println(r);
	}

}
