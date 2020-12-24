####크루스칼,위상정렬 문제3(커리큘럼)####
'''
##내가쓴 소스코드##
from collections import deque

n=int(input())
indegree=[0]*(n+1)
g=[[] for i in range(n+1)]
t=[0]*(n+1)
tr=[0]*(n+1)

for i in range(1,n+1):
  a=list(map(int,input().split()))
  t[i]=a[0]
  tr[i]=a[0]
  if a[1:len(a)-1]:
    indegree[i]+=len(a[1:len(a)-1])
    for j in a[1:len(a)-1]:
      g[j].append(i)

def topology_sort():
  q=deque()

  for i in range(1,n+1):
    if indegree[i]==0:
      q.append(i)

  while q:
    now=q.popleft()
    for i in g[now]:
      indegree[i]-=1
      tr[i]=t[i]+tr[now]
      if indegree[i]==0:
        q.append(i)
  for i in tr:
    print(i,end=' ')

topology_sort()

##답##
from collections import deque
import copy

v=int(input())
indegree=[0]*(v+1)
graph=[[] for i in range(v+1)]
time=[0]*(v+1)

for i in range(1,v+1):
  data=list(map(int,input().split()))
  time[i]=data[0]
  for x in data[1:-1]:
    indegree[i]+=1
    graph[x].append(i)

def topology_sort():
  result=copy.deepcopy(time)
  q=deque()

  for i in range(1,v+1):
    if indegree[i]==0:
      q.append(i)
  
  while q:
    now=q.popleft()
    for i in graph[now]:
      result[i]=max(result[i],result[now]+time[i])
      indegree[i]-=1
      if indegree[i]==0:
        q.append(i)
  
  for i in range(1,v+1):
    print(result[i])

topology_sort()
'''