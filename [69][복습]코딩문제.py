##모험가 길드##
'''
#내가쓴 코드#
#(결과값이 나온다)#
n=int(input())
a=list(map(int,input().split()))

a.sort()

r=0
c=0
for i in a:
    c+=1
    if c==i:
        r+=1
        c=0
        
print(r)

##곱하기 혹은 더하기##
#내가쓴 코드#
#(잘못쓴코드 = 숫자가 1일때를 조건으로 못넣었다)#
from collections import deque

s=input()
s=list(map(int,s))

a=deque()

for i in s:
    a.append(i)
    if len(a)==2:
        n1=a.popleft()
        n2=a.popleft()
        if n1==0 or n2==0 :## or n1==1 or n2==1 코드를 추가로 써야한다 
            a.append(n1+n2)
        else:
            a.append(n1*n2)

print(a.popleft())

##문자열 뒤집기##
#내가쓴 코드#
#(결과값이 나온다)#
s=input()

t=''
n1=0
n2=0
for i in s:
    if t!=i:
        if i=='0':
            n1+=1
        else:
            n2+=1
        t=i
print(min(n1,n2))

##만들 수 없는 금액##
#내가쓴 코드#
#(잘못쓴 코드)#
n=int(input())
a=list(map(int,input().split()))

a.sort()

#답#
n=int(input())
data=list(map(int,input().split()))
data.sort()

target=1
for x in data:
    if target<x:
        break
    target+=x

print(target)

##볼링공 고르기##
#내가쓴 코드#
#(결과값이 나온다)#
from itertools import combinations
n,m=map(int,input().split())
a=list(map(int,input().split()))

a=list(combinations(a,2))
r=[]
for i in a:
    if i[0]!=i[1]:
        r.append(i)
print(len(r))

##무지의 먹방 라이브##
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
'''
