package upload.new_upload;

import java.util.*;

/*
 * 스타트와 링크
 * 답 작성후 다시 풀었다
 */
public class Baekjoon_14889_1R3 {

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
			List<Integer> first = new ArrayList<>();
			List<Integer> second = new ArrayList<>();
			
			for(int j=0; j<n; j++) {
				if( (i&(1<<j)) == 0) {
					first.add(j);
				}else {
					second.add(j);
				}
			}
			
			if(first.size()!=n/2) {
				continue;
			}
			
			int t1=0;
			int t2=0;
			for(int i2=0; i2<n/2; i2++) {
				for(int j2=0; j2<n/2; j2++) {
					if(i2==j2) {
						continue;
					}
					t1+=s[ first.get(i2) ][ first.get(j2) ];
					t2+=s[ second.get(i2) ][ second.get(j2) ];
				}
			}
			
			if(ans==-1 || ans>Math.abs(t1-t2)) {
				ans = Math.abs(t1-t2);
			}
			
		}
		System.out.println(ans);
	}

}
