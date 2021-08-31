package upload.new_upload;

import java.util.*;

/*
 * n과 m(3)
 * 내가쓴 코드
 * 결과 = 실패(시간초과,예제 출력은 나옵니다)
 */
public class Baekjoon_15651 {

	static int[] arr;
	static int n;
	static int m;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		m = sc.nextInt();
		arr = new int[m];
		test(0);
	}
	
	static void test(int c) {
		if(c==m) {
			for(int i:arr) {
				System.out.print(i+" ");
			}
			System.out.println();
			return;
		}
		
		for(int i=1;i<=n;i++) {
			arr[c]=i;
			test(c+1);
		}
	}

}
