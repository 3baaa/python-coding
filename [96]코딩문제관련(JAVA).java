package test;

import java.util.Arrays;
import java.util.Optional;
import java.util.Random;
import java.util.stream.DoubleStream;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class _96_코딩문제관련_JAVA {

	public static void main(String[] args) {
		/*
		IntStream intStream = new Random().ints(1,46);
		Stream<String> lottoStream = intStream.distinct().limit(6).sorted().mapToObj(i->i+",");
		lottoStream.forEach(System.out::print);
		
		Stream<String[]> strArrStrm = Stream.of(
				new String[] {"abc","def","ghi"},
				new String[] {"ABC","GHI","JKLMN"}
				);
		
		Stream<String> strStrStrm = strArrStrm.flatMap(Arrays::stream);
		strStrStrm.forEach(System.out::println);
		
		String[] lineArr = {
				"Belive or not It is true",
				"Do or do not There is no try",
		};
		
		Stream<String> lineStream = Arrays.stream(lineArr);
		lineStream.forEach(System.out::println);
		Stream<String> strArrStream = lineStream.flatMap(line->Stream.of(line.split(" +")));
		strArrStream.forEach(System.out::println);
		
		Stream<String> strStrm = Stream.of("abc","def","jklmn");
		Stream<String> strStrm2 = Stream.of("ABC","GHI","JKLMN");
		
		Stream<Stream<String>> strmStrm = Stream.of(strStrm,strStrm2);
		
		Stream<String> strStream = strmStrm.map(s->s.toArray(String[]::new)).flatMap(Arrays::stream);
		strStream.forEach(System.out::println);
		
		Stream<String[]> strArrStrm = Stream.of(
				new String[] {"abc","def","ghi"},
				new String[] {"ABC","GHI","JKLMN"}
				);
		
		Stream<String> strStrm = strArrStrm.flatMap(Arrays::stream);
		
		strStrm.map(String::toLowerCase).distinct().sorted().forEach(System.out::println);
		System.out.println();
		
		String[] lineArr = {
				"Belive or not It is true",
				"Do or do not There is no try",
		};
		
		Stream<String> lineStream = Arrays.stream(lineArr);
		lineStream.flatMap(line->Stream.of(line.split(" +"))).map(String::toLowerCase).distinct().sorted().forEach(System.out::println);
		System.out.println();
		
		Stream<String> strStrm1 = Stream.of("AAA","ABC","bBb","Dd");
		Stream<String> strStrm2 = Stream.of("bbb","aaa","ccc","dd");
		
		Stream<Stream<String>> strStrmStrm = Stream.of(strStrm1,strStrm2);
		Stream<String> strStream = strStrmStrm.map(s->s.toArray(String[]::new)).flatMap(Arrays::stream);
		strStream.map(String::toLowerCase).distinct().forEach(System.out::println);
		
		//Optional<String> optVal = Optional.of("abc");
		//System.out.println(optVal.get());
		Optional<String> optVal = Optional.empty();
		//System.out.println(optVal.orElse(""));
		System.out.println(optVal.orElseGet(()->"x"));
		*/
		int result = Optional.of("123").filter(x->x.length()>0).map(Integer::parseInt).orElse(-1);
		System.out.println(result);
 	}
}
