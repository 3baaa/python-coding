package test;

import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.Set;
import java.util.stream.Collectors;
import java.util.function.Function;
import java.util.stream.Collector;
import java.util.stream.Stream;
import static java.util.stream.Collectors.*;
import static java.util.Comparator.*;

public class _99_코딩문제관련_JAVA {

	public static void main(String[] args) {
		/*
		List<Student99> totalList = Arrays.asList(
				new Student99("일",10,Student99.Sex.MALE,Student99.City.Seoul),
				new Student99("이",6,Student99.Sex.FEMALE,Student99.City.Pusan),
				new Student99("삼",10,Student99.Sex.MALE,Student99.City.Pusan),
				new Student99("사",6,Student99.Sex.FEMALE,Student99.City.Seoul)
				);
		
		Map<Student99.Sex, List<Student99>> mapBySex = totalList.stream().collect(Collectors.groupingBy(Student99::getSex));
		System.out.println("[남학생]");
		mapBySex.get(Student99.Sex.MALE).stream().forEach(s->System.out.print(s.getName()+" "));
		
		System.out.println("\n[여학생]");
		mapBySex.get(Student99.Sex.FEMALE).stream().forEach(s->System.out.print(s.getName()+" "));
		
		System.out.println();
		
		Map<Student99.City,List<String>> mapByCity = totalList.stream().collect(Collectors.groupingBy(
				Student99::getCity,Collectors.mapping(Student99::getName, Collectors.toList())
				));
		
		System.out.print("\n[서울]");
		mapByCity.get(Student99.City.Seoul).stream().forEach(s->System.out.print(s+" "));
		
		System.out.print("\n[부산]");
		mapByCity.get(Student99.City.Pusan).stream().forEach(s->System.out.print(s+" "));
		*/
		Stream<Student99_2> stuStream = Stream.of(
				new Student99_2("나자바",true,1,1,300),
				new Student99_2("김지미",false,1,1,250),
				new Student99_2("김자바",true,1,1,200),
				new Student99_2("이지미",false,1,2,150),
				new Student99_2("남자바",true,1,2,100),
				new Student99_2("안지미",false,1,2,50),
				new Student99_2("황지미",false,1,3,100),
				new Student99_2("강지미",false,1,3,150),
				new Student99_2("이바자",true,1,3,200),
				
				new Student99_2("나자바",true,2,1,300),
				new Student99_2("김지미",false,2,1,250),
				new Student99_2("김자바",true,2,1,200),
				new Student99_2("이지미",false,2,2,150),
				new Student99_2("남자바",true,2,2,100),
				new Student99_2("안지미",false,2,2,50),
				new Student99_2("황지미",false,2,3,100),
				new Student99_2("강지미",false,2,3,150),
				new Student99_2("이바자",true,2,3,200)
				);
		/*
		Map<Boolean,List<Student99_2>> stuBySex = stuStream.collect(Collectors.partitioningBy(Student99_2::isMale));
		List<Student99_2> maleStudent = stuBySex.get(true);
		List<Student99_2> femaleStudent = stuBySex.get(false);
		
		Map<Boolean,Long> stuNumBySex = stuStream.collect(partitioningBy(Student99_2::isMale,counting()));
		System.out.println("남학생 수 : "+stuNumBySex.get(true));
		System.out.println("여학생 수 : "+stuNumBySex.get(false));
		
		Map<Boolean,Long> stuNumBySex = stuStream.collect(partitioningBy(Student99_2::isMale,summingLong(Student99_2::getScore)));

		Map<Boolean,Optional<Student99_2>> topScoreBySex = stuStream.collect(
				partitioningBy(Student99_2::isMale,maxBy(comparingInt(Student99_2::getScore)))
				);
		System.out.println("남학생 1등 : "+topScoreBySex.get(true));
		System.out.println("여학생 1등 : "+topScoreBySex.get(false));
		
		Map<Boolean,Student99_2> topScoreBySex = stuStream.collect(partitioningBy(Student99_2::isMale,collectingAndThen(maxBy(comparingInt(Student99_2::getScore)),Optional::get)));
		System.out.println("남학생 1등 : "+topScoreBySex.get(true));
		System.out.println("여학생 1등 : "+topScoreBySex.get(false));

		Map<Boolean,Map<Boolean,List<Student99_2>>> failedStuBySex = stuStream.collect(partitioningBy(Student99_2::isMale,partitioningBy(s->s.getScore()<150)));
		List<Student99_2> failedMaleStu = failedStuBySex.get(true).get(true);
		List<Student99_2> failedFemaleStu = failedStuBySex.get(false).get(true);
		
		failedMaleStu.stream().forEach(System.out::print);
		System.out.println();
		failedFemaleStu.stream().forEach(System.out::print);
		
		Map<Student99_2.Level,Long> stuByLevel = stuStream.collect(groupingBy(s->{
			if(s.getScore() >= 200) return Student99_2.Level.HIGH;
			else if(s.getScore() >= 100) return Student99_2.Level.MID;
			else return Student99_2.Level.LOW;
			}, counting()));
		
		for(Student99_2.Level key : stuByLevel.keySet()) {
			System.out.print("["+key+"]="+stuByLevel.get(key));
			System.out.println();
		}
		
		Map<Integer,Map<Integer,List<Student99_2>>> stuByHakAndBan = stuStream.collect(groupingBy(Student99_2::getHak,groupingBy(Student99_2::getBan)));
		
		for(Map<Integer, List<Student99_2>> hak : stuByHakAndBan.values()) {
			for(List<Student99_2> ban : hak.values()) {
				System.out.println();
				for(Student99_2 s : ban) {
					System.out.println(s);
				}
			}
		}
		
		Map<Integer,Map<Integer,Student99_2>> topStuByHakAndBan = stuStream.collect(groupingBy(Student99_2::getHak,groupingBy(Student99_2::getBan,collectingAndThen(maxBy(comparingInt(Student99_2::getScore)), Optional::get))));
		for(Map<Integer,Student99_2> ban : topStuByHakAndBan.values()) {
			for(Student99_2 s : ban.values()) {
				System.out.println(s);
			}
		}
		*/
	}
}
/*
class Student99{
	public enum Sex{MALE,FEMALE}
	public enum City{Seoul,Pusan}
	
	private String name;
	private int score;
	private Sex sex;
	private City city;
	
	public Student99(String name,int score,Sex sex) {
		this.name=name;
		this.score=score;
		this.sex=sex;
	}
	
	public Student99(String name,int score,Sex sex,City city) {
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
class Student99_2{
	String name;
	boolean isMale;
	int hak;
	int ban;
	int score;
	
	Student99_2(String name,boolean isMale,int hak,int ban,int score){
		this.name=name;
		this.isMale=isMale;
		this.hak=hak;
		this.ban=ban;
		this.score=score;
	}

	public String getName() {
		return name;
	}

	public boolean isMale() {
		return isMale;
	}

	public int getHak() {
		return hak;
	}

	public int getBan() {
		return ban;
	}

	public int getScore() {
		return score;
	}
	
	public String toString() {
		return String.format("[%s, %s, %d학번, %d반, %3d점]", name,isMale?"남":"여",hak,ban,score);
	}
	
	enum Level{HIGH,MID,LOW}
}