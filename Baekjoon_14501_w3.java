package upload.new_upload;

import java.util.*;

/*
 * 퇴사
 * 내가쓴 코드
 * 결과 = 맞았습니다!!
 */
public class Baekjoon_14501_w3 {

	static int n;
	static int[] t,p;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		n = sc.nextInt();
		t = new int[n];
		p = new int[n];
		
		for(int i=0;i<n;i++) {
			t[i]=sc.nextInt();
			p[i]=sc.nextInt();
		}
		
		System.out.println(test(0,0));
	}
	
	public static int test(int s,int v) {		
		if(s>=n) {
			return v;
		}
		
		int r=v;
		for(int i=s;i<n;i++) {
			if(i+t[i]>n) {
				continue;
			}
			int a = test(i+t[i],v+p[i]);
			r=Math.max(r, a);
		}
		return r;
	}
}