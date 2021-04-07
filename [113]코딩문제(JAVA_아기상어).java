package test;

import java.util.*;

/*
 * 아기상어
 * 내가쓴 코드
 * 결과값이 나온다
 */
public class _113_코딩문제_JAVA_아기상어 {
	static int n;
	static int[][] a;
	static Shark_l shark_l=null;
	static int shark_b=2;
	static int[] dx= {-1,1,0,0};
	static int[] dy= {0,0,-1,1};
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n=sc.nextInt();
		a = new int[n][n];
		
		for(int i=0;i<n;i++) {
			for(int j=0;j<n;j++) {
				a[i][j]=sc.nextInt();
				if(a[i][j]==9) {
					shark_l=new Shark_l(i,j,0);
				}
			}
		}
		
		while(true) {
			List<Fish_l> f=check();
			if(f.isEmpty()) {
				break;
			}
			int shark_e=0;
			Collections.sort(f);
			Queue<Fish_l> f_q = new LinkedList<Fish_l>();
			for(Fish_l ff : f) {
				shark_e=z(shark_e,ff);
			}
		}
		
		System.out.println(shark_l.getC());
	}
	
	public static List<Fish_l> check(){
		List<Fish_l> f=new ArrayList<Fish_l>();
		for(int i=0;i<n;i++) {
			for(int j=0;j<n;j++) {
				if(a[i][j]!=0 && shark_b>a[i][j]) {
					int d=Math.abs(shark_l.getX()-i)+Math.abs(shark_l.getY()-j);
					f.add(new Fish_l(d, i, j));
				}
			}
		}
		return f;
	}

	public static int z(int shark_e,Fish_l f_l) {
		Queue<Shark_l> s_q = new LinkedList<Shark_l>();
		s_q.offer(shark_l);
		int f_x=f_l.getX();
		int f_y=f_l.getY();
		while(!s_q.isEmpty()) {
			Shark_l s_l=s_q.poll();
			int x=s_l.getX();
			int y=s_l.getY();
			int c=s_l.getC();
			for(int i=0;i<4;i++) {
				int nx=x+dx[i];
				int ny=y+dy[i];
				if(nx>=0 && nx<n && ny>=0 && ny<n) {
					if(a[nx][ny]==a[f_x][f_y]) {
						shark_e+=1;
						a[nx][ny]=0;
						if(shark_e==shark_b) {
							shark_e=0;
							shark_b+=1;
						}
						shark_l=new Shark_l(nx, ny, c+1);
						return shark_e;
					}else if(a[nx][ny]>shark_b) {
						continue;
					}
					s_q.offer(new Shark_l(nx,ny,c+1));
				}
			}
		}
		return shark_e;
	}
}

class Fish_l implements Comparable<Fish_l>{
	
	private int d,x,y;
	
	public Fish_l(int d,int x,int y) {
		this.d=d;
		this.x=x;
		this.y=y;
	}
	
	public int getD() {
		return d;
	}


	public int getX() {
		return x;
	}


	public int getY() {
		return y;
	}

	@Override
	public int compareTo(Fish_l o) {
		if(this.d<o.d) {
			return -1;
		}
		return 1;
	}
	
}

class Shark_l{
	private int x,y,c;
	public Shark_l(int x,int y,int c) {
		this.x=x;
		this.y=y;
		this.c=c;
	}
	public int getX() {
		return x;
	}
	public int getY() {
		return y;
	}
	
	public int getC() {
		return c;
	}
	
	
}
