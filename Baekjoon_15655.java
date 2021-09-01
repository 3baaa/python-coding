package upload.new_upload;

import java.util.*;

/*
 * n과 m(6)
 * 내가쓴 코드
 * 결과 = 맞았습니다!!
 */
public class Baekjoon_15655 {

	static int n;
	static int m;
	static int[] arr;
	static int[] arr2;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n=sc.nextInt();
		m=sc.nextInt();
		arr = new int[n];
		arr2 = new int[m];
		sc.nextLine();
		StringTokenizer st = new StringTokenizer(sc.nextLine()," ");
		for(int i=0;st.hasMoreTokens();i++) {
			arr[i]=Integer.parseInt(st.nextToken());
		}
		
		Arrays.sort(arr);
		
		System.out.print(test(0,0));
	}

	static StringBuilder test(int a,int c) {
		if(c==m) {
			StringBuilder sb = new StringBuilder();
			for(int i=0;i<m;i++) {
				sb.append(arr2[i]);
				if(i!=m-1) {
					sb.append(" ");
				}
			}
			sb.append("\n");
			return sb;
		}
		
		StringBuilder sb = new StringBuilder();
		for(int i=a;i<n;i++) {
			arr2[c]=arr[i];
			sb.append(test(i+1,c+1));
		}
		return sb;
	}
}
