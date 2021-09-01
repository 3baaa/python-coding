package upload.new_upload;

import java.util.*;

/*
 * n과 m(5)
 * 내가쓴 코드
 * 결과 = 맞았습니다!!
 */
public class Baekjoon_15654 {

	static int n;
	static int m;
	static int[] arr;
	static int[] arr2;
	static boolean[] check;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		m = sc.nextInt();
		arr = new int[n];
		arr2 = new int[n];
		check = new boolean[n];
		List<Integer> arr2 = new ArrayList();
		sc.nextLine();
		StringTokenizer st = new StringTokenizer(sc.nextLine()," ");
		
		for(int i=0;st.hasMoreTokens();i++){
			arr[i] = Integer.parseInt(st.nextToken());
		}
		Arrays.sort(arr);
		System.out.println(test(0));
	}
	
	static StringBuilder test(int c) {
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
		for(int i=0;i<n;i++) {
			if(check[i]) {
				continue;
			}
			arr2[c]=arr[i];
			check[i]=true;
			sb.append(test(c+1));
			check[i]=false;
		}
		
		return sb;
	}

}
