##연구소##
'''
#답#
from copy import deepcopy
from itertools import combinations
from collections import deque

data=[
  [2,0,0,0,1,1,0],
  [0,0,1,0,1,2,0],
  [0,1,1,0,1,0,0],
  [0,1,0,0,0,0,0],
  [0,0,0,0,0,1,1],
  [0,1,0,0,0,0,0],
  [0,1,0,0,0,0,0]
  ]
n,m=7,7
empty_wall,virus=[],[]
dx=[-1,0,1,0]
dy=[0,1,0,-1]

for i in range(n):
  for j in range(m):
    if data[i][j]==0:
      empty_wall.append((i,j))
    elif data[i][j]==2:
      virus.append((i,j))

def count_zero(maps):
  count=0
  for i in range(n):
    for j in range(m):
      if maps[i][j]==0:
        count+=1
  return count

def bfs(start,candidate):
  maps=deepcopy(data)
  
  for i,j in candidate:
    maps[i][j]=1

  q=deque(start)
  while q:
    y,x=q.popleft()
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if 0<= ny<n and 0<=nx<m and maps[ny][nx]==0:
        maps[ny][nx]=2
        q.append((ny,nx))
  return count_zero(maps)

candidates=list(combinations(empty_wall,3))
max_value=0
for i in candidates:
  result=bfs(virus,i)
  max_value=max(max_value,result)

print(max_value)
'''