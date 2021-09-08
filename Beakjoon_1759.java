package upload.new_upload;

import java.util.*;

/*
 * 암호 만들기
 * 내가쓴 코드
 * 결과 = 맞았습니다!!
 */
public class Beakjoon_1759 {

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
		test(0,0);
		
	}

	public static void test(int z,int n) {
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
				sb.append(s);
			}
			if(count>=1 && count2>=2) {
				System.out.println(sb.toString());
			}
			return;
		}
		for(int i=n;i<c;i++) {
			ans_str[z]=str[i];
			test(z+1,i+1);
		}
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
