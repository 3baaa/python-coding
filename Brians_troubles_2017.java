package Kakao_upload;

import java.util.*;
/*
 * 내가쓴 코드
 * 실패
 */
public class Brians_troubles_2017 {
	
	public static void main(String[] args) {
	}

}
class Brians_troubles_Solution {
    public String solution(String sentence) {
        String answer = "";
        char lower_w = '0';
        int lower_c=0;
        //int upper_c=0;
        Queue<Character> q = new LinkedList<Character>();
        Stack<Character> stack = new Stack<Character>();
        //boolean check_upper = false;
        
        for(int i=0;i<sentence.length();i++) {
        	char ch = sentence.charAt(i);
        	if(Character.isUpperCase(ch)) {
        		q.offer(ch);
        	}else if(Character.isLowerCase(ch)){
        		if(lower_c==0) {
        			lower_w=ch;
        			lower_c+=1;
        			stack.push(ch);
        		}else {
        			if(stack.peek()!=ch) {
        				stack.pop();
        				stack.push(ch);
        				lower_c=1;
        				while(!q.isEmpty()) {
        					answer+=q.poll();
        				}
        			}
        		}
        		
        		/*
        		if(lower_c==0) {
        			lower_w=ch;
        			lower_c+=1;
        		}else if(lower_w!=ch) {
        			lower_w=ch;
        			lower_c=1;
        			answer+=" ";
        		}else {
        			lower_c+=1;
        		}
        		*/
        		
        	}
        }
        System.out.println(q);
    	System.out.println("lower_c = "+lower_c);
        while(!q.isEmpty()) {
        	answer+=q.poll();
        }
        /*
        if(!q.isEmpty()) {
        	return "invalid";
        }
        */
        return answer;
    }
}
