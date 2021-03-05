package test;

import java.util.*;
//가사검색
//내가쓴 코드
//#(결과값은 나오나 정확성 테스트 통과 + 효율성 테스트 3개 실패로 합계 55.0 하지만 밑의 주석한것처럼하면 합계 85.0 (효율성 테스트1만 실패) )##
public class _87_코딩문제_JAVA {
}

class Solution {
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
            Collections.sort(list1.get(str.length()));//여기줄을 지우고 밑의 주석의 코드로하면 합계 85.0
            list2.get(str.length()).add(ch(str));
            Collections.sort(list2.get(str.length()));//여기줄을 지우고 밑의 주석의 코드로하면 합계 85.0
        }
        /*
        for(int i=0;i<10001;i++){
            Collections.sort(list1.get(i));
            Collections.sort(list2.get(i));
        }
        */
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
                r1=right(q,sr,0,q.size()-1);
                r2=left(q,sl,0,q.size()-1);
                if(r1==-1){
                    answer[c]=0;
                }else{
                    answer[c]=r1-r2+1;
                }
            }else{
                q=list1.get(l);
                r1=right(q,sr,0,q.size()-1);
                r2=left(q,sl,0,q.size()-1);
                if(r1==-1){
                    answer[c]=0;
                }else{
                    answer[c]=r1-r2+1;
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
        if(s>e){
            return -1;
        }
        int m=(s+e)/2;
        if((m==0 || str.compareTo((String) q.get(m-1))>0) && str.compareTo((String) q.get(m))<0){
            return m;
        }else if(str.compareTo((String) q.get(m))<=0){
            return left(q,str,s,m-1);
        }else{
            return left(q,str,m+1,e);
        }
    }
    
    public static int right(List q,String str,int s,int e){
        if(s>e){
            return -1;
        }
        int m = (s+e)/2;
        if((m==(q.size()-1) || str.compareTo((String) q.get(m+1))<0) && str.compareTo((String) q.get(m))>0){
            return m;
        }else if(str.compareTo((String) q.get(m))>=0){
            return right(q,str,m+1,e);
        }else{
            return right(q,str,s,m-1);
        }
    }
}