package upload.new_upload;

/*
 * 배열 돌리기 3
 * 내가쓴 코드
 */
import java.util.*;
import java.util.function.Function;
import java.util.stream.*;

public class Baekjoon_16935_w2 {

	static int n,m;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n=sc.nextInt();
		m=sc.nextInt();
		int r=sc.nextInt();
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
			arr=check_oper(i,arr);
		}
		System.out.println();
		arr_p(arr);
	}
	
	public static void arr_p(int[][] arr) {
		for(int[] n1 : arr) {
			for(int n2 : n1) {
				System.out.print(n2+" ");
			}
			System.out.println();
		}
	}
	
	public static int[][] check_oper(int i,int[][] arr) {
		
		switch(i) {
		case 1 : arr=oper_1(arr); break;
		case 2 : arr=oper_2(arr); break;
		case 3 : arr=oper_3(arr); break;
		//case 4 : arr=oper_4(arr); break;
		//case 5 : arr=oper_5(arr); break;
		//case 6 : arr=oper_6(arr); break;
		}
		return arr;
	}
	
	public static int[][] oper_1(int[][] arr) {
		for(int s=0,e=n-1;s<e;s++,e--) {
			int[] t = arr[s];
			arr[s] = arr[e];
			arr[e] = t;
		}
		return arr;
	}
	public static int[][] oper_2(int[][] arr) {
		for(int s=0,e=m-1;s<e;s++,e--) {
			for(int i=0;i<n;i++) {
				int t = arr[i][s];
				arr[i][s] = arr[i][e];
				arr[i][e] = t;
			}
		}
		return arr;
	}
	public static int[][] oper_3(int[][] arr) {
		int[][] new_arr = new int[m][n];
		for(int i=0;i<m;i++) {
			int[] tarr = new int[n];
			for(int j=0;j<n;j++) {
				tarr[n-j-1] = arr[j][i];
			}
			new_arr[i] = tarr;
		}
		
		return new_arr;
	}
	public static void oper_4(int[][] arr) {
		
	}
	public static void oper_5(int[][] arr) {
		
	}
	public static void oper_6(int[][] arr) {
		
	}
}
