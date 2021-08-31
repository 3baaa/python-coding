package upload.new_upload;

import java.util.*;

/*
 * n과 m(2)
 * 내가쓴 코드
 * 결과 = 맞았습니다!!
 */
public class Baekjoon_15650 {
	static int[] arr;
	static int n,m;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n=sc.nextInt();
		m=sc.nextInt();
		arr = new int[m];
		
		test(1,0);
	}
	
	static void test(int a,int c) {
		if(c==m) {
			for(int i:arr) {
				System.out.print(i+" ");
			}
			System.out.println();
			return;
		}
		for(int i=a;i<=n;i++) {
			arr[c]=i;
			test(i+1,c+1);
		}
	}
}
