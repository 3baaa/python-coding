package upload.new_upload;

import java.util.*;

/*
 * 숫자 뽑기
 * 함수 작성
 * 결과 = 실패
 */
public class Test09 {
	static // 다음과 같이 import를 사용할 수 있습니다.
	class Solution {
	    public int solution(int[] arr, int K) {
	        // 여기에 코드를 작성해주세요.
	        int answer = 0;
	        answer=check(10001,0,0,K,new ArrayList<Integer>(),arr);
	        return answer;
	    }

	    public int check(int answer,int s,int c,int K,List<Integer> list,int[] arr){
	        if(c==K){
	            return list.get(list.size()-1)-list.get(0);
	        }
	        
	        for(int i=s;i<arr.length;i++){
	            if(c==0 || arr[i]-list.get(0)<answer){
	                list.add(arr[i]);
	                answer = Math.min(answer,check(answer,i+1,c+1,K,list,arr));
	                list.remove(list.size()-1);
	            }
	        }
	        return answer;
	    }

	    public static void main(String[] args) {
	        Solution sol = new Solution();
	        int[] arr = {9, 11, 9, 6, 4, 19};
	        int K = 4;
	        Arrays.sort(arr);
	        int ret = sol.solution(arr, K);

	        System.out.println("solution 메소드의 반환 값은 " + ret + "입니다.");
	    }
	}
}
