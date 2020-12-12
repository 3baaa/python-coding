##dfs와 bfs문제##
#음료수 얼려먹기#
'''
def d(a,i,j):
  if j<0 or j>=m or i<0 or i>=n:
    return False
  if a[i][j]==0:
    a[i][j]=1
    d(a,i-1,j)
    d(a,i+1,j)
    d(a,i,j-1)
    d(a,i,j+1)
    return True
  return False

n,m=map(int,input().split())
a=[]
for i in range(n):
  a.append(list(map(int,input())))

count=0

for i in range(n):
  for j in range(m):
    if d(a,i,j)==True:
      count+=1

print(count)

#내가쓴 코드#
from collections import deque

def b(i,j):
  queue=deque()
  c=False
  queue.append([i,j])
  while queue:
    x,y=queue.popleft()
    if a[x][y]==0:
      c=True
      a[x][y]=1
      if x<n-1:
        queue.append([x+1,y])
      if x>=1:
        queue.append([x-1,y])
      if y<m-1:
        queue.append([x,y+1])
      if y>=1:
        queue.append([x,y-1])
  return c
      

n,m=map(int,input().split())
a=[]
for i in range(n):
 a.append(list(map(int,input())))

count=0

for i in range(n):
  for j in range(m):
    if b(i,j) == True:
      count+=1

print(count)

##dfs/bfs 문제 2 (미로탈출문제)##
#내가쓴 코드#
from collections import deque

dx=[0,0,1,-1]
dy=[1,-1,0,0]
def b(a,s):
  queue=deque()
  queue.append(s)
  count=1
  while queue:
    x,y=queue.popleft()
    a[x][y]=count
    if a[x][y]==0:
      continue
    if x==n-1 and y==m-1:
      return 
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if 0<=nx<n and 0<=ny<m and a[nx][ny]==1:
        queue.append([nx,ny])
        count+=1
  return count

n,m=map(int,input().split())
a=[]
count=0

for i in range(n):
 a.append(list(map(int,input())))

count=b(a,[1,1])

print('count=',count)

##답##
from collections import deque

n,m=map(int,input().split())

graph=[]
for i in range(n):
  graph.append(list(map(int,input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
  queue = deque()
  queue.append((x,y))
  while queue:
    x,y=queue.popleft()

    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      
      if nx<0 or ny<0 or nx>=n or ny>=m:
        continue
      
      if graph[nx][ny]==0:
        continue
      
      if graph[nx][ny]==1:
        graph[nx][ny]=graph[x][y]+1
        queue.append((nx,ny))
  
  return graph[n-1][m-1]

print(bfs(0,0))
'''