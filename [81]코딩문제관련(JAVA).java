package test;

import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;

public class _81_코딩문제관련_JAVA {

	public static void main(String[] args) {
		String[] str = {"cat","Dog","lion","tiger"};
		Arrays.sort(str);
		System.out.println("str="+Arrays.toString(str));
		
		Arrays.sort(str,String.CASE_INSENSITIVE_ORDER);
		System.out.println("str="+Arrays.toString(str));
		
		Arrays.sort(str,new Descending());
		System.out.println("srt="+Arrays.toString(str));
	}
	
}
class Descending implements Comparator{

	@Override
	public int compare(Object o1, Object o2) {
		if(o1 instanceof Comparable && o2 instanceof Comparable) {
			Comparable c1 =(Comparable)o1;
			Comparable c2 =(Comparable)o2;
			return c1.compareTo(c2)*-1;
		}
		return -1;
	}
	
}
