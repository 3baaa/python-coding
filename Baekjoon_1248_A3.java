package upload.new_upload;

import java.util.*;

/*
 * 맞춰봐
 * 답3
*/
public class Baekjoon_1248_A3 {

	static int n;
	static int[][] sign;
	static int[] ans;
	
	static boolean check(int index) {
		int sum = 0;
		for(int i=index ; i>=0 ; i--) {
			sum += ans[i];
			if(sign[i][index] == 0) {
				if(sum !=0) {
					return false;
				}
			}else if(sign[i][index] < 0) {
				if(sum >= 0) {
					return false;
				}
			}else if(sign[i][index] > 0) {
				if(sum <= 0) {
					return false;
				}
			}
		}
		return true;
	}
	
	/*
	static boolean ok() {
		for(int i=0 ; i<n ; i++) {
			int sum = 0;
			for(int j=i ; j<n ; j++) {
				sum += ans[j];
				if(sign[i][j] == 0) {
					if(sum != 0 ) {
						return false;
					}
				}else if(sign[i][j] > 0) {
					if(sum <= 0) {
						return false;
					}
				}else if(sign[i][j] < 0) {
					if(sum >= 0) {
						return false;
					}
				}
			}
		}
		return true;
	}
	*/
	
	static boolean go(int index) {
		if(index == n) {
			return true;
		}
		if(sign[index][index] == 0) {
			ans[index] = 0;
			return check(index) && go(index+1);
			//return go(index+1);
		}
		for(int i=1;i<=10;i++) {
			ans[index] = sign[index][index]*i;
			if(check(index) && go(index+1)) {
				return true;
			}
			/*
			if(go(index+1)) {
				return true;
			}
			*/
		}
		/*
		for(int i=-10 ; i<=10 ; i++) {
			ans[index] = i;
			if( go(index+1) ) {
				return true;
			}
		}
		*/
		return false;
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		ans = new int[n];
		sign = new int[n][n];
		String s = sc.next();
		
		int cnt = 0;
		for(int i=0 ; i<n ; i++) {
			for(int j=i ; j<n ; j++) {
				char x = s.charAt(cnt);
				if(x=='0') {
					sign[i][j] = 0;
				}else if(x=='+') {
					sign[i][j]=1;
				}else {
					sign[i][j]=-1;
				}
				cnt += 1;
			}
		}
		
		go(0);
		
		for(int i=0;i<n;i++) {
			System.out.print(ans[i]+" ");
		}
		System.out.println();
	}

}
