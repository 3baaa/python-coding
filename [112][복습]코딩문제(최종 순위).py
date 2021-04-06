##최종 순위
#내가쓴 코드(잘못쓴 코드)
'''
from collections import deque

def z(a,c,r):
    q=deque()
    for i in range(1,n+1):
        if c[i]==0:
            q.append(i)

    while q:
        t=q.popleft()
        r.append(t)
        for i in b[i]:
            c[i]-=1
            if c[i]==0:
                q.append(i)

for _ in range(int(input())):
    n=int(input())
    b=[[] for _ in range(n+1)]
    c=[0]*(n+1)
    a=list(map(int,input().split()))
    for i in range(int(input())):
        n1,n2=map(int,intput().split())
    p=a[0]
    for i in a[1:]:
        b[p].append(i)
        c[i]+=1
    r=[]
    z(a,c,r)

    print(r)
    for i in r:
        print(i,end=" ")
'''
#답#
from collections import deque

for tc in range(int(input())):
    n=int(input())
    indegree=[0]*(n+1)
    graph=[[False] * (n+1) for i in range(n+1)]
    data=list(map(int,input().split()))
    for i in range(n):
        for j in range(i+1,n):
            graph[data[i]][data[j]]=True
            indegree[data[j]]+=1
    m=int(input())
    for i in range(m):
        a,b=map(int,input().split())
        if graph[a][b]:
            graph[a][b]=False
            graph[b][a]=True
            indegree[a]+=1
            indegree[b]-=1
        else:
            graph[a][b]=True
            graph[b][a]=False
            indegree[a]-=1
            indegree[b]+=1

    result=[]
    q=deque()

    for i in range(1,n+1):
        if indegree[i]==0:
            q.append(i)

    certain = True
    cycle=False

    for i in range(n):
        if len(q)==0:
            cycle=True
            break

        if len(q)>=2:
            certain=False
            break

        now=q.popleft()
        result.append(now)
        for j in range(1,n+1):
            if graph[now][j]:
                indegree[j]-=1
                if indegree[j]==0:
                    q.append(j)

    if cycle:
        print("IMPOSSIBLE")
    elif not certain:
        print("?")
    else:
        for i in result:
            print(i,end=" ")
        print()
