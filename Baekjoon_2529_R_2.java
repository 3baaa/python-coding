package upload.new_upload;

import java.util.*;

/*
 * 부등호
 * 다시 풀었다
 */
public class Baekjoon_2529_R_2 {
	static int k;
	static int[] arr;
	static List<String> list = new ArrayList<String>();
	static boolean[] b = new boolean[10];
	
	public static boolean check(String num) {
		for(int i=0;i<k;i++) {
			if(arr[i] == '<') {
				if(num.charAt(i)>num.charAt(i+1)) {
					return false;
				}
			}
			if(arr[i] == '>') {
				if(num.charAt(i)<num.charAt(i+1)) {
					return false;
				}
			}
		}
		return true;
	}
	
	public static void go(int index,String num) {
		if(index == k+1) {
			if(check(num)) {
				list.add(num);
			}
			return;
		}
		for(int i=0;i<10;i++) {
			if(b[i]) {
				continue;
			}
			b[i]=true;
			go(index+1,num+i);
			b[i]=false;
		}
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		k = sc.nextInt();
		arr = new int[k];
		for(int i=0;i<k;i++) {
			arr[i] = sc.next().toCharArray()[0];
		}
		
		go(0,"");
		Collections.sort(list);
		System.out.println(list.get(list.size()-1));
		System.out.println(list.get(0));
	}

}
