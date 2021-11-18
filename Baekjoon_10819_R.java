package upload.new_upload;

import java.util.*;

/*
 * 차이를 최대로
 * 답 작성후 다시 풀었다
 */
public class Baekjoon_10819_R {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] a = new int[n];
		for(int i=0;i<n;i++) {
			a[i] = sc.nextInt();
		}
		Arrays.sort(a);
		int ans = 0;
		while(true) {
			int temp = calculate(a);
			ans = Math.max(ans, temp);
			if(!next_permutation(a)) {
				break;
			}
		}
		
		System.out.println(ans);
	}

	private static int calculate(int[] a) {
		int sum = 0;
		for(int i=1;i<a.length;i++) {
			sum+=Math.abs(a[i-1]-a[i]);
		}
		return sum;
	}

	private static boolean next_permutation(int[] a) {
		int i = a.length-1;
		while(i>0 && a[i-1]>=a[i]) {
			i-=1;
		}
		
		if(i<=0) {
			return false;
		}
		
		int j = a.length-1;
		while(a[i-1]>=a[j]) {
			j-=1;
		}
		
		int temp = a[i-1];
		a[i-1] = a[j];
		a[j] = temp;
		
		j = a.length-1;
		while(i<j) {
			temp = a[i];
			a[i] = a[j];
			a[j] = temp;
			i++;
			j--;
		}
		
		return true;
	}

}
