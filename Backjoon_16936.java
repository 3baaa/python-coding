package upload;

import java.util.*;
/*
 * 나3곱2
 * 내가쓴 코드(작성중)
 */
public class Backjoon_16936 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int x = sc.nextInt();
		sc.nextLine();
		StringTokenizer st = new StringTokenizer(sc.nextLine()," ");
		List<Integer> list = new ArrayList<Integer>();
		List<Integer> answer = new ArrayList<Integer>();
		int c=0;
		while(st.hasMoreTokens()) {
			list.add(Integer.valueOf(st.nextToken()));
			c++;
		}
		
		int t3=0,t2=0;
		for(int n : list) {
			if(n%3==0 && list.contains(n/3)) {
				t3=n/3;
			}else {
				t3=0;
			}
			if(list.contains(n*2)) {
				t2=n*2;
			}else {
				t2=0;
			}
			
			if(t3!=0 || t2!=0) {
				int idx;
				if((idx = answer.indexOf(t3))!=-1) {
					answer.add(idx, t3);
				}else if((idx = answer.indexOf(t2))!=-1) {
					answer.add(idx,t2);
				}else {
					answer.add(t3);
				}
			}else {
				answer.add(n);
			}
		}
		
		System.out.println(answer);
	}
}
