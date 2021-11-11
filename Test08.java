package upload.new_upload;

/*
 * 꽃피우기
 * 함수 작성
 * 결과 = 정확성: 100.0 합계: 100.0 / 100.0
 */
import java.util.*;

public class Test08 {

	static class Solution {
	    public int[] dx = {-1,1,0,0};
	    public int[] dy = {0,0,-1,1};
	    
	    public int solution(int[][] garden) {
	        int answer = 0;
	        Queue<V> v = new LinkedList<>();
	        for(int i=0;i<garden.length;i++){
	            for(int j=0;j<garden.length;j++){
	                if(garden[i][j]==1){
	                    v.offer(new V(i,j));
	                }
	            }
	        }
	        
	        while(true){
	            if(!e(garden) || v.isEmpty()){
	                break;
	            }
	            answer+=1;
	            v=check(v,answer,garden);
	        }
	        return answer;
	    }
	    
	    public Queue<V> check(Queue<V> v,int answer,int[][] garden){
	        Queue<V> v2 = new LinkedList<>();
	        while(!v.isEmpty()){
	            V vv = v.poll();
	            int x = vv.x;
	            int y = vv.y;
	            for(int i=0;i<4;i++){
	                int nx = x + dx[i];
	                int ny = y + dy[i];
	                if(nx<0 || nx>=garden.length || ny<0 || ny>=garden.length){
	                    continue;
	                }
	                if(garden[nx][ny]!=0){
	                    continue;
	                }
	                garden[nx][ny]=answer;
	                v2.offer(new V(nx,ny));
	            }
	        }
	        return v2;
	    }
	    
	    public boolean e(int[][] garden){
	        for(int[] gar : garden){
	            for(int g : gar){
	                if(g==0){
	                    return true;
	                }
	            }
	        }
	        
	        return false;
	    }
	    public static void main(String[] args) {
	        Solution sol = new Solution();
	        int[][] garden1 = {{0, 0, 0}, {0, 1, 0}, {0, 0, 0}};
	        int ret1 = sol.solution(garden1);
	        
	        System.out.println("solution 메소드의 반환 값은 " + ret1 + " 입니다.");
	        
	        int[][] garden2 = {{1, 1}, {1, 1}};
	        int ret2 = sol.solution(garden2);
	        
	        System.out.println("solution 메소드의 반환 값은 " + ret2 + " 입니다.");
	        
	    }    
	}

	static class V{
	    int x;
	    int y;
	    
	    public V(int x,int y){
	        this.x = x;
	        this.y = y;
	    }
	}
}
