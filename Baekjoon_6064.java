package upload.new_upload;

import java.util.*;

/*
 * 카잉 달력
 * 결과 = 실패(시간초과,예제 출력은 나옵니다)
 */
public class Baekjoon_6064 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		int[] arr = new int[t];
		for(int i=0;i<t;i++) {
			int m=sc.nextInt();
			int n=sc.nextInt();
			int x=sc.nextInt();
			int y=sc.nextInt();
			int n1=0,n2=0,c=0;
			while(n1!=m || n2!=n) {
				if(n1<m) {
					n1+=1;
				}else {
					n1=1;
				}
				if(n2<n) {
					n2+=1;
				}else {
					n2=1;
				}
				if(n2>n) {
					n2=1;
				}
				c++;
				if(n1==x && n2==y) {
					break;
				}
			}
			if(n1==x && n2==y) {
				arr[i]=c;
			}else {
				arr[i]=-1;
			}
		}
		for(int i : arr) {
			System.out.println(i);
		}
	}

}
