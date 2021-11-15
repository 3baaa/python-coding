package upload.new_upload;

import java.util.*;

/*
 * 맞춰봐
 * 다시 풀었다
 */
public class Backjoon_1248_R {

	public static int n;
	public static int[][] sign;
	public static int[] ans;
	
	public static boolean ok() {
		for(int i=0;i<n;i++) {
			int sum=0;
			for(int j=i;j<n;j++) {
				sum+=ans[j];
				if(sign[i][j]==0) {
					if(sum!=0) {
						return false;
					}
				}else if(sign[i][j]>0) {
					if(sum<=0) {
						return false;
					}
				}else if(sign[i][j]<0) {
					if(sum>=0) {
						return false;
					}
				}
			}
		}
		
		return true;
	}
	public static boolean go(int index) {
		if(index == n) {
			return ok();
		}
		
		for(int i=-10;i<=10;i++) {
			ans[index] = i;
			if( go(index+1) ) {
				return true;
			}
		}
		
		return false;
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		sign = new int[n][n];
		ans = new int[n];
		String s = sc.next();
		
		int cnt=0;
		for(int i=0;i<n;i++) {
			for(int j=i;j<n;j++) {
				char ch = s.charAt(cnt);
				if(ch == 0) {
					sign[i][j]=0;
				}else if(ch == '+') {
					sign[i][j]=1;
				}else if(ch == '-') {
					sign[i][j]=-1;
				}
				cnt++;
			}
		}
		
		go(0);
		
		for(int i=0;i<n;i++) {
			System.out.print(ans[i]+" ");
		}
	}

}
