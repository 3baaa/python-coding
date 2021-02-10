##코딩테스트 관련##
'''
##투 포인터 1 ##
n=5
m=5
data=[1,2,3,2,5]

count=0
interval_sum=0
end=0

for start in  range(n):
    while interval_sum<m and end<n:
        interval_sum+=data[end]
        end+=1
    if interval_sum==m:
        count+=1
    interval_sum-=data[start]

print(count)

##투 포인터 2 ##
n,m=3,4
a=[1,3,5]
b=[2,4,6,8]

result=[0]*(n+m)
i=0
j=0
k=0

while i<n or j<m:
    if j>=m or (i<n and a[i]<=b[j]):
        result[k]=a[i]
        i+=1
    else:
        result[k]=b[j]
        j+=1
    k+=1

for i in result:
    print(i,end=' ')

##구간 합 계산##
n=5
data=[10,20,30,40,50]

sum_value=0
prefix_sum=[0]
for i in data:
    sum_value+=i
    prefix_sum.append(sum_value)

left=3
right=4
print(prefix_sum[right]-prefix_sum[left-1])

##순열과 조합##
import itertools

data=[1,2]

for x in itertools.permutations(data,2):
    print(list(x))

for x in itertools.combinations(data,2):
    print(list(x))

##---------------------##

##코딩테스트 문제##
##소수 구하기##
#내가쓴 코드#
#(결과값이 나온다 하지만 범위를 잘못했다)#
import math

m,n=map(int,input().split())
r=[True]*(n+1)

for i in range(2,int(math.sqrt(n))):## math.sqrt(n)+1을해야한다
    j=2
    while i*j<=n:
        r[i*j]=False
        j+=1

for i in range(m,n+1):
    if r[i]:
        print(i)

##암호 만들기##
#내가쓴 코드#
#(결과값이 나온다)#
from itertools import combinations

l,c=map(int,input().split())
a=list(input().split())
c=['a','e','i','o','u']
result=[]

a.sort()
r=list(combinations(a,l))
print(r)
for i in r:
    t=''
    t2=0
    t3=0
    for j in i:
        t+=j
    for j in t:
        if j in c:
            t2+=1
        else:
            t3+=1
    if t2>0 and t3>1:
        result.append(t)

for i in result:
    print(i)
'''
