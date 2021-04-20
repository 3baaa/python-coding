##DFS와 BFS
#내가쓴 코드
from collections import deque
def dfs(v):
    if v1[v]:
        return
    v1[v]=True
    r1.append(v)
    for i in a[v]:
        dfs(i)
    
def bfs(v):
    q=deque([v])
    v2[v]=True
    while q:
        n1=q.popleft()
        r2.append(n1)
        for i in a[n1]:
            if not v2[i]:
                q.append(i)
                v2[i]=True

n,m,v=map(int,input().split())
a=[[] for _ in range(n+1)]
v1=[False]*(n+1)
v2=[False]*(n+1)

r1=[]
r2=[]
for _ in range(m):
    n1,n2=map(int,input().split())
    a[n1].append(n2)
    a[n2].append(n1)
    
for i in range(n+1):
    a[i].sort()

dfs(v)
bfs(v)
for i in r1:
    print(i,end=" ")
print()
for i in r2:
    print(i,end=" ")
