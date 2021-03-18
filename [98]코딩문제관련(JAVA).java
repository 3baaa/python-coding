package test;

import java.util.Arrays;
import java.util.Comparator;
import java.util.HashSet;
import java.util.IntSummaryStatistics;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.Set;
import java.util.stream.Collector;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;
import static java.util.stream.Collectors.*;

public class _98_코딩문제관련_JAVA {

	public static void main(String[] args) {
		/*
		List<Student98> totalList = Arrays.asList(
				new Student98("일",10,Student98.Sex.MALE),
				new Student98("이",6,Student98.Sex.FEMALE),
				new Student98("삼",10,Student98.Sex.MALE),
				new Student98("사",6,Student98.Sex.FEMALE)
				);
		
		List<Student98> maleList = totalList.stream().filter(s->s.getSex()==Student98.Sex.MALE).collect(Collectors.toList());
		maleList.stream().forEach(s->System.out.println(s.getName()));
		
		System.out.println();
		
		Set<Student98> femaleSet = totalList.stream().filter(s->s.getSex()==Student98.Sex.FEMALE).collect(Collectors.toCollection(HashSet::new));
		femaleSet.stream().forEach(s->System.out.println(s.getName()));
		*/
		/*
		int[] intArray = {1,2,3,4,5};
		
		IntStream intStream = Arrays.stream(intArray);
		intStream.asDoubleStream().forEach(System.out::println);
		
		System.out.println();
		
		intStream = Arrays.stream(intArray);
		intStream.boxed().forEach(System.out::println);
		*/
		Student98_2[] stuArr = {
				new Student98_2("이자바",3,300),
				new Student98_2("김자바",1,200),
				new Student98_2("안자바",2,100),
				new Student98_2("박자바",2,150),
				new Student98_2("소자바",1,200),
				new Student98_2("나자바",3,290),
				new Student98_2("감자바",3,180)
		};
		
		List<String> names = Stream.of(stuArr).map(Student98_2::getName).collect(Collectors.toList());
		System.out.println(names);
		
		Student98_2[] stuArr2 = Stream.of(stuArr).toArray(Student98_2[]::new);
		
		for(Student98_2 s : stuArr2) {
			System.out.println(s);
		}
		
		Map<String,Student98_2> stuMap = Stream.of(stuArr).collect(Collectors.toMap(s->s.getName(), p->p));
		
		for(String name : stuMap.keySet()) {
			System.out.println(name+"-"+stuMap.get(name));
		}
		
		long count = Stream.of(stuArr).collect(counting());
		long totalScore = Stream.of(stuArr).collect(summingInt(Student98_2::getTotalScore));
		
		System.out.println("count="+count);
		System.out.println("totalScore="+totalScore);
		
		totalScore = Stream.of(stuArr).collect(reducing(0,Student98_2::getTotalScore,Integer::sum));
		System.out.println("totalScore="+totalScore);
		
		Optional<Student98_2> topStudent = Stream.of(stuArr).collect(maxBy(Comparator.comparingInt(Student98_2::getTotalScore)));
		
		System.out.println("topStudent="+topStudent.get());
		
		IntSummaryStatistics stat = Stream.of(stuArr).collect(summarizingInt(Student98_2::getTotalScore));
		System.out.println(stat);
		String stuNames = Stream.of(stuArr).map(Student98_2::getName).collect(joining(",","{","}"));
		System.out.println(stuNames);
	}

}
/*
class Student98{
	public enum Sex{MALE,FEMALE}
	public enum City{Seoul,Pusan}
	
	private String name;
	private int score;
	private Sex sex;
	private City city;
	
	public Student98(String name,int score,Sex sex) {
		this.name=name;
		this.score=score;
		this.sex=sex;
	}
	
	public Student98(String name,int score,Sex sex,City city) {
		this.name=name;
		this.score=score;
		this.sex=sex;
		this.city=city;
	}

	public String getName() {
		return name;
	}

	public int getScore() {
		return score;
	}

	public Sex getSex() {
		return sex;
	}

	public City getCity() {
		return city;
	}
}
*/
class Student98_2{
	String name;
	int ban;
	int totalScore;
	
	Student98_2(String name,int ban,int totalScore){
		this.name=name;
		this.ban=ban;
		this.totalScore=totalScore;
	}
	
	public String toString() {
		return String.format("[%s, %d, %d]", name,ban,totalScore).toString();
	}
	
	public String getName() {
		return name;
	}

	public int getBan() {
		return ban;
	}

	public int getTotalScore() {
		return totalScore;
	}
	
	public int compareTo(Student98_2 s) {
		return s.totalScore-this.totalScore;
	}
}
