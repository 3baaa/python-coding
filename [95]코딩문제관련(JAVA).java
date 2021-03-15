package test;

import java.io.File;
import java.util.Arrays;
import java.util.Comparator;
import java.util.IntSummaryStatistics;
import java.util.List;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class _95_코딩문제관련_JAVA {

	public static void main(String[] args) {
		/*
		Stream emptyStream = Stream.empty();
		System.out.println(emptyStream.count());
		
		String[] str1 = {"123","456","789"};
		String[] str2 = {"ABC","abc","DEF"};
		
		Stream<String> strs1 = Stream.of(str1);
		Stream<String> strs2 = Stream.of(str2);
		Stream<String> strs3 = Stream.concat(strs1, strs2);
		strs3.forEach(System.out::println);
		
		IntStream intStream = IntStream.rangeClosed(1, 10);
		intStream.skip(3).limit(5).forEach(System.out::println);
		
		IntStream intStream = IntStream.of(1,2,2,3,3,3,4,5,5,6);
		intStream.distinct().forEach(System.out::print);
		
		IntStream intStream =IntStream.rangeClosed(1, 10);
		//intStream.filter(i->i%2==0).forEach(System.out::print);
		//intStream.filter(i->i%2!=0 && i%3!=0).forEach(System.out::print);
		intStream.filter(i->i%2!=0).filter(i->i%3!=0).forEach(System.out::print);
		
		Stream<String> strStream = Stream.of("dd","aaa","CC","cc","b");
		//strStream.sorted().forEach(System.out::print);
		strStream.sorted(Comparator.reverseOrder()).forEach(System.out::print);
		
		Stream<Student95> studentStream = Stream.of(
				new Student95("이자바",3,300),
				new Student95("김자바",1,200),
				new Student95("안자바",2,100),
				new Student95("박자바",2,150),
				new Student95("소자바",1,200),
				new Student95("나자바",3,290),
				new Student95("감자바",3,180)
				);
		
		studentStream.sorted(Comparator.comparing(Student95::getBan).thenComparing(Comparator.naturalOrder())).forEach(System.out::println);
		
		File[] fileArr = {
				new File("Ex1.java"),
				new File("ex1.bak"),
				new File("Ex2.java"),
				new File("Ex1"),
				new File("Ex1.txt")
		};
		Stream<File> fileStream = Stream.of(fileArr);
		Stream<String> filenameStream = fileStream.map(File::getName);
		filenameStream.forEach(System.out::println);
		
		fileStream = Stream.of(fileArr);
		
		fileStream.map(File::getName).filter(s->s.indexOf('.')!=-1).map(s->s.substring(s.indexOf('.')+1)).map(String::toUpperCase).distinct().forEach(System.out::println);
		System.out.println();
		
		List<S95> studentList = Arrays.asList(
				new S95("일",10),
				new S95("이",20),
				new S95("삼",30)
				);
		
		studentList.stream().mapToInt(S95::getScore).forEach(System.out::println);
		*/
		Student95[] stuArr = {
				new Student95("이자바",3,300),
				new Student95("김자바",1,200),
				new Student95("안자바",2,100),
				new Student95("박자바",2,150),
				new Student95("소자바",1,200),
				new Student95("나자바",3,290),
				new Student95("감자바",3,180)
		};
		
		Stream<Student95> stuStream = Stream.of(stuArr);
		
		stuStream.sorted(Comparator.comparing(Student95::getBan).thenComparing(Comparator.naturalOrder())).forEach(System.out::println);
		
		stuStream = Stream.of(stuArr);
		IntStream stuScoreStream = stuStream.mapToInt(Student95::getTotalScore); 
		
		IntSummaryStatistics stat = stuScoreStream.summaryStatistics();
		System.out.println("count="+stat.getCount());
		System.out.println("sum="+stat.getSum());
		System.out.printf("average=%.2f%n",stat.getAverage());
		System.out.println("min="+stat.getMin());
		System.out.println("max="+stat.getMax());
	}
}

class Student95 implements Comparable<Student95>{
	
	String name;
	int ban;
	int totalScore;
	public Student95(String name,int ban,int totalScore) {
		this.name=name;
		this.ban=ban;
		this.totalScore=totalScore;
	}
	
	public String toString() {
		return String.format("[%s, %d, %d]", name,ban,totalScore);
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

	@Override
	public int compareTo(Student95 s) {
		return s.totalScore-this.totalScore;
	}
	
}

/*
class S95{
	private String name;
	private int score;
	
	public S95(String name,int score) {
		this.name=name;
		this.score=score;
	}
	
	public String getName() {return name;}
	public int getScore() {return score;}
}
*/