package upload.new_upload;

import java.util.*;

/*
 * 퇴사
 * 내가쓴 코드
 * 
 */
public class Baekjoon_14501_w {

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
		
		System.out.println(test(0,0,0));
	}
	
	public static int test(int z,int c,int v) {
		if(z>=n || z+t[z]>n) {
			return v;
		}else {
			v=v+p[z];
		}
		
		int r = 0;
		for(int i=z;i<n;i++) {
			if(i+t[i]>n) {
				continue;
			}
			int s = test(i+t[i],c+1,v);
			r=Math.max(r, s);
		}
		return r;
	}
	
}