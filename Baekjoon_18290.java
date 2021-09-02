package upload.new_upload;

import java.util.*;

/*
 * nm과 k
 * 내가쓴 코드
 * 결과 = 틀렸습니다(예제 출력은 나옵니다)
 */
public class Baekjoon_18290 {

	static int n;
	static int m;
	static int k;
	static int[][] arr;
	static List<T> list1;
	static List<T> list2;
	static List<Integer> list_ans;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n=sc.nextInt();
		m=sc.nextInt();
		k=sc.nextInt();
		arr = new int[n][m];
		list1 = new ArrayList<T>();
		list2 = new ArrayList<T>();
		sc.nextLine();
		for(int i=0;i<n;i++) {
			StringTokenizer st = new StringTokenizer(sc.nextLine()," ");
			for(int j=0;st.hasMoreTokens();j++) {
				arr[i][j]=Integer.parseInt(st.nextToken());
			}
		}
		
		test1();
		
		list_ans = new ArrayList<Integer>();
		Stack<T> stack = new Stack<T>();
		
		test2(list1,stack,0,0);
		test2(list2,stack,0,0);
		
		System.out.println(Collections.max(list_ans));
	}
	
	static void test1() {
		for(int i=0;i<n;i++) {
			for(int j=0;j<m;j++) {
				T t = new T(i,j);
				if((i+j)%2==0) {
					list1.add(t);
				}else {
					list2.add(t);
				}
			}
		}
	}
	
	static void test2(List<T> list,Stack<T> stack,int a,int c) {
		if(c==k) {
			int r = 0;
			while(!stack.isEmpty()) {
				T t = stack.pop();
				r+=arr[t.i][t.j];
			}
			list_ans.add(r);
			return;
		}
		
		for(int i=a;i<list.size();i++) {
			stack.push(list.get(i));
			test2(list,stack,i+1,c+1);
		}
		
		stack.clear();
	}
}

class T{
	int i;
	int j;
	
	T(int i,int j){
		this.i=i;
		this.j=j;
	}
}
