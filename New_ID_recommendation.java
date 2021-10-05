package Kakao_upload;

import java.util.*;

/*
 * 내가쓴 코드
 * 결과 = 정확성: 100.0 합계: 100.0 / 100.0
 */
public class New_ID_recommendation {
	class Solution {
	    public String solution(String new_id) {
	        String answer = "";
	        set.add('-');
	        set.add('_');
	        set.add('.');
	        
	        new_id=step1(new_id);
	        new_id=step2(new_id);
	        new_id=step3(new_id);
	        new_id=step4(new_id);
	        new_id=step5(new_id);
	        new_id=step6(new_id);
	        new_id=step7(new_id);
	        
	        answer = new_id;
	        return answer;
	    }

	    public String step1(String str){
	        return str.toLowerCase();
	    }
	    
	    public Set<Character> set = new HashSet<>();
	    
	    public String step2(String str){
	        StringBuilder sb = new StringBuilder();
	        for(int i=0;i<str.length();i++){
	            char ch = str.charAt(i);
	            if(set.contains(ch) || Character.isDigit(ch) || Character.isLetter(ch)){
	                sb.append(ch);
	            }
	        }
	        return sb.toString();
	    }
	    
	    public String step3(String str){
	        StringBuilder sb = new StringBuilder();
	        int c=0;
	        for(int i=0;i<str.length();i++){
	            char ch = str.charAt(i);
	            if(ch=='.' && c!=0){
	                continue;
	            }
	            sb.append(ch);
	            if(ch=='.'){
	                c=1;
	            }else{
	                c=0;
	            }
	        }
	        return sb.toString();
	    }
	    
	    public String step4(String str){
	        int s=0;
	        int e=str.length();
	        if(str.charAt(s)=='.'){
	            s=1;
	        }
	        if(e>s && str.charAt(e-1)=='.'){
	            e-=1;
	        }
	        return str.substring(s,e);
	    }
	    
	    public String step5(String str){
	        if(str.isEmpty()){
	            return "a";
	        }
	        return str;
	    }
	    
	    public String step6(String str){
	        StringBuilder sb = new StringBuilder(str);
	        if(sb.length()>=16){
	            sb.delete(15,str.length());
	            if(sb.charAt(14)=='.'){
	                sb.deleteCharAt(14);
	            }
	        }
	        return sb.toString();
	    }
	    
	    public String step7(String str){
	        StringBuilder sb = new StringBuilder(str);
	        if(str.length()<=2){
	            char ch = str.charAt(str.length()-1);
	            while(sb.length()!=3){
	                sb.append(ch);
	            }
	        }
	        return sb.toString();
	    }
	}
}
