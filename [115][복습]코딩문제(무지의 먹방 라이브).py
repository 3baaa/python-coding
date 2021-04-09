##무지의 먹방 라이브
#내가쓴 코드(잘못쓴 코드)
'''
정확성: 6.7
효율성: 7.1
합계: 13.8 / 100.0
'''
def solution(food_times, k):
    answer = 0
    food_l=len(food_times)
    n1=k//food_l
    n2=k%food_l
    for i in range(food_l):
        food_times[i]-=n1
        if food_times[i]>0:
            n2-=1
        if n2==0:
            answer=(i+1)%food_l+1
    return answer

#답#
import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))  

    sum_value = 0
    previous = 0
    length = len(food_times)

    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now

    result = sorted(q, key=lambda x: x[1])
    return result[(k - sum_value) % length][1]
