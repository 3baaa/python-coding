package upload.new_upload;

import java.util.*;

/*
 * 암호 만들기
 * 내가쓴 코드
 * 결과 = 맞았습니다!!
 */
public class Beakjoon_1759_2 {

	static String[] str;
	static String[] ans_str;
	static int l,c;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		l = sc.nextInt();
		c = sc.nextInt();
		sc.nextLine();
		StringTokenizer st = new StringTokenizer(sc.nextLine()," ");
		str = new String[c];
		ans_str = new String[l];
		for(int i=0;st.hasMoreTokens();i++) {
			str[i]=st.nextToken();
		}
		
		Arrays.sort(str);
		System.out.println(test(0,0));
		
	}

	public static StringBuilder test(int z,int n) {
		if(z==l) {
			StringBuilder sb = new StringBuilder();
			int count=0;
			int count2=0;
			for(String s : ans_str) {
				if(check(s)) {
					count++;
				}else {
					count2++;
				}
			}
			
			if(count>=1 && count2>=2) {
				sb.append(String.join("", ans_str));
				sb.append("\n");
			}
			return sb;
		}
		
		StringBuilder sb = new StringBuilder();
		for(int i=n;i<c;i++) {
			ans_str[z]=str[i];
			sb.append(test(z+1,i+1));
		}
		
		return sb;
	}
	
	public static boolean check(String s) {
		String[] m = {"a","e","i","o","u"};
		for(String mm : m) {
			if(mm.equals(s)) {
				return true;
			}
		}
		return false;
	}
}
