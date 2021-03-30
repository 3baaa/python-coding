##숨바꼭질
#내가쓴 코드
#결과값이 나온다

import heapq

def b():
    q=[]
    heapq.heappush(q,(0,1))
    while q:
        d,n3=heapq.heappop(q)

        if r[n3]<d:
            continue
        for i in a[n3]:
            if r[i]>d+1:
                heapq.heappush(q,(d+1,i))
                r[i]=d+1

n,m=map(int,input().split())

a=[[] for _ in range(n+1)]
r=[int(1e9)]*(n+1)
r[1]=0

for _ in range(m):
    n1,n2=map(int,input().split())
    a[n1].append(n2)
    a[n2].append(n1)

b()

rr=max(r[1:])
print(r.index(rr), rr, r.count(rr))

