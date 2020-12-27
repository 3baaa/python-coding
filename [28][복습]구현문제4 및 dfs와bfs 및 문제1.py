##구현 문제4(게임 개발)##
'''
#답#
n,m=map(int,input().split())

d=[[0]*m for _ in range(n)]
x,y,direction=map(int,input().split())
d[x][y]=1

array=[]
for i in range(n):
  array.append(list(map(int,input().split())))

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def turn_left():
  global direction
  direction-=1
  if  direction==-1:
    direction=3

count=1
turn_time=0
while True:
  turn_left()
  nx=x+dx[direction]
  ny=y+dy[direction]

  if d[nx][ny] == 0 and array[nx][ny] == 0:
    print(nx,ny)
    d[nx][ny]=1
    x=nx
    y=ny
    count+=1
    turn_time=0
    continue
  else:
    turn_time+=1
  if turn_time==4:
    nx=x-dx[direction]
    ny=y-dy[direction]
    if array[nx][ny]==0:
      x=nx
      y=ny
    else:
      break
    turn_time=0

print(count)

####dfs/bfs####
##dfs##
def dfs(graph,v,visited):
  visited[v]=True
  print(v,end=' ')
  for i in graph[v]:
    if not visited[i]:
      dfs(graph,i,visited)

graph=[
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

visited=[False]*9

dfs(graph,1,visited)

##bfs##
from collections import deque

def bfs(graph,start,visited):
  queue=deque([start])
  visited[start]=True
  while queue:
    v=queue.popleft()
    print(v,end=' ')
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i]=True

graph=[
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

visited=[False]*9

bfs(graph,1,visited)

##음료수 얼려먹기(dfs/bfs문제1)##
#내가쓴 코드#
from collections import deque

n,m=map(int,input().split())
a=[]
c=0
dx=[-1,1,0,0]
dy=[0,0,-1,1]
for i in range(n):
  a.append(list(map(int,input())))

def b(z):
  x,y=z[0],z[1]
  if a[x][y]==0:
    queue=deque([z])
    a[x][y]=1
    while queue:
      x,y=queue.popleft()
      for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx>=0 and nx<n and ny>=0 and ny<m:
          if a[nx][ny]==0:
            a[nx][ny]=1
            queue.append((nx,ny))
    return 1
  else:
    return -1

for i in range(n):
  for j in range(m):
    r=b([i,j])
    if r==1:
      c+=1

print(c)
'''
