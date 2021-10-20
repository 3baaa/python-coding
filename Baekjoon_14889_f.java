package test;

import java.util.*;

/*
 * 스타트와 링크
 * 내가쓴 코드
 * 결과 = 예제값은 나오나 시간초과로 실패
 */

public class Baekjoon_14889_f {

	public static int n;
	public static int[][] arr;
	public static void main(String[] args) {
		int a=201;
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		arr = new int[n][n];
		sc.nextLine();
		
		for(int i=0;i<n;i++) {
			String[] str = sc.nextLine().split("\\s");
			for(int j=0;j<n;j++) {
				arr[i][j]=Integer.valueOf(str[j]);
			}
		}
		
		
		List<List<Integer>> list = new ArrayList<List<Integer>>();
		Stack<Integer> st = new Stack<Integer>();
		t(0,list,st,0);
		
		for(int i=0 ; i<list.size() ; i++) {
			List<Integer> l = list.get(i);
			for(int j=i+1 ; j<list.size() ; j++) {
				List<Integer> l2 = list.get(j);
		
				if(check(l,l2)) {
					continue;
				}
				int t1 = check2(l);
				int t2 = check2(l2);
				a=Math.min(a, Math.abs(t1-t2));
			}
		}
		System.out.println(a);
	}

	public static int check2(List<Integer> l) {
		int a=0;
		for(int i=0;i<n/2;i++) {
			for(int j=i+1;j<n/2;j++) {
				a+=arr[l.get(i)][l.get(j)]+arr[l.get(j)][l.get(i)];
			}
		}
		return a;
	}
	public static boolean check(List<Integer> l,List<Integer> l2) {
		for(int i=0;i<n/2;i++) {
			Integer t1 = l.get(i);
			if(l2.contains(t1)) {
				return true;
			}
		}
		return false;
	}
	
	public static void t(int s,List<List<Integer>> list,Stack<Integer> st,int c) {
		if(c==n/2) {
			list.add( new ArrayList<Integer>(st) );
			return;
		}
		for(int i=s;i<n;i++) {
			st.push(i);
			t(i+1,list,st,c+1);
			st.pop();
		}
		return;
	}
}
