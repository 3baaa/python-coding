package test;

import java.util.Arrays;
import java.util.Scanner;

//정렬된 배열에서 특정 수의 개수 구하기
//내가쓴 코드
//(결과값이 나온다)

public class _83_코딩문제2_JAVA {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String[] str1=sc.nextLine().split("\\s");
		String[] str2=sc.nextLine().split("\\s");
		int n=Integer.parseInt(str1[0]);
		int x=Integer.parseInt(str1[1]);
		int[] a = new int[n];
		for(int i=0;i<a.length;i++) {
			a[i]=Integer.parseInt(str2[i]);
		}
		int r1 = left(a,0,a.length,x,a.length);
		int r2 = right(a,0,a.length,x,a.length);
		if(r1!=-1) {
			System.out.println(r2-r1+1);
		}else {
			System.out.println(r1);
		}
	}
	
	public static int left(int[] a,int s,int e,int x,int l) {
		if(s>e || s==l) {
			return -1;
		}
		int m=(s+e)/2;
		if((s==e || s==l-1) && a[m]==x) {
			return m;
		}
		if(s==l-1 && a[m]!=x) {
			return -1;
		}
		
		if(a[m]>=x) {
			return left(a,s,m,x,l);
		}else {
			return left(a,m+1,e,x,l);
		}
	}
	
	public static int right(int[] a,int s,int e,int x,int l) {
		if(s>e || s==l) {
			return -1;
		}
		int m=(s+e)/2;
		if((s==e || s==l-1)&& a[m]==x) {
			return m;
		}
		if(s==l-1 && a[m]!=x) {
			return -1;
		}
		
		if(a[m]>x) {
			return right(a,s,m-1,x,l);
		}else{
			return right(a,m,e,x,l);
		}
	}
}
