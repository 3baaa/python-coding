##볼링공 고르기##
'''
#내가쓴 코드#
from itertools import combinations

n,m=map(int,input().split())
k=list(map(int,input().split()))

result=list(combinations(k,2))
result = [i for i in result if i[0]!=i[1]]
print(len(result))

##무지의 먹방 라이브##
#내가쓴 코드#
def solution(food_times, k):
    answer = 0
    t=0
    c=0
    while k>0:
        if c==len(food_times):
            answer=-1
            return answer
            break
        elif food_times[t]!=0:
            food_times[t]-=1
            c=0
        elif food_times[t]==0:
            t=(t+1)%len(food_times)
            c+=1
            continue
        t=(t+1)%len(food_times)
        k-=1
        
    answer=(t+1)%len(food_times)
    return answer

#답#
import heapq

def solution(food_times, k):

    if sum(food_times)<=k:
        return -1

    q = list()

    for i in range(len(food_times)):
        heapq.heappush(q,(food_times[i],i+1))

    sum_value = 0
    prev =0
    length = len(food_times)

    while (sum_value + (q[0][0]-prev)*length)<=k:

        now = heapq.heappop(q)[0]
        sum_value += (now-prev)*length
        length -= 1
        prev = now

    result = sorted(q,key = lambda x: x[1])
    return result[(k-sum_value)%length][1]
'''