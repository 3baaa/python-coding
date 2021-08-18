package upload;

/*
 * 양념 반 후라이드 반
 * 내가쓴 코드
 * 결과 = 맞았습니다
 */

import java.util.*;

public class backjoon_16917 {
	public static void main(String[] args) {
		int[] arr = new int[5];
		Scanner sc =new Scanner(System.in);
		for(int i=0;i<5;i++) {
			arr[i]=sc.nextInt();
		}
			
		int[] price = Arrays.copyOf(arr, 3);
		int[] amount = Arrays.copyOfRange(arr, 3,arr.length);
		int total = check_price(price,amount);
			
		for(int i=2;;i+=2) {
			amount[0]-=1;
			amount[1]-=1;
			if(amount[0]<0 && amount[1]<0) {
				break;
			}
			int t_price = (price[2]*i)+check_price(price,amount);
			if(t_price<total) {
				total=t_price;
			}
		}
			
		System.out.println(total);
	}

	public static int check_price(int[] price,int[] amount) {
		if(amount[0]<0) {
			return price[1]*amount[1];
		}else if(amount[1]<0) {
			return price[0]*amount[0];
		}
		return price[0]*amount[0]+price[1]*amount[1];
	}
}
