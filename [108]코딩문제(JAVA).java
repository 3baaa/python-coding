package test;

import java.util.*;

/*
 * 여행 계획
 * 내가쓴 코드
 * 결과값이 나온다
 */
public class _108_코딩문제_JAVA {

	static int[] p;
	static int n;
	public static void main(String[] args) {
		Scanner sc =new Scanner(System.in);
		n = sc.nextInt();
		int m = sc.nextInt();
		p = new int[n];
		for(int i=0;i<n;i++) {
			p[i]=i;
		}
		
		for(int i=0;i<n;i++) {
			for(int j=0;j<n;j++) {
				int t=sc.nextInt();
				if(t==1) {
					union_parent(i,j);
				}
			}
		}
		
		List<Integer> r = new ArrayList<Integer>();
		for(int i=0;i<m;i++) {
			r.add(sc.nextInt());
		}
		int a=p[r.get(0)-1];
		String rr = "YES";
		for(int i=1;i<r.size();i++) {
			if(a!=p[r.get(i)-1]) {
				rr="NO";
			}
		}
		System.out.println(rr);
		
	}
	
	public static int find_parent(int n) {
		if(p[n]==n) {
			return n;
		}
		p[n]=find_parent(p[n]);
		return p[n];
	}
	
	public static void union_parent(int a,int b) {
		a=find_parent(a);
		b=find_parent(b);
		if(a>b) {
			p[a]=b;
		}else {
			p[b]=a;
		}
	}
}
