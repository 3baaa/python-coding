package test;

import java.util.*;

/*
 * 무지의 먹방 라이브
 */
public class _115_코딩문제_JAVA_무지의먹방라이브 {

	
	/*
	 * 내가쓴 코드(잘못쓴 코드)
	 * 정확성: 6.7
	 * 효율성: 7.1
	 * 합계: 13.8 / 100.0

	class Solution {
	    public int solution(int[] food_times, long k) {
	        int answer = 0;
	        int food_l=food_times.length;
	        long n1=k/food_l;
	        long n2=k%food_l;
	        for(int i=0;i<food_l;i++){
	            food_times[i]-=n1;
	            if(food_times[i]>0){
	                n2-=1;
	            }
	            if(n2==0){
	                answer=(i+1)%food_l+1;
	            }
	        }
	        return answer;
	    }
	}
	*/
	
	//답
	class Food implements Comparable<Food> {

	    private int time;
	    private int index;

	    public Food(int time, int index) {
	        this.time = time;
	        this.index = index;
	    }

	    public int getTime() {
	        return this.time;
	    }

	    public int getIndex() {
	        return this.index;
	    }

	    @Override
	    public int compareTo(Food other) {
	        return Integer.compare(this.time, other.time);
	    }
	}

	class Solution {
	    public int solution(int[] food_times, long k) {
	        long summary = 0;
	        for (int i = 0; i < food_times.length; i++) {
	            summary += food_times[i];
	        }
	        if (summary <= k) return -1;

	        PriorityQueue<Food> pq = new PriorityQueue<>();
	        for (int i = 0; i < food_times.length; i++) {
	            pq.offer(new Food(food_times[i], i + 1));
	        }

	        summary = 0;
	        long previous = 0;
	        long length = food_times.length;

	        while (summary + ((pq.peek().getTime() - previous) * length) <= k) {
	            int now = pq.poll().getTime();
	            summary += (now - previous) * length;
	            length -= 1;
	            previous = now;
	        }

	        ArrayList<Food> result = new ArrayList<>();
	        while (!pq.isEmpty()) {
	            result.add(pq.poll());
	        }

	        Collections.sort(result, new Comparator<Food>() { 
	            @Override
	            public int compare(Food a, Food b) {
	                return Integer.compare(a.getIndex(), b.getIndex());
	            }
	        });
	        return result.get((int) ((k - summary) % length)).getIndex();
	    }
	}
}
