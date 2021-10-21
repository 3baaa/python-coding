package upload.new_upload;

import java.util.*;

/*
 * 부등호
 * 내가쓴 코드(실패)
 */
public class Baekjoon_2529_f {

	public static int k;
	public static String[] arr;
	public static int ans_big = Integer.MIN_VALUE;
	public static int ans_small = Integer.MAX_VALUE;
	public static int t(int s,int e,int c,List<Integer> list) {
		if(c==k+1) {
			int all=0;
			for(int i : list) {
				all+=i;
			}
			return all;
		}

		int r=-1;
		for(int i=s;i<e;i++) {
			list.add(i);
			if(c==k) {
				r=t(i,e,c+1,list);
			}else {
				String str = arr[c];
				if(str.equals("<")) {
					if( c+1<10 ) {
						r=t(i+1,e,c+1,list);
					}else {
					return -1;
					}
				}else if(str.equals(">")) {
					if(c-1>-1 ) {
						r=t(s,i-1,c+1,list);
					}else {
						return -1;
					}
				}
			}
			
			if(r!=-1) {
				ans_big = Math.max(ans_big, r);
				ans_small = Math.min(ans_small, r);
			}
			list.remove(list.size()-1);
		}
		
		return r;
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		k = sc.nextInt();
		sc.nextLine();
		arr = sc.nextLine().split("\\s");
		List<Integer> list = new ArrayList<Integer>();
		t(0,9,0,list);
		System.out.println(ans_big);
		System.out.println(ans_small);
	}

}
