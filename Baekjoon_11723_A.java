package upload.new_upload;

import java.io.*;
import java.util.*;

/*
 * 집합
 * 답
 */
public class Baekjoon_11723_A {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		int n = 20;
		int m = Integer.valueOf(bf.readLine());
		int s = 0;
		StringBuilder sb = new StringBuilder();
		while(m-- > 0) {
			String[] line = bf.readLine().split(" ");
			if(line[0].equals("add")) {
				int x = Integer.valueOf(line[1]) - 1;
				s = (s | (1 << x));
			}else if(line[0].equals("remove")) {
				int x = Integer.valueOf(line[1]) - 1;
				s = (s & ~(1<<x));
			}else if(line[0].equals("check")) {
				int x = Integer.valueOf(line[1]) - 1;
				int res = (s & (1 << x));
				if(res == 0) {
					sb.append("0\n");
				}else {
					sb.append("1\n");
				}
			}else if(line[0].equals("toggle")) {
				int x = Integer.valueOf(line[1]) - 1;
				s = (s ^ (1 << x));
			}else if(line[0].equals("all")) {
				s = (1 << n) - 1;
			}else if(line[0].equals("empty")) {
				s = 0;
			}
		}
		System.out.println(sb);
	}

}
