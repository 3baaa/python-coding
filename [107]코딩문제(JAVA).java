package test;

import java.util.*;

/*
 * 숨바꼭질
 * 내가쓴 코드
 * 결과값이 나온다
 */
public class _107_코딩문제_JAVA {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		int[] r = new int[n+1];
		
		
		List<List<Integer>> z = new ArrayList<List<Integer>>();
		for(int i=0;i<n+1;i++) {
			z.add(new ArrayList<Integer>());
			r[i]=(int)1e9;
		}
		r[0]=0;
		r[1]=0;
		
		for(int i=0;i<m;i++) {
			int a=sc.nextInt();
			int b=sc.nextInt();
			z.get(a).add(b);
			z.get(b).add(a);
		}
		
		d(z,r);
		int r2=Arrays.stream(r).max().getAsInt();
		for(int i=1;i<n+1;i++) {
			if(r2==r[i]) {
				System.out.print(i+" ");
				break;
			}
		}
		System.out.print(r2+" ");
		System.out.println(Arrays.stream(r).filter(i->i==r2).count());
	}
	
	static void d(List<List<Integer>> z, int[] r) {
		PriorityQueue<VV> q = new PriorityQueue<VV>();
		q.offer(new VV(0,1));
		
		while(!q.isEmpty()) {
			VV v=q.poll();
			int d = v.getD();
			int c = v.getC();
			if(d>r[c]) {
				continue;
			}
			Iterator<Integer> t = z.get(c).stream().filter(i->d+1<r[i]).iterator();
			while(t.hasNext()) {
				int e=t.next();
				r[e]=d+1;
				q.offer(new VV(d+1,e));
			}
		}
	}

}
class VV implements Comparable<VV>{
	private int d;
	private int c;
	
	public VV(int d,int c) {
		this.d=d;
		this.c=c;
	}
	@Override
	public int compareTo(VV o) {
		return this.d-o.d;
	}
	public int getD() {
		return d;
	}
	public int getC() {
		return c;
	}
	
	
}
