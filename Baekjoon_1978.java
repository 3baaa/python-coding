package test;

import java.util.*;

/*
 * 소수 찾기
 * 내가쓴 코드
 * 결과 = 맞았습니다!!
 */
public class baekjoon_1978 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		sc.nextLine();
		StringTokenizer st = new StringTokenizer(sc.nextLine()," ");
		int c = 0;
		while(st.hasMoreTokens()) {
			int t = Integer.valueOf(st.nextToken());
			if(t!=1) {
				c++;
			}else {
				continue;
			}
			for(int i=2;i*i<=t;i++) {
				if(t%i==0) {
					c--;
					break;
				}
			}
		}
		System.out.println(c);
	}

}
