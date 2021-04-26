package test;

/*
 * 유효한 팰린드롬
 * 내가쓴 코드
 * 결과 = Accepted
 */

public class 유효한_팰린드롬 {

	class Solution {
	    public boolean isPalindrome(String s) {
	        s=s.toUpperCase();
	        StringBuffer r = new StringBuffer();
	        
	        for(int i=0;i<s.length();i++){
	            char t=s.charAt(i);
	            if(('0'<=t && '9'>=t) || ('A'<=t && 'Z'>=t)){
	                r.append(t);
	            }
	        }
	        String r2=r.toString();
	        String r3=r.reverse().toString();
	        return r2.equals(r3);
	    }
	}
}
