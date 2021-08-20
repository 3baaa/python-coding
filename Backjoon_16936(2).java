package test;

import java.util.*;
/*
 * 나3곱2
 * 내가쓴 코드
 * 결과 = 틀렸습니다(예제 출력은 나옵니다)
 */
public class Backjoon_16936 {

	public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
		int x = sc.nextInt();
		sc.nextLine();
        String s = sc.nextLine();
		StringTokenizer st = new StringTokenizer(s," ");
		List<Long> list = new ArrayList<Long>();
		List<Long> answer = new LinkedList<Long>();
       
        while(st.hasMoreTokens()) {
            list.add(Long.parseLong(st.nextToken()));
		}
        
		long t3=0,t2=0;
		for(long n : list) {
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
			
			if(t2==0 && t3==0) {
				answer.add(n);
				continue;
			}
			
			int idx=0;
			if(t2!=0) {
				if(answer.contains(t2)) {
					idx = answer.indexOf(t2);
				}
			}else if(t3!=0) {
				if(answer.contains(t3)) {
					idx = answer.indexOf(t3);
				}
			}
			answer.add(idx, n);
		}
		
		for(long n2 : answer) {
			System.out.print(n2+" ");
		}
}
