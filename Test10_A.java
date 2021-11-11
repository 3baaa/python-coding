package upload.new_upload;

import java.util.*;

/*
 * 메모장
 * 함수 작성
 * 답
 */

public class Test10_A {

	static class Solution {
	    public int solution(int K, String[] words) {
	        int answer = 1;
	        int freeSpace = K;
	        int wdCnt = words.length;
	        for(int i=0;i<wdCnt;i++){
	            freeSpace -= words[i].length()+1;
	            if(freeSpace < -1 ){
	                answer++;
	                freeSpace = K - (words[i].length()+1);
	            }
	        }
	        return answer;
	    }
	    
	    public static void main(String[] args) {
	        Solution sol = new Solution();
	        int K = 10;
	        String[] words = {new String("nice"), new String("happy"), new String("hello"), new String("world"), new String("hi")};
	        int ret = sol.solution(K, words);

	        System.out.println("solution 메소의 반환 값은 " + ret + " 입니다.");
	    }
	}
}
