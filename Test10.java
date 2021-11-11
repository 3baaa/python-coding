package upload.new_upload;

import java.util.*;

/*
 * 메모장
 * 함수 작성
 * 결과 = 실패
 */

public class Test10 {

	static class Solution {
	    public int solution(int K, String[] words) {
	        int answer = 0;
	        int l = 0;
	        int t = K;
	        for(int i=0;i<words.length;i++){
	            int r = t - (words[i].length()+1);
	            if( r >= 0){
	                t=r;
	                answer++;
	            }else{
	                t=K;
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
