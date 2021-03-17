package test;

import java.util.Arrays;
import java.util.List;
import java.util.Optional;
import java.util.OptionalInt;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class _97_코딩문제관련_JAVA {

	public static void main(String[] args) {
		/*
		String str=null;
		Optional.ofNullable(str).ifPresent(System.out::println);
		
		Optional<String> optStr = Optional.of("abcde");
		Optional<Integer> optInt = optStr.map(String::length);
		System.out.println("optStr="+optStr.get());
		System.out.println("optInt="+optInt.get());
		
		int result1 = Optional.of("123").filter(x->x.length()>0).map(Integer::parseInt).get();
		int result2 = Optional.of("").filter(x->x.length()>0).map(Integer::parseInt).orElse(-1);
		System.out.println("result1="+result1);
		System.out.println("result2="+result2);
		
		Optional.of("456").map(Integer::parseInt).ifPresent(x->System.out.printf("result3=%d\n", x));
		
		OptionalInt optInt1 = OptionalInt.of(0);
		OptionalInt optInt2 = OptionalInt.empty();
		
		System.out.println(optInt1.isPresent());
		System.out.println(optInt2.isPresent());
		
		System.out.println(optInt1.getAsInt());
		//System.out.println(optInt2.getAsInt());
		System.out.println("optInt1="+optInt1);
		System.out.println("optInt2="+optInt2);
		System.out.println("optInt1.equals(optInt2)="+optInt1.equals(optInt2));
		
		Optional<String> opt = Optional.ofNullable(null);
		Optional<String> opt2 = Optional.empty();
		System.out.println("opt = "+opt);
		System.out.println("opt2 = "+opt2);
		System.out.println("opt.equals(opt2) = "+opt.equals(opt2));
		
		int result3 = optStrToInt(Optional.of("123"),0);
		int result4 = optStrToInt(Optional.of(""),0);
		
		System.out.println("result3="+result3);
		System.out.println("result4="+result4);
		
		int[] intArr = {2,4,6};
		
		boolean result = Arrays.stream(intArr).allMatch(a->a%2==0);
		System.out.println("모두 2의 배수인가? "+result);
		
		result=Arrays.stream(intArr).anyMatch(a->a%3==0);
		System.out.println("하나라도 3의 배수가 있는가? "+result);
		
		result=Arrays.stream(intArr).noneMatch(a->a%3==0);
		System.out.println("3의 배수가 없는가? "+result);
		
		List<Student97> studentList = Arrays.asList(
				new Student97("일",92),
				new Student97("이",95),
				new Student97("삼",88)
				);
		
		int sum1 = studentList.stream().mapToInt(Student97::getScore).sum();
		int sum2 = studentList.stream().map(Student97::getScore).reduce((a,b)->a+b).get();
		int sum3 = studentList.stream().map(Student97::getScore).reduce(0, (a,b)->a+b);
		
		System.out.println("sum1:"+sum1);
		System.out.println("sum2:"+sum2);
		System.out.println("sum3:"+sum3);
		*/
		String[] strArr = {
				"Inheritance","Java","Lambda","stream",
				"OptionalDouble","IntStream","count","sum"
		};
		
		Stream.of(strArr).forEach(System.out::println);
		
		boolean noEmptyStr = Stream.of(strArr).noneMatch(s->s.length()==0);
		Optional<String> sWord = Stream.of(strArr).filter(s->s.charAt(0)=='s').findFirst();
		System.out.println("noEmptyStr="+noEmptyStr);
		System.out.println("sWord="+sWord.get());
		
		IntStream intStream1 = Stream.of(strArr).mapToInt(String::length);
		IntStream intStream2 = Stream.of(strArr).mapToInt(String::length);
		IntStream intStream3 = Stream.of(strArr).mapToInt(String::length);
		IntStream intStream4 = Stream.of(strArr).mapToInt(String::length);
		int count = intStream1.reduce(0, (a,b)->a+1);
		int sum = intStream2.reduce(0, (a,b)->a+b);
		
		OptionalInt max = intStream3.reduce(Integer::max);
		OptionalInt min = intStream4.reduce(Integer::min);
		System.out.println("count="+count);
		System.out.println("sum="+sum);
		System.out.println("max="+max.getAsInt());
		System.out.println("min="+min.getAsInt());
	}

	static int optStrToInt(Optional<String> optStr,int defaultValue) {
		try {
			return optStr.map(Integer::parseInt).get();
		} catch (Exception e) {
			return defaultValue;
		}
	}
	
}

class Student97{
	private String name;
	private int score;
	
	public Student97(String name,int score) {
		this.name=name;
		this.score=score;
	}
	
	public String getName(){return name;}
	public int getScore() {return score;}
}
