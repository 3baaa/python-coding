package Kakao_upload;

/*
 * 내가쓴 코드
 * 성공
 */

import java.util.*;

public class coloring_book_2017 {

	public static void main(String[] args) {
	}

}
class Solution {
    public static int[] dx = {-1,1,0,0};
    public static int[] dy = {0,0,-1,1};
    public static boolean[][] check;
    
    public int[] solution(int m, int n, int[][] picture) {
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;

        int[] answer = new int[2];
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        
        check = new boolean[m][n];
        
        for(int[] a : picture){
            System.out.println(Arrays.toString(a));
        }
        
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(picture[i][j]!=0 && !check[i][j]){
                    int c = t(n,m,picture,new Ij(i,j));
                    if(c>answer[1]){
                        answer[1]=c;
                    }
                    answer[0]+=1;
                }
            }
        }
        return answer;
    }
    
    public static int t(int n,int m,int[][] picture,Ij ij) {
        Queue<Ij> q = new LinkedList();
        int c = 1;
        int v=picture[ij.i][ij.j];
  
        q.offer(ij);
        check[ij.i][ij.j]=true;

        while(!q.isEmpty()){
            Ij tij = q.poll();
            int x=tij.i;
            int y=tij.j;
            for(int i=0;i<4;i++){
                int nx = x + dx[i];
                int ny = y + dy[i];
                if(nx>=0 && nx<m && ny>=0 && ny<n){
                    if(picture[nx][ny]==v&&!check[nx][ny]){
                        c++;
                        check[nx][ny]=true;
                        q.offer(new Ij(nx,ny));
                    }
                }
            }
        }
        
        return c;
    }
}
class Ij{
    int i,j;
    
    Ij(int i,int j){
        this.i=i;
        this.j=j;
    }
} 
