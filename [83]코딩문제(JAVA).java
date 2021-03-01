package test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Stack;
import java.util.Scanner;

//카드 정렬하기
//내가쓴 코드
//(결과값이 나온다)
public class _83_코딩문제_JAVA {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		
		int[] a = new int[n];
		Stack<Integer> s = new Stack<Integer>();
		
		for(int i=0;i<n;i++) {
			a[i]=sc.nextInt();
		}
		
		int r=0;
		for(int t : a) {
			s.push(t);
			if(s.size()==2) {
				s.push(s.pop()+s.pop());
				r+=s.peek();
			}
		}
		System.out.println(r);
	}

}
