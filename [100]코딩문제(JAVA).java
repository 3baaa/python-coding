package test;

import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;
import java.util.stream.Collector;
import java.util.stream.Stream;

//정수 삼각형과 퇴사
public class _100_코딩문제_JAVA {

	/*
	//문제 1 정수 삼각형
	//내가쓴 코드
	//결과값이 나온다
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[][] a = new int[n][];
		
		sc.nextLine();
		for(int i=0;i<n;i++) {
			String[] s = sc.nextLine().split("\\s");
			a[i]=Arrays.stream(s).mapToInt(Integer::parseInt).toArray();
		}
		
		int up=0,left_up=0;
		for(int i=1;i<n;i++) {
			for(int j=0;j<a[i].length;j++) {
				if(j-1<0) {
					left_up=0;
				}else {
					left_up=a[i-1][j-1];
				}
				
				if(a[i-1].length<=j) {
					up=0;
				}else {
					up=a[i-1][j];
				}
				
				a[i][j]=a[i][j]+Math.max(left_up, up);
			}
		}
		
		System.out.println(Arrays.stream(a[n-1]).max().getAsInt());
	}
	*/
	
	//문제 2 퇴사
	//내가쓴 코드
	//결과값이 나온다
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[][] a = new int[n][2];
		for(int i=0;i<n;i++) {
			a[i][0]=sc.nextInt();
			a[i][1]=sc.nextInt();
		}
		
		int[][] b = Arrays.stream(a).map(int[]::clone).toArray(int[][]::new);
		int r=0;
		for(int i=0;i<n;i++) {
			int t = i+a[i][0];
			if(t<n) {
				for(int j=t;j<n;j++) {
					if(j+a[j][0]>n) {
						continue;
					}
					b[j][1]=Math.max(b[j][1], b[i][1]+a[j][1]);
					r=Math.max(r, b[j][1]);
				}
			}
		}
		System.out.println(r);
	}
}
