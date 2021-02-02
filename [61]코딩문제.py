##화성 탐사##
'''
#내가쓴 코드#
#(결과값이 나온다)#
import heapq

def dd(s):
    q=[]
    heapq.heappush(q,(s,(0,0)))
    while q:
        dist,xy=heapq.heappop(q)
        x=xy[0]
        y=xy[1]
        if a2[x][y]<dist:
            continue
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<N and nx>-1 and ny<N and ny>-1:
                cost=dist+a[nx][ny]
                if cost<a2[nx][ny]:
                    a2[nx][ny]=cost
                    heapq.heappush(q,(cost,(nx,ny)))
    return a2[N-1][N-1]
           
T=int(input())

dx=[-1,1,0,0]
dy=[0,0,-1,1]
result=[]

for _ in range(T):
    N=int(input())
    a=[]
    for i in range(N):
        a.append(list(map(int,input().split())))
    a2=[[int(1e9)]*N for _ in range(N)]
    result.append(dd(a[0][0]))

for i in result:
    print(i)

##숨바꼭질##
#내가쓴 코드#
#(결과값이 나온다)#
import heapq

def dd():
    q=[]
    heapq.heappush(q,(0,1))
    d[1]=0
    while q:
        dist,now=heapq.heappop(q)
        if d[now]<dist:
            continue
        for i in a[now]:
            cost=dist+i[1]
            if d[i[0]]>cost:
                d[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

N,M=map(int,input().split())
a=[[] for _ in range(N+1)]
d=[int(1e9)]*(N+1)
for i in range(M):
    x,y=map(int,input().split())
    a[x].append([y,1])
    a[y].append([x,1])

dd()
big=max(d[1:])
idd=d.index(big)
print(idd,d[idd],d.count(big))
'''
