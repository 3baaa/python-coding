package upload.new_upload;

import java.util.*;

/*
 * 수 이어 쓰기 1
 * 내가쓴 코드
 * 결과 = 맞았습니다!!
 */
public class Baekjoon_1748 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int r=0;
		int i=1,j=1;
		while(n>=(i*10)) {
			r+=j*(i*10-i);
			i*=10;
			j+=1;
		}
		r+=j*(n-i+1);
		System.out.println(r);
	}

}
