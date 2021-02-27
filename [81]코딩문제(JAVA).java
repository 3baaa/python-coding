package test;

import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class _81_코딩문제_JAVA_ {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		sc.nextLine();
		String[] a = sc.nextLine().split("\\s");
		Arrays.sort(a);
		System.out.println(a[(a.length-1)/2]);
	}

}
