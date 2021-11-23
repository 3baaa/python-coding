package upload.new_upload;

import java.util.*;

/*
 * 부분수열의 합
 * 답 작성후 다시 풀었다
 */
public class Baekjoon_1182_R {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int s = sc.nextInt();
		int[] a = new int[n];
		for(int i=0;i<n;i++) {
			a[i] = sc.nextInt();
		}
		
		int ans = 0;
		for(int i=1; i<(1<<n); i++) {
			int sum = 0;
			for(int k=0; k<n; k++) {
				if( ( i&(1<<k) ) !=0) {
					sum+=a[k];
				}
			}
			if(sum==s) {
				ans+=1;
			}
		}
		System.out.println(ans);
	}

}