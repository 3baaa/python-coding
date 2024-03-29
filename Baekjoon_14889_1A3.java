package upload.new_upload;

import java.util.*;

/*
 * 스타트와 링크
 * 답
 */
public class Baekjoon_14889_1A3 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[][] s = new int[n][n];
		for(int i=0; i<n; i++) {
			for(int j=0; j<n; j++) {
				s[i][j] = sc.nextInt();
			}
		}
		int ans = -1;
		for(int i=0; i<(1<<n); i++) {
			ArrayList<Integer> first = new ArrayList<>();
			ArrayList<Integer> second = new ArrayList<>();
			for(int j=0; j<n; j++) {
				if((i&(1<<j)) == 0 ) {
					first.add(j);
				}else {
					second.add(j);
				}
			}
			if(first.size() != n/2) {
				continue;
			}
			int t1 = 0;
			int t2 = 0;
			for(int l1=0; l1<n/2; l1++) {
				for(int l2=0; l2<n/2; l2++) {
					if(l1 == l2) {
						continue;
					}
					t1 += s[first.get(l1)][first.get(l2)];
					t2 += s[second.get(l1)][second.get(l2)];
				}
			}
			int diff = Math.abs(t1-t2);
			if(ans == -1 || ans > diff) {
				ans = diff;
			}
		}
		System.out.println(ans);
	}

}
