package upload.new_upload;

import java.util.*;

/*
 * 숫자 뽑기
 * 답
 */
public class Test09_A {
	static class Solution {
	    public int solution(int[] arr, int K) {
	        Arrays.sort(arr);
	        int answer = arr[arr.length-1];
	        int len = arr.length-K;
	        for(int i=0; i<=len ; i++){
	            if(answer > arr[i+(K-1)] - arr[i]){
	                answer = arr[i+(K-1)]-arr[i];
	            }
	        }
	        return answer;
	    }

	    public static void main(String[] args) {
	        Solution sol = new Solution();
	        int[] arr = {9, 11, 9, 6, 4, 19};
	        int K = 4;
	        int ret = sol.solution(arr, K);

	        System.out.println("solution 메소드의 반환 값은 " + ret + "입니다.");
	    }
	}
}
