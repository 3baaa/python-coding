package test;

import java.util.Scanner;
//고정점 찾기
//내가쓴 코드
//(결과값이 나온다)
public class _84_코딩문제_JAVA {
	public static int z(int[] a,int s,int e) {
		if(s>e) {
			return -1;
		}
		int m=(s+e)/2;
		if(a[m]==m) {
			return m;
		}else if(a[m]>m) {
			return z(a,s,m-1);
		}else {
			return z(a,m+1,e);
		}
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] a = new int[n];
		sc.nextLine();
		String[] str = sc.nextLine().split("\\s");
		for(int i=0;i<n;i++) {
			a[i]=Integer.parseInt(str[i]);
		}
		
		System.out.println(z(a,0,n-1));
	}

}
