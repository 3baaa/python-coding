package test;

/*
 * 가장_흔한_단어
 * 내가쓴 코드
 * 결과 = Accepted
 */

import java.util.*;

public class 가장_흔한_단어 {

	class Solution {
	    public String mostCommonWord(String paragraph, String[] banned) {
	        Map<String,Integer> rm = new HashMap<String,Integer>();
	        paragraph=paragraph+" ";
	        StringBuffer s = new StringBuffer();
	        for(int i=0;i<paragraph.length();i++){
	            char c = paragraph.charAt(i);
	            if(('a'<=c && c<='z') || ('A'<=c && c<='Z')){
	                s.append(c);
	            }else{
	                if(s.toString().equals("")){
	                    continue;
	                }
	                String t=new String(s).toLowerCase();
	                if(rm.containsKey(t)){
	                    rm.put(t,rm.get(t)+1);
	                }else{
	                    rm.put(t,1);
	                }
	                s=new StringBuffer();
	            }
	        }
	        Iterator<Map.Entry<String,Integer>> iter = rm.entrySet().iterator();
	        String r_k="";
	        int r_v=-1;
	        while(iter.hasNext()){
	            Map.Entry<String,Integer> e = iter.next();
	            String k = e.getKey();
	            Integer v = e.getValue();
	            int r2=0;
	            if(r_v<v){
	                for(String b_k : banned){
	                    if(k.equals(b_k)){
	                        r2=1;
	                        break;
	                    }
	                }
	                if(r2==0){
	                    r_v=v;
	                    r_k=k;
	                }
	            }
	        }
	        return r_k;
	    }
	}
}
