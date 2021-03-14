package test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;
import java.util.function.Consumer;
import java.util.function.Function;
import java.util.function.IntConsumer;
import java.util.function.IntPredicate;
import java.util.function.IntSupplier;
import java.util.function.IntUnaryOperator;
import java.util.function.Predicate;
import java.util.function.Supplier;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class _94_코딩문제관련_JAVA {

	public static void main(String[] args) {
		/*
		Supplier<Integer> s = ()->(int)(Math.random()*100)+1;
		Consumer<Integer> c = i->System.out.print(i+", ");
		Predicate<Integer> p = i->i%2==0;
		Function<Integer,Integer> f = i->i/10*10;
		List<Integer> list = new ArrayList<>();
		makeRandomList(s, list);
		System.out.println(list);
		printEvenNum(p, c, list);
		List<Integer> newList = doSomething(f,list);
		System.out.println(newList);
		
		IntSupplier s = ()->(int)(Math.random()*100)+1;
		IntConsumer c = i->System.out.print(i+", ");
		IntPredicate p = i->i%2==0;
		IntUnaryOperator op = i->i/10*10;
		
		int[] arr = new int[10];
		
		makeRandomList(s, arr);
		System.out.println(Arrays.toString(arr));
		printEvenNum(p, c, arr);
		int[] newArr = doSomething(op,arr);
		System.out.println(Arrays.toString(newArr));
		
		List<String> list = Arrays.asList("일","이","삼");
		
		Stream<String> stream = list.stream();
		stream.forEach(System.out::println);
		
		List<Student> list = Arrays.asList(new Student("일",90),new Student("이",92));
		
		Stream<Student> stream = list.stream();
		stream.forEach(s->{
			String name = s.getName();
			int score = s.getScore();
			System.out.println(name+"-"+score);
		});
		
		List<Integer> list = Arrays.asList(1,2,3,4,5);
		Stream<Integer> intStream = list.stream();
		
		intStream.forEach(System.out::print);
		System.out.println();
		
		Stream<String> strStream = Stream.of("a","b","c");
		Stream<String> strStream2 = Arrays.stream(new String[]{"a","b","c"});
		
		strStream.forEach(System.out::print);
		System.out.println();
		strStream2.forEach(System.out::print);
		System.out.println();
		
		IntStream intStream = IntStream.range(1,5);
		IntStream intStream2 = IntStream.rangeClosed(1, 5);
		
		intStream.forEach(System.out::print);
		System.out.println();
		intStream2.forEach(System.out::print);
		
		IntStream intStream = new Random().ints();
		intStream.limit(5).forEach(System.out::println);
		
		IntStream intStream = new Random().ints(5);
		intStream.forEach(System.out::println);
		
		IntStream intStream = new Random().ints(1, 5);
		intStream.limit(5).forEach(System.out::println);
		
		IntStream intStream = new Random().ints(5, 1, 5);
		intStream.forEach(System.out::println);
		
		Stream<Integer> evenStream = Stream.iterate(0, n->n+2);
		evenStream.limit(5).forEach(System.out::println);
		*/
		Stream<Double> randomStream = Stream.generate(Math::random);
		Stream<Integer> oneStream = Stream.generate(()->1);
		randomStream.limit(5).forEach(System.out::println);
		oneStream.limit(5).forEach(System.out::println);
	}

	/*
	static <T> List<T> doSomething(Function<T,T> f, List<T> list){
		List<T> newList = new ArrayList<T>(list.size());
		
		for(T i : list) {
			newList.add(f.apply(i));
		}
		return newList;
	}
	static <T> void printEvenNum(Predicate<T> p,Consumer<T> c,List<T> list) {
		System.out.print("[");
		for(T i:list) {
			if(p.test(i)) {
				c.accept(i);
			}
		}
		System.out.println("]");
	}
	static <T> void makeRandomList(Supplier<T> s,List<T> list) {
		for(int i=0;i<10;i++) {
			list.add(s.get());
		}
	}
	
	static void makeRandomList(IntSupplier s,int[] arr) {
		for(int i=0;i<arr.length;i++) {
			arr[i]=s.getAsInt();
		}
	}
	
	static void printEvenNum(IntPredicate p,IntConsumer c,int[] arr) {
		System.out.print("[");
		for(int i : arr) {
			if(p.test(i)) {
				c.accept(i);
			}
		}
		System.out.println("]");
	}
	
	static int[] doSomething(IntUnaryOperator op,int[] arr) {
		int[] newArr = new int[arr.length];
		
		for(int i = 0 ; i<newArr.length;i++) {
			newArr[i]=op.applyAsInt(arr[i]);
		}
		return newArr;
	}
	*/
}
class Student{
	private String name;
	private int score;
	
	Student(String name,int score){
		this.name=name;
		this.score=score;
	}
	
	String getName() {return name;}
	int getScore() {return score;}
}
