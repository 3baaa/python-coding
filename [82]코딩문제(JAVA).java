package test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
//내가쓴 코드
//결과값이나온다 정확도 100.0
public class _82_코딩문제_JAVA {
	public static void main(String[] args) {
	}
	public static int[] solution(int N, int[] stages) {
        int[] answer = new int[N];
        int l = stages.length;
        ArrayList<T> r1 = new ArrayList<T>();
        for(int i=0;i<N+1;i++){
        	r1.add(new T(i));
        }
        for(int i : stages) {
        	if(i!=N+1) {
        		r1.get(i).setC(r1.get(i).getC()+1);
        	}	
        }
        r1=new ArrayList<T>(r1.subList(1, r1.size()));
        
        for(T t : r1) {
        	double z=t.getC();
        	if(z==0.0) {
        		t.setC(0);
        	}else {
        		t.setC(t.getC()/l);
        	}
        	l-=z;
        }
        Collections.sort(r1);
        for(int i=0;i<r1.size();i++) {
        	answer[i]=r1.get(i).getIdx();
        }
        return answer;
    }
}
class T implements Comparable{
	private int idx;
	private double c;
	
	public T(int idx) {
		this.idx=idx;
	}
	public int getIdx() {
		return idx;
	}
	public void setIdx(int idx) {
		this.idx = idx;
	}
	public double getC() {
		return c;
	}
	public void setC(double c) {
		this.c = c;
	}
	@Override
	public int compareTo(Object o) {
		T t = (T)o;
		if(c>t.getC()) {
			return -1;
		}else if(c==t.getC()) {
			return 0;
		}else {
			return 1;
		}
	}
	
	@Override
	public String toString() {
		return idx+","+c;
	}
}