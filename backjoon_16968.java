package upload;

/*
 * 내가쓴 코드
 * 결과 = 맞았습니다
 */
import java.util.Scanner;

public class backjoon_16968 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String str=sc.nextLine();
		System.out.println(test(str));
		
	}

	public static int test(String str) {
		int result=1;
		char ch = 0;
		char sch;
		int d=10;
		int c=26;
		
		for(int i=0;i<str.length();i++) {
			sch = str.charAt(i);
			if(sch=='c') {
				if(sch==ch && c==26) {
					c-=1;
				}
				d=10;
				result*=c;
			}else {
				if(sch==ch && d==10) {
					d-=1;
				}
				c=26;
				result*=d;
			}
			ch=sch;
		}
		
		return result;
	}
}
