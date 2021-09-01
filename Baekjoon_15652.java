package upload.new_upload;

import java.util.*;

/*
 * n과 m(4)
 * 내가쓴 코드
 * 결과 = 맞았습니다!!
 */
public class Baekjoon_15652 {

	static int n;
	static int m;
	static int[] arr;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n=sc.nextInt();
		m=sc.nextInt();
		arr=new int[m];
		
		System.out.print(test(1,0));
	}
	
	static StringBuilder test(int a,int c) {
		if(c==m) {
			StringBuilder sb = new StringBuilder();
			for(int i=0;i<m;i++) {
				sb.append(arr[i]);
				if(i!=m-1) {
					sb.append(" ");
				}
			}
			sb.append("\n");
			return sb;
		}
		
		StringBuilder sb = new StringBuilder();
		for(int i=a;i<=n;i++) {
			arr[c]=i;
			sb.append(test(i,c+1));
		}
		
		return sb; 
	}

}
