##특정 거리의 도시 찾기##
'''
#내가쓴 코드#
#(결과값이 나온다)#
from collections import deque

def bb(x):
    q=deque([x])
    t[x[0]]=0
    while q:
        n=q.popleft()
        for i in z[n[0]]:
            if t[i]>n[1]+1:
                t[i]=n[1]+1
            q.append([i,n[1]+1])
            
n,m,k,x=map(int,input().split())
z=[[] for _ in range(n+1)]
t=[int(1e9)]*(n+1)
for i in range(m):
    a,b=map(int,input().split())
    z[a].append(b)

bb([x,0])
c=0
for i,v in enumerate(t[1:],start=1):
    if v==k:
        print(i)
        c+=1
if c==0:
    print(-1)

##연구소##
#내가쓴 코드#
#(결과값이 나온다)#
from itertools import combinations
from collections import deque
import copy

def ch(t):
    c=0
    for i in t:
        for j in i:
            if j==0:
                c+=1
    return c

def bb(i,t):
    q=deque(two)
    for j in i:
        t[j[0]][j[1]]=1
    while q:
        x,y=q.popleft();
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<m and t[nx][ny]==0:
                t[nx][ny]=2
                q.append([nx,ny])
    return ch(t)
n,m=map(int,input().split())
a=[]
z=[]
two=[]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
for i in range(n):
    t=list(map(int,input().split()))
    for j,v in enumerate(t):
        if v==0:
            z.append([i,j])
        elif v==2:
            two.append([i,j])
    a.append(t)

z=list(combinations(z,3))
r=0
for i in z:
    t=copy.deepcopy(a)
    r=max(r,bb(i,t))
print(r)
'''
