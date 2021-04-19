package test;

import java.util.*;

/*
 * 설탕 배달
 * 내가쓴 코드
 * 결과 = 맞았습니다!!
 */
public class _116_코딩문제_JAVA_설탕배달 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int r=0,t=0,n1=(n/5),n2=0;
		
		while(true){
			t=n-((5*n1)+(3*n2));
			if(t<=0)
				break;
			if(t<3 && n1>0) {
				n1-=1;
			}
			n2+=1;
		}
		
		if(t<0) {
			System.out.println(-1);
		}else {
			System.out.println(n1+n2);
		}
	}

}
