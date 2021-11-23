package upload.new_upload;

import java.io.*;
import java.util.*;

/*
 * 집합
 * 답 작성후 다시 풀었다
 */
public class Baekjoon_11723_R {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		int n = 20;
		int m = Integer.valueOf(bf.readLine());
		int s = 0;
		StringBuilder sb = new StringBuilder();
		while(m-- > 0) {
			String[] a = bf.readLine().split(" "); 
			if(a[0].equals("add")) {
				int x = Integer.parseInt(a[1]);
				s = s | ( 1 << (x-1) );
			}else if(a[0].equals("remove")) {
				int x = Integer.parseInt(a[1]);
				s = s & ~( 1 << (x-1) );
			}else if(a[0].equals("check")) {
				int x = Integer.parseInt(a[1]);
				int r = s & ( 1 << (x-1) );
				if(r==0) {
					sb.append("0\n");
				}else {
					sb.append("1\n");
				}
			}else if(a[0].equals("toggle")) {
				int x = Integer.parseInt(a[1]);
				s = s ^ ( 1 << (x-1) );
			}else if(a[0].equals("all")) {
				s = (1 << n) - 1;
			}else if(a[0].equals("empty")) {
				s = 0;
			}
		}
		System.out.println(sb);
	}

}
