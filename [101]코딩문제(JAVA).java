package test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;
import java.util.stream.IntStream;

//병사 배치하기
//내가쓴코드
//결과값이 나온다
public class _101_코딩문제_JAVA {

	public static void main(String[] args) {
		Scanner sc =new Scanner(System.in);
		int n = sc.nextInt();
		int[] a = new int[n];
		for(int i=0;i<n;i++) {
			a[i]=sc.nextInt();
		}
		List<List<Integer>> z = new ArrayList<>();
		for(int i=0;i<n;i++) {
			z.add(new ArrayList<>());
		}
		z.get(0).add(a[0]);
		int j=0;
		for(int i=1;i<n;i++) {
			for(int k=0;k<z.get(j).size()-1;k++) {
				if(a[i]>z.get(j).get(k)) {
					j+=1;
					break;
				}
			}

			if(z.get(j).size()>0 && z.get(j).get(z.get(j).size()-1)<a[i]) {
				z.get(j).remove(z.get(j).size()-1);
			}
			z.get(j).add(a[i]);
		}
		int r=z.stream().mapToInt(i->i.size()).max().getAsInt();
		System.out.println(n-r);
	}
}
