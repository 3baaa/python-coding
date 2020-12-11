'''
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()
print(stack)
print(stack[::-1])

from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)

def factorial_i(n):
  result = 1
  for i in range(1,n+1):
    result *= i
  return result

def factorial_r(n):
  if n<=1:
    return 1
  return n*factorial_r(n-1)

print(factorial_i(5))
print(factorial_r(5))

INF=9999999

g=[
  [0,7,5],
  [7,0,INF],
  [5,INF,0]
]

print(g)

g=[[] for _ in range(3)]
g[0].append((1,7))
g[0].append((2,5))

g[1].append((0,7))

g[2].append((0,5))

print(g)

def d(g,v,visited):
  visited[v] = True
  print(v,end=' ')
  for i in g[v]:
    if not visited[i]:
      d(g,i,visited)

g=[
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7],
]

visited = [False]*9

d(g,1,visited)

from collections import deque

def b(g,s,visited):
  queue = deque([s])
  visited[s] = True
  while queue:
    v = queue.popleft()
    print(v,end=' ')
    for i in g[v]:
      if not visited[i]:
        queue.append(i)
        visited[i]=True

g=[
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7],
]

visited = [False] * 9

b(g,1,visited)

#### dfs/bfs 문제 1 (음료수 얼려 먹기) ####
##내가쓴 코드##
from collections import deque

#n,m=map(int,input().split())
visited=[False*(4+1) for _ in range(5)]
count=0

g=[
  [],
  [0,0,1,1,0],
  [0,0,0,1,1],
  [1,1,1,1,1],
  [0,0,0,0,0]
]

def b(a):
  for i,v in enumerate(a[1:]):
    for j in v:
      if i>=2
  pass

def zz(g):
  for i,v in enumerate(g[1:]):
    for j,v in enumerate(v):
      if v==0:
        a[i+1].append(j)
a=[[],[],[],[],[]]

zz(g)

b(a,visited)
print()
print()
for i in a:
  print(i,end=' ')
  print()

##답##
def dfs(x,y):
  if x<=-1 or x>=n or y<=-1 or y>=m:
    return False
  if graph[x][y]==0:
    graph[x][y]=1
    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x+1,y)
    dfs(x,y+1)
    return True
  return False

n,m=map(int,input().split())

graph=[]
for i in range(n):
  graph.append(list(map(int,input())))

result = 0
for i in range(n):
  for j in range(m):
    if dfs(i,j)==True:
      result+=1

print(result)
'''