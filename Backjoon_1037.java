package upload.new_upload;

import java.util.*;

/*
 * 약수
 * 내가쓴 코드
 * 결과 = 맞았습니다!!
 */
public class Backjoon_1037 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int c = sc.nextInt();
		sc.nextLine();
		StringTokenizer st = new StringTokenizer(sc.nextLine()," ");
		int[] arr = new int[c];
		
		for(int i=0;st.hasMoreTokens();i++) {
			arr[i] = Integer.valueOf(st.nextToken());
		}
		
		Arrays.sort(arr);
		
		System.out.println(arr[0]*arr[c-1]);
	}

}
