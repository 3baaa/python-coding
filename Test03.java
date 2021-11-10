package upload.new_upload;

/*
 * Up and down
 * 빈칸 채우기
 * 결과 = 정확성: 100.0 합계: 100.0 / 100.0
 */
public class Test03 {
	static class Solution {
	    public int solution(int K, int[] numbers, String[] UpDown) {
	        int left = 1;
	        int right = K;
	        for(int i = 0; i < numbers.length; i++) {
	            int num = numbers[i];
	            if(UpDown[i].equals("UP"))
	                left = Math.max(left,num);
	            else if(UpDown[i].equals("DOWN"))
	                right = Math.min(right,num);
	            else if(UpDown[i].equals("RIGHT"))
	                return 1;
	        }
	        return right-left-1;
	    }

	    public static void main(String[] args) {
	        Solution sol = new Solution();
	        int K1 = 10;
	        int[] numbers1 = {4, 9, 6};
	        String[] UpDown1 = {new String("UP"), new String("DOWN"), new String("UP")};
	        int ret1 = sol.solution(K1, numbers1, UpDown1);

	        System.out.println("solution 메소드의 반환 값은 " + ret1 + " 입니다.");

	        int K2 = 10;
	        int[] numbers2 = {2, 1, 6};
	        String[] UpDown2 = {new String("UP"), new String("UP"), new String("DOWN")};
	        int ret2 = sol.solution(K2, numbers2, UpDown2);

	        System.out.println("solution 메소드의 반환 값은 " + ret2 + " 입니다.");

	        int K3 = 100;
	        int[] numbers3 = {97, 98};
	        String[] UpDown3 = {new String("UP"), new String("RIGHT")};
	        int ret3 = sol.solution(K3, numbers3, UpDown3);

	        System.out.println("solution 메소드의 반환 값은 " + ret3 + " 입니다.");
	    }
	}
}
