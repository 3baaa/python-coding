package upload.new_upload;

/*
 * 보드게임
 * 한줄바꾸기
 * 결과 = 정확성: 100.0 합계: 100.0 / 100.0
 */
public class Test06 {
	static class Solution {
	    public int solution(int[][] board) {
	        int answer = 0;

	        int[][] coins = new int[4][4];
	        for(int i = 0; i < 4; i++) {
	            for(int j = 0; j < 4; j++) {
	                if(i == 0 && j == 0)
	                    coins[i][j] = board[i][j];
	                else if(i == 0 && j != 0)
	                    coins[i][j] = board[i][j] + coins[i][j-1];
	                else if(i != 0 && j == 0)
	                    coins[i][j] = board[i][j] + coins[i-1][j];
	                else
	                    coins[i][j] = board[i][j] + Math.max(coins[i][j-1], coins[i-1][j]);
	            }
	        }

	        answer = coins[3][3];
	        return answer;
	    }

	    public static void main(String[] args) {
	        Solution sol = new Solution();
	        int[][] board = {{6, 7, 1, 2}, {3, 5, 3, 9}, {6, 4, 5, 2}, {7, 3, 2, 6}};
	        int ret = sol.solution(board);

	        System.out.println("solution 메소드의 반환 값은 " + ret + " 입니다.");
	    }
	}
}
