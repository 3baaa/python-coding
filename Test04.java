package upload.new_upload;

/*
 * 아르바이트,판매사원
 * 빈칸 채우기
 * 결과 = 정확성: 100.0 합계: 100.0 / 100.0
 */
public class Test04 {
	class Solution {
	    class Job {
	        public int salary;

	        public Job() {
	            this.salary = 0;
	        }

	        public int getSalary() {
	            return salary;
	        }
	    }

	    class PartTimeJob extends Job{
	        public int workHour, payPerHour;

	        public PartTimeJob(int workHour, int payPerHour) {
	            this.workHour = workHour;
	            this.payPerHour = payPerHour;
	        }

	        public int getSalary(){
	            salary = workHour * payPerHour;
	            if(workHour >= 40)
	                salary += (payPerHour * 8);

	            return salary;
	        }
	    }
	    }
}
