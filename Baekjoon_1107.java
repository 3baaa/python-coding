package upload.new_upload;

import java.util.*;

/*
 * 리모컨
 * 결과 = 틀렸습니다(예제 출력은 나옵니다)
 */
public class Baekjoon_1107 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		boolean[] check = new boolean[10];
		for(int i=0;i<m;i++) {
			check[sc.nextInt()]=true;
		}
		String str = String.valueOf(n);
		int str_l = str.length();
		int c=0;
		int[] arr1 = new int[str_l];
		StringBuffer sb1 = new StringBuffer();
		int[] arr2 = new int[str_l];
		StringBuffer sb2 = new StringBuffer();
		
		if(n==100) {
			System.out.println(0);
		}else if(m==10) {
			System.out.println(Math.abs(n-100));
		}else {
			for(int i=0;i<str_l;i++) {
				String ch = String.valueOf(str.charAt(i));
				int t=Integer.parseInt(ch);
				int j=check2(t,check);
				int k=check3(t,check);
				
				if(j<0) {
					if(i!=0) {
						arr1[i-1]-=1;
						arr1[i]=check2(9,check);
					}else {
						arr1[0]=0;
					}
				}else {
					arr1[i]=j;
				}
				
				if(k>9) {
					if(i!=0) {
						arr2[i]=check3(0,check);
					}else {
						arr2[i]=9;
					}
				}else {
					arr2[i]=k;
				}
				c++;
			}
			for(int i=0;i<str_l;i++) {
				sb1.append(arr1[i]);
				sb2.append(arr2[i]);
			}
			String str1 = sb1.toString();
			String str2 = sb2.toString();
			int r1 = n-Integer.parseInt(str1)+c;
			int r2 = Integer.parseInt(str2)-n+c;
			System.out.println(Math.min(r1, r2));
		}
	}
	
	static int check2(int j,boolean[] check) {
		while(true) {
			if(j<0 || check[j]==false) {
				break;
			}
			j--;
		}
		return j;
	}
	
	static int check3(int k,boolean[] check) {
		while(true) {
			if(k>9 || check[k]==false) {
				break;
			}
			k++;
		}
		return k;
	}

}
