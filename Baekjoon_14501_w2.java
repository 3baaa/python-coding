package upload.new_upload;

import java.util.*;

/*
 * 퇴사
 * 내가쓴 코드
 * 
 */
public class Baekjoon_14501_w2 {

	static int n;
	static int[] t,p;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		n = sc.nextInt();
		t = new int[n];
		p = new int[n];
		
		for(int i=0;i<n;i++) {
			t[i]=sc.nextInt();
			p[i]=sc.nextInt();
		}
		
		System.out.println(test(0,0,0));
	}
	
	public static int test(int s,int c,int v) {
		System.out.println("-------------s= "+s+" v= "+v);
		
		if(s>=n) {
			System.out.println("e");
			System.out.println();
			return v;
		}
		
		int r=0;
		for(int i=s;i<n;i++) {
			if(i+t[i]>n) {
				continue;
			}
			System.out.println("s= "+s+" i= "+i+" v = "+v+" p["+i+"]= "+p[i]);
			//v+=p[i];
			System.out.println("v= "+v+" "+i+"+"+"t["+i+"] = "+(i+t[i]));
			int a = test(i+t[i],c+1,v+p[i]);
			System.out.println("a = "+a);
			r=Math.max(r, a);
			//v-=p[i];
			System.out.println("vvvvv= "+v);
		}
		return r;
	}
}
/*
class B_14501 {
	int v;
	int c;
	
	public B_14501(int v,int c){
		this.v = v;
		this.c = c;
	}
}
*/