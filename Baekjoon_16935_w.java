package upload.new_upload;

/*
 * 배열 돌리기 3
 * 작성중
 */
import java.util.*;

public class Baekjoon_16935_w {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n=sc.nextInt(),m=sc.nextInt(),r=sc.nextInt();
		int[][] arr = new int[n][m];
		int[] oper = new int[r];
		sc.nextLine();
		for(int i=0;i<n;i++) {
			StringTokenizer st = new StringTokenizer(sc.nextLine()," ");
			for(int j=0;st.hasMoreTokens();j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		StringTokenizer st = new StringTokenizer(sc.nextLine()," ");
		for(int i=0;st.hasMoreTokens();i++) {
			oper[i] = Integer.parseInt(st.nextToken());
		}
		
		arr_p(arr);
		for(int i : oper) {
			check_oper(i,arr);
		}
	}
	
	public static void arr_p(int[][] arr) {
		for(int[] n1 : arr) {
			for(int n2 : n1) {
				System.out.print(n2+" ");
			}
			System.out.println();
		}
	}
	
	public static void check_oper(int i,int[][] arr) {
		switch(i) {
		case 1 : oper_1(arr); break;
		case 2 : oper_2(arr); break;
		case 3 : oper_3(arr); break;
		case 4 : oper_4(arr); break;
		case 5 : oper_5(arr); break;
		case 6 : oper_6(arr); break;
		}
	}
	
	public static void oper_1(int[][] arr) {
		
	}
	public static void oper_2(int[][] arr) {
		
	}
	public static void oper_3(int[][] arr) {
		
	}
	public static void oper_4(int[][] arr) {
		
	}
	public static void oper_5(int[][] arr) {
		
	}
	public static void oper_6(int[][] arr) {
		
	}
}
