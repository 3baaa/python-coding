package test;

import java.util.*;

/*
 * DFS와 BFS
 * 내가쓴 코드
 * 결과 = 맞았습니다!!
 */
public class _117_코딩문제_JAVA_DFS와BFS {
	static int n;
	static boolean[] v1;
	static boolean[] v2;
	static List<Integer> r1;
	static List<Integer> r2;
	static List<List<Integer>> a;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		int m = sc.nextInt();
		int v = sc.nextInt();
		
		a = new ArrayList<List<Integer>>();
		for(int i=0;i<n+1;i++) {
			a.add(new ArrayList<Integer>());
		}
		
		v1 = new boolean[n+1];
		v2 = new boolean[n+1];
		
		r1 = new ArrayList<Integer>();
		r2 = new ArrayList<Integer>();
		
		for(int i=0;i<m;i++) {
			int n1=sc.nextInt();
			int n2=sc.nextInt();
			a.get(n1).add(n2);
			a.get(n2).add(n1);
		}
		
		for(int i=0;i<n+1;i++) {
			Collections.sort(a.get(i));
		}
		
		dfs(v);
		bfs(v);
		
		for(int i : r1) {
			System.out.print(i+" ");
		}
		System.out.println();
		for(int i : r2) {
			System.out.print(i+" ");
		}
	}

	public static void dfs(int v) {
		if(v1[v]) {
			return;
		}
		v1[v]=true;
		r1.add(v);
		for(int i : a.get(v)) {
			dfs(i);
		}
	}
	
	public static void bfs(int v) {
		Queue<Integer> q = new LinkedList<Integer>();
		q.offer(v);
		v2[v]=true;
		while(!q.isEmpty()) {
			int n1=q.poll();
			r2.add(n1);
			for(int i : a.get(n1)) {
				if(!v2[i]) {
					q.offer(i);
					v2[i]=true;
				}
			}
		}
	}
}
