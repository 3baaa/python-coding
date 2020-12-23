####최소신장트리####
'''
##크루스칼##
def find_parent(parent,x):
  if parent[x] != x:
    parent[x]=find_parent(parent,parent[x])
  return parent[x]

def union_parent(parent,a,b):
  a=find_parent(parent,a)
  b=find_parent(parent,b)
  if a<b:
    parent[b]=a
  else:
    parent[a]=b

v,e=map(int,input().split())
parent=[0]*(v+1)

edges=[]
result=0

for i in range(1,v+1):
  parent[i]=i

for _ in range(e):
  a,b,cost=map(int,input().split())
  edges.append((cost,a,b))

edges.sort()

for edge in edges:
  cost,a,b=edge
  if find_parent(parent,a) != find_parent(parent,b):
    union_parent(parent,a,b)
    result+=cost

print(result)

####위상정렬####
from collections import deque

v,e = map(int,input().split())
indegree=[0]*(v+1)
graph=[[] for i in range(v+1)]

for _ in range(e):
  a,b=map(int,input().split())
  graph[a].append(b)
  indegree[b]+=1

def topology_sort():
  result=[]
  q=deque()
  
  for i in range(1,v+1):
    if indegree[i]==0:
      q.append(i)

  while q:
    now=q.popleft()
    result.append(now)
    
    for i in graph[now]:
      indegree[i]-=1
      
      if indegree[i]==0:
        q.append(i)
  for i in result:
    print(i,end=' ')

topology_sort()

####문제 1 (팀결성)####
##내가쓴 코드##
def find_parent(parent,x):
  if parent[x]!=x:
    parent[x]=find_parent(parent,parent[x])
  return parent[x]

def union_parent(parent,a,b):
  a=find_parent(parent,a)
  b=find_parent(parent,b)
  if a<b:
    parent[b]=a
  else:
    parent[a]=b
  
n,m=map(int,input().split())
parent=[0]*(n+1)
r=[]

for i in range(1,n+1):
  parent[i]=i

for i in range(m):
  z,a,b=map(int,input().split())
  if z==0:
    union_parent(parent,a,b)
  else:
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a==b:
      r.append('YES')
    else:
      r.append('NO')

for i in r:
  print(i)

##문제2(도시 분할 계획)##
#답#
def find_parent(parent,x):
  if parent[x]!=x:
    parent[x]=find_parent(parent,parent[x])
  return parent[x]

def union_parent(parent,a,b):
  a=find_parent(parent,a)
  b=find_parent(parent,b)
  if a<b:
    parent[b]=a
  else:
    parent[a]=b

v,e=map(int,input().split())

parent=[0]*(v+1)

edges=[]
result=0

for i in range(1,v+1):
  parent[i]=i

for _ in range(e):
  a,b,cost=map(int,input().split())
  edges.append((cost,a,b))

edges.sort()
last=0

for edge in edges:
  cost,a,b=edge
  if find_parent(parent,a)!=find_parent(parent,b):
    union_parent(parent,a,b)
    result+=cost
    last=cost

print(result-last)
'''
