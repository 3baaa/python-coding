package test;

/*
 * 로그 파일 재정렬
 * 내가쓴 코드
 * 결과 = Accepted
 */

public class 로그_파일_재정렬 {

	class Solution {
	    public static List<Log> r1;
	    public String[] reorderLogFiles(String[] logs) {
	        List<String> r3=new ArrayList<String>();
	        List<String> r2=new ArrayList<String>();
	        r1=new ArrayList<Log>();
	        for(int i=0;i<logs.length;i++){
	            String[] t = logs[i].split("\\s");
	            boolean a=true;
	            for(int j=0;j<t[1].length();j++){
	                if(!Character.isDigit(t[1].charAt(j))){
	                    a=false;
	                    break;
	                }
	            }
	            if(!a){
	                r1.add(new Log(t));
	            }else{
	                r2.add(logs[i]);
	            }
	            
	        }
	        Collections.sort(r1);
	        
	        for(Log log : r1){
	            r3.add(log.toString());
	        }
	        r3.addAll(r2);
	        return r3.toArray(logs);
	    }
	}

	class Log implements Comparable<Log>{
	    String[] log_str;
	    public Log(String[] log_str){
	        this.log_str=log_str;
	    }
	    
	    public int compareTo(Log l){
	        String[] l_str=l.log_str;
	        int a=this.log_str.length;
	        if(l_str.length<this.log_str.length){
	            a=l_str.length;
	        }
	        for(int i=1;i<a;i++){
	            int r = log_str[i].compareTo(l_str[i]);
	            if(r==0){
	                continue;
	            }else if(r>0){
	                return 1;
	            }else{
	                return -1;
	            }
	        }
	        if(log_str.length<l_str.length){
	            return -1;
	        }
	        return log_str[0].compareTo(l_str[0]);
	    }
	    
	    public String toString(){
	        String r="";
	        for(String s : log_str){
	            r+=s+" ";
	        }
	        return r.trim();
	    }
	}
}
