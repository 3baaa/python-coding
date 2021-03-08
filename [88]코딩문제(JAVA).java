package test;

import java.util.*;

/* 가사검색
 * 내가쓴 코드 + 참고
 * (결과값이나온다 100.0= 25.0(정확성) + 75.0(효율성))
 */
public class _88_코딩문제_JAVA {
}

class Solution88 {
    public int[] solution(String[] words, String[] queries) {
        int[] answer = new int[queries.length];
        List<ArrayList<String>> list1 = new ArrayList<ArrayList<String>>();
        List<ArrayList<String>> list2 = new ArrayList<ArrayList<String>>();
        for(int i=0;i<10001;i++){
            list1.add(new ArrayList());
            list2.add(new ArrayList());
        }
        for(String str : words){
            list1.get(str.length()).add(str);
            list2.get(str.length()).add(ch(str));
        }
        for(int i=0;i<10001;i++){
            Collections.sort(list1.get(i));
            Collections.sort(list2.get(i));
        }
        
        int c=0;
        for(String str : queries){
            int r1,r2,t=0;
            int l=str.length();
            List q;
            if(str.charAt(0)=='?'){
                str=ch(str);
                t=1;
            }
            String sl=str.replace('?','a');
            String sr=str.replace('?','z');
            if(t==1){
                q=list2.get(l);
                r1=right(q,sr,0,q.size());
                r2=left(q,sl,0,q.size());
                if(r1-r2==0){
                    answer[c]=0;
                }else{
                    answer[c]=r1-r2;
                }
            }else{
                q=list1.get(l);
                r1=right(q,sr,0,q.size());
                r2=left(q,sl,0,q.size());
                if(r1==-1){
                    answer[c]=0;
                }else{
                    answer[c]=r1-r2;
                }
            }
            c+=1;
            
        }
        return answer;
    }
    
    public static String ch(String str){
        String t="";
        for(int i=str.length()-1;i>=0;i--){
            t+=str.charAt(i);
        }
        return t;
    }
    
    public static int left(List q,String str,int s,int e){
        int m;
        while(s<e){
            m=(s+e)/2;
            if(str.compareTo((String) q.get(m))<=0){
                e=m;
            }else{
                s=m+1;
            }
        }
        return e;
    }
    
    public static int right(List q,String str,int s,int e){
        int m;
        while(s<e){
            m=(s+e)/2;
            if(str.compareTo((String)q.get(m))>=0){
                s=m+1;
            }else{
                e=m;
            }
        }
        return e;
    }
}