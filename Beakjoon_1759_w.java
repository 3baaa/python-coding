package test;

import java.util.*;

/*
 * 암호 만들기
 * 내가쓴 코드
 */
public class Beakjoon_1759 {

	static String[] str;
	static String[] tt;
	static int l,c;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		l = sc.nextInt();
		c = sc.nextInt();
		sc.nextLine();
		StringTokenizer st = new StringTokenizer(sc.nextLine()," ");
		str = new String[c];
		tt = new String[l];
		for(int i=0;st.hasMoreTokens();i++) {
			str[i]=st.nextToken();
		}
		
		Arrays.sort(str);
		System.out.println(Arrays.toString(str));
		test(0,0);
		
	}

	public static StringBuilder test(int s,int t) {
		
		if(t==c) {
			for(String a : tt) {
				sb.append(a);
			}
			return sb;
		}
		StringBuilder sb = new StringBuilder();
		for(int i=s;i<l;i++) {
			if(c-i<l) {
				break;
			}
			tt[t]=str[i];
			sb.append(test(s+1,t+1));
			sb.append("\n");
		}
		
		return sb;
	}
}
