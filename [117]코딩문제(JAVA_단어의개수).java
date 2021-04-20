package test;

/*
 * 단어의 개수
 * 내가쓴 코드
 * 결과 = 맞았습니다!!
 */
import java.util.*;

public class _117_코딩문제_JAVA_단어의개수 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		StringTokenizer s = new StringTokenizer(sc.nextLine()," ");
		System.out.println(s.countTokens());
	}

}
