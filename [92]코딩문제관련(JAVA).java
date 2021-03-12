package test;

import java.util.Arrays;
import java.util.List;
import java.util.Random;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class _92_코딩문제관련_JAVA {

	public static void main(String[] args) {
		/*
		int[] arr = new int[5];
		Arrays.setAll(arr, (i)->(int)(Math.random()*5)+1);
		System.out.println(Arrays.toString(arr));
		*/
		/*
		List<Integer> list = Arrays.asList(1,2,3,4,5);
		Stream<Integer> intStream = list.stream();
		intStream.forEach(System.out::print);
		System.out.println();
		
		Stream<String> strStream = Stream.of("a","b","c");
		Stream<Integer> intS = Stream.of(1,2);
		Stream<String> strStream2 = Stream.of(new String[] {"a","b","c"});
		strStream.forEach(System.out::print);
		System.out.println();
		intS.forEach(System.out::print);
		System.out.println();
		strStream2.forEach(System.out::print);
		System.out.println();
		
		IntStream intStream2 = IntStream.of(1,2,3);
		IntStream intStream3 = Arrays.stream(new int[] {1,2,3});
		intStream2.forEach(System.out::print);
		System.out.println();
		intStream3.forEach(System.out::print);
		*/
		/*
		IntStream intStream = IntStream.range(1, 5);
		intStream.forEach(System.out::print);
		IntStream intStream2 = IntStream.rangeClosed(1, 5);
		System.out.println();
		intStream2.forEach(System.out::print);
		*/
		/*
		IntStream intStream = new Random().ints(5, 1, 100);
		IntStream intStream2 = new Random().ints(1,100);
		intStream.forEach(System.out::println);
		System.out.println();
		intStream2.limit(5).forEach(System.out::println);
		*/
	}

}
