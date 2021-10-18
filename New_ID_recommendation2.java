package Kakao_upload;

/*
 * 신규 아이디 추천(다른풀이)
 * 내가쓴 코드
 * 결과 = 정확성: 100.0
 * 합계: 100.0 / 100.0
 */

import java.util.regex.*;

public class New_ID_recommendation2 {

	class Solution {
	    public String solution(String new_id) {
	        String answer = "";
	        
	        Pattern p = Pattern.compile("[A-Z]");
	        Matcher m = p.matcher(new_id);
	        StringBuilder sb = new StringBuilder();
	        while(m.find()){
	            m.appendReplacement(sb,m.group().toLowerCase());
	        }
	        m.appendTail(sb);
	        new_id = sb.toString();
	        
	        new_id = new_id.replaceAll("[^\\w.-]","");
	        new_id=new_id.replaceAll("\\.{2,}",".");
	        new_id=new_id.replaceAll("^\\.|\\.$","");
	        p = Pattern.compile("[\\w.-]+");
	        m = p.matcher(new_id);
	        if(!m.find()){
	            new_id=new_id+"a";
	        }
	        
	        p = Pattern.compile(".{16,}");
	        m = p.matcher(new_id);
	        if(m.find()){
	            new_id = m.group().substring(0,15);
	            if(new_id.charAt(14)=='.'){
	                new_id = m.group().substring(0,14);
	            }
	        }
	        
	        p = Pattern.compile(".{3,}");
	        if(!m.find()){
	            String s = ""+new_id.charAt(new_id.length()-1);
	            while(new_id.length()<3){
	                new_id+=s;
	            }
	        }
	        answer = new_id;
	        return answer;
	    }
	}
}
