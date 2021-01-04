####위상 정렬####
'''
from collections import deque

v,e=map(int,input().split())
indegree=[0]*(v+1)
graph=[[] for i in range(v+1)]

for _ in range(e):
  a,b=map(int,input().split())
  graph[a].append(b)
  indegree[b]+=1

def topology_sort():
  result = []
  q=deque()

  for i in range(1,v+1):
    if indegree[i]==0:
      q.append(i)
  

  while q:
    now = q.popleft()
    result.append(now)
    
    for i in graph[now]:
      indegree[i]-=1
      if indegree[i]==0:
        q.append(i)
  
  for i in result:
    print(i,end=' ')

topology_sort()

##팀 결성(서로소집합,크루스칼,위상정렬 문제1)##
#내가쓴 코드#
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
  a,b,c=map(int,input().split())
  if a==0:
    union_parent(parent,b,c)
  else:
    r1=find_parent(parent,b)
    r2=find_parent(parent,c)
    if r1==r2:
      r.append('YES')
    else:
      r.append('NO')

for i in r:
  print(i)

##도시 분할 계획(서로소집합,크루스칼,위상정렬 문제2)##
#내가쓴 코드#
#(## no ##=코드를 잘못쓴부분 , ## yes ##=답보고 맞게쓴 부분)#
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
es=[]
r=0

for i in range(n+1):
  parent[i]=i

for i in range(m):
  a,b,c=map(int,input().split())
  es.append((c,a,b))

es.sort()
last=0 ## yes ##
#z,a,b=es[len(es)-1] ## no ##

for e in es:
  c,a,b=e
  if find_parent(parent,a)!=find_parent(parent,b):
    union_parent(parent,a,b)
    r+=c
    last=c ## yes ##

print(r-last)
#print(r-z) ## no ##

##커리큘럼(서로소집합,크루스칼,위상정렬 문제3)##
#내가쓴 코드#
from collections import deque

n=int(input())
t=[0]
r=[]
indegree=[0]*(n+1)
graph=[[] for _ in range(n+1)]
for i in range(1,n+1):
  array=list(map(int,input().split()))
  t.append(array[0])
  for j in array[1:-1]:
    graph[j].append(i)
    indegree[i]+=1

q=deque()

for i in range(1,n+1):
  if indegree[i]==0:
    q.append(i)

tr=t.copy()

while q:
  now=q.popleft()
  r.append(now)
  m=0
  for i in graph[now]:
    indegree[i]-=1
    if tr[i]<tr[now]+t[i]:
      tr[i]=tr[now]+t[i]
    if indegree[i]==0:
      q.append(i)

for i in tr[1:]:
  print(i)
'''