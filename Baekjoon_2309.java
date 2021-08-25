package upload.new_upload;

/*
 * 일곱 난쟁이
 * 내가쓴 코드
 * 결과 = 맞았습니다!!
 */

import java.util.*;

public class Baekjoon_2309 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[] arr = new int[9];
		int[] answer = new int[7];
		for(int i=0;i<9;i++) {
			arr[i]=sc.nextInt();
		}
		check(arr,0,0,answer);
		Arrays.sort(answer);
		for(int n : answer) {
			System.out.println(n);
		}
	}

	public static int check(int[] arr,int a,int c,int[] answer) {
		if(c==7) {
			if(sum(answer)==100) {
				return 1;
			}
			return 0;
		}
		
		for(int i=a;i<9;i++) {
			answer[c]=arr[i];
			int r = check(arr,i+1,c+1,answer);		
			if(r==1) {
				return 1;
			}
		}
		return 0;
	}
	
	public static int sum(int[] answer) {
		int sum=0;
		for(int n : answer) {
			sum+=n;
		}
		return sum;
	}
}
