package test;
/*
 * 문자열_뒤집기
 * 내가쓴 코드
 * 결과 = Accepted
 */
public class 문자열_뒤집기 {
	
	class Solution {
	    public void reverseString(char[] s) {
	        int n=s.length;
	        for(int i=0;i<n/2;i++){
	            char t=s[i];
	            s[i]=s[n-(i+1)];
	            s[n-(i+1)]=t;
	        }
	    }
	}
}
