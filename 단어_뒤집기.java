package test;

/*
 * 단어 뒤집기
 * 내가쓴 코드
 * 결과 = 맞았습니다!!
 */
import java.util.*;

public class 단어_뒤집기 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		StringBuffer sb;
		int tc = sc.nextInt();
		sc.nextLine();
		for(int i=0;i<tc;i++) {
			String sr="";
			StringTokenizer st = new StringTokenizer(sc.nextLine());
			while(st.hasMoreTokens()) {
				sb=new StringBuffer(st.nextToken());
				sr+=sb.reverse()+" ";
			}
			System.out.println(sr.trim());
		}
	}
}
