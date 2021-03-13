package test;

import java.util.function.Predicate;
import java.util.*;

public class _93_코딩문제관련_JAVA {

	public static void main(String[] args) {
		/*
		Box<String> b = new Box<String>();
		b.setItem("ABC");
		String item = b.getItem();
		System.out.println(item);
		*/
		/*
		Predicate<String> isEmptyStr = s->s.length() == 0;
		String s = "";
		
		if(isEmptyStr.test(s)) {
			System.out.println("This is an empty String.");
		}
		*/
		ArrayList<Integer> list = new ArrayList<>();
		for(int i=0;i<10;i++) {
			list.add(i);
		}
		
		list.forEach(i->System.out.print(i+","));
		System.out.println();
		
		list.removeIf(x->x%2==0 || x%3==0);
		System.out.println(list);
		
		list.replaceAll(i->i*10);
		System.out.println(list);
		
		Map<String,String> map = new HashMap<>();
		map.put("1", "1");
		map.put("2", "2");
		map.put("3", "3");
		map.put("4", "4");
		
		map.forEach((k,v)->System.out.print("{"+k+","+v+"},"));
		System.out.println();
	}

}

class Box<T>{
	T item;
	void setItem(T item) {
		this.item=item;
	}
	T getItem() {
		return item;
	}
}
