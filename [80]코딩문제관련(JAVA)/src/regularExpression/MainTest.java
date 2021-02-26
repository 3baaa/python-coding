package regularExpression;

import java.util.StringTokenizer;
import java.util.regex.*;

public class MainTest {

	public static void main(String[] args) {
		String str = "abcabdabe";
		String[] t = str.split("[ab]");
		StringTokenizer t2 = new StringTokenizer(str,"ab");
		for(String i : t) {
			System.out.print(i+'|');
		}
		System.out.println();
		while(t2.hasMoreTokens()){
			System.out.print(t2.nextToken()+"|");
		}
		
	}
	
	/*
	 * 추가로 정규표현식 공부
	 */

}
