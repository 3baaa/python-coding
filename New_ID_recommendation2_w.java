package Kakao_upload;

import java.util.regex.*;

public class New_ID_recommendation2 {

	class Solution {
	    public String solution(String new_id) {
	        String answer = "";
	        
	        System.out.println("first = "+new_id);
	        
	        Pattern p = Pattern.compile("[A-Z]");
	        Matcher m = p.matcher(new_id);
	        StringBuilder sb = new StringBuilder();
	        while(m.find()){
	            m.appendReplacement(sb,m.group().toLowerCase());
	        }
	        m.appendTail(sb);
	        new_id = sb.toString();
	        
	        System.out.println("step1 = "+new_id);
	        
	        /*
	        sb.setLength(0);
	        p=Pattern.compile("[a-z]|-|\\.");
	        m = p.matcher(new_id);
	        while(m.find()){
	            m.appendReplacement(sb,"");
	        }
	        m.appendTail(sb);
	        new_id = sb.toString();
	        */
	        new_id = new_id.replaceAll("^[a-z\\d|-|//.]","");
	        System.out.println("step2 = "+new_id);
	        return answer;
	    }
	}
}
