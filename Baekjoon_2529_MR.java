package test;

import java.util.*;

/*
 * 부등호
 * 다시 문제 품(실패)
 */


public class Baekjoon_2529_MR {

	public static String ans1;
	public static String ans2;
	public static int sbl;
	public static boolean[] b = new boolean[10];
	public static String[] oper;
	public static int check(String s,int count) {
		if(count == sbl) {
			System.out.println("sbaaaaaaaaaaaaaaaaaaaaa = "+s);
			System.out.println("ans1 = "+ans1);
			System.out.println("asn2 = "+ans2);
			System.out.println("s = "+s);
			if(ans1.compareTo(s)<0) {
				ans1 = s;
			}
			if(ans2.compareTo(s)>0) {
				ans2 = s;
			}
			s="";
			return 0;
		}
		
		for(int i=0;i<10;i++) {
			if(b[i]) {
				continue;
			}
			if(s.length()!=0){
				System.out.println("count = "+count);
				System.out.println("s = "+s);
				char ch = s.charAt(count-1);
				int t = Integer.valueOf(ch-'0');
				if(oper[count-1].equals("<")) {
					if(t>i) {
						System.out.println("t = "+t);
						System.out.println("s = "+s+" [ sb.charAt = "+s.charAt(count-1)+"] [ i = "+i+" ]");
						//System.out.println("1-"+" i = "+i);
						return -1;
					}
				}else {
					if(t<i) {
						System.out.println("2-"+" i = "+i);
						return -1;
					}
				}
			}
			b[i]=true;
			s+=i;
			int r = check(s,count+1);
			b[i]=false;
			if(r==-1) {
				s="";
				return -1;
			}
		}
		return count;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int k = sc.nextInt();
		char[] t = new char[k];
		Arrays.fill(t,'0');
		ans1 = new String(t.clone());
		Arrays.fill(t, '9');
		ans2 = new String(t.clone());
		
		sbl= k+1;
		
		sc.nextLine();
		oper = sc.nextLine().split("\\s");
		System.out.println("oper = "+Arrays.toString(oper));
		check("",0);
		
		System.out.println("ans1 = "+ans1);
		System.out.println("ans2 = "+ans2);
		
		char f = '4';
		if(f-'0'>9) {
			System.out.println("ttttttttttttt");
			System.out.println('4');
			System.out.println("--"+('4'-'0'));
			System.out.println("-"+String.valueOf(9));
		}
	}

}
