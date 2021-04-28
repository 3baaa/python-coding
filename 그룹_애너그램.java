package test;

/*
 * 그룹 애너그램
 * 답(파이썬의 답보고 쓴코드)
 */
import java.util.*;

public class 그룹_애너그램 {

	class Solution {
	    public List<List<String>> groupAnagrams(String[] strs) {
	        Map<String,List<String>> an = new HashMap();
	        List<List<String>> r = new ArrayList<List<String>>();
	        
	        for(int i=0;i<strs.length;i++){
	            char[] c = strs[i].toCharArray();
	            Arrays.sort(c);
	            String word=new String(c);
	            if(an.containsKey(word)){
	                an.get(word).add(strs[i]);
	            }else{
	                List<String> t = new ArrayList<String>();
	                t.add(strs[i]);
	                an.put(word,t);
	            }
	        }
	        
	        Iterator iter = an.keySet().iterator();
	        while(iter.hasNext()){
	            String k = (String)iter.next();
	            r.add(an.get(k));
	        }
	        return r;
	    }
	}
}
