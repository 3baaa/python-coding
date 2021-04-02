package test;

import java.util.*;

/*
 * 어두운 길
 * 내가쓴 코드
 * 결과값이 나온다
 */
public class _110_코딩문제_JAVA_어두운길 {
	
	static int[] p;
	public static void main(String[] args) {
		Scanner sc =new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		p=new int[n];
		List<B> a = new ArrayList<B>();
		int s=0,r=0;
		
		Arrays.setAll(p, i->i);
		for(int i=0;i<m;i++) {
			int x=sc.nextInt();
			int y=sc.nextInt();
			int z=sc.nextInt();
			a.add(new B(x,y,z));
			s+=z;
		}
		
		Collections.sort(a);
		for(B b : a) {
			if(find_p(b.getX())!=find_p(b.getY())) {
				union_p(b.getX(), b.getY());
				r+=b.getZ();
			}
		}
		System.out.println(s-r);
	}
	
	public static int find_p(int n) {
		if(p[n]!=n) {
			return p[n]=find_p(p[n]);
		}
		return p[n];
	}
	
	public static void union_p(int a,int b) {
		a=find_p(a);
		b=find_p(b);
		if(a<b) {
			p[b]=a;
		}else {
			p[a]=b;
		}
	}
}

class B implements Comparable<B>{
	int x,y,z;
	public B(int x,int y,int z) {
		this.x=x;
		this.y=y;
		this.z=z;
	}
	
	
	
	public int getX() {
		return x;
	}



	public int getY() {
		return y;
	}



	public int getZ() {
		return z;
	}



	@Override
	public int compareTo(B o) {
		return this.z-o.z;
	}
}