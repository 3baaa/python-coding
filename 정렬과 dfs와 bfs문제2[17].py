####bfs/dfs 문제 2 (미로 탈출)####
'''
from collections import deque

n,m=map(int,input().split())
graph=[]

for i in range(n):
  graph.append(list(map(int,input())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
  queue=deque()
  queue.append((x,y))
  
  while queue:
    x,y = queue.popleft()
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
for i in graph:
  for j in i:
    print(j,end=' ')
  print()

##내가쓴 코드##
n,m=map(int,input().split())
a=[]

for i in range(n):
  a.append(list(map(int,input())))

def d(x,y,n1,n2):
  if x<0 or y<0 or x>=n or y>=m:
    return
  if a[x][y]==0:
    return
  if a[x][y]==1:
    if x!=0 or y!=0:
      a[x][y]=a[n1][n2]+1
    d(x-1,y,x,y)
    d(x+1,y,x,y)
    d(x,y-1,x,y)
    d(x,y+1,x,y)
  return a[n-1][m-1]

print(d(0,0,0,0))
#### 정렬 ####
#선택정렬#
a = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(a)):
  min_i=i
  for j in range(i+1,len(a)):
    if a[min_i]>a[j]:
      min_i=j
  a[i],a[min_i]=a[min_i],a[i]

print(a)

#삽입정렬#
a = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(a)):
  for j in range(i,0,-1):
    if a[j]<a[j-1]:
      a[j],a[j-1]=a[j-1],a[j]
    else:
      break

print(a)

#퀵정렬1#
a=[5,7,9,0,3,1,6,2,4,8]

def quick_sort(a,s,e):
  if s>=e:
    return
  pivot=s
  left=s+1
  right=e
  while left<=right:
    while left <= e and a[left] <= a[pivot]:
      left+=1
    while right > s and a[right] >= a[pivot]:
      right-=1
    if left>right:
      a[right],a[pivot]=a[pivot],a[right]
    else:
      a[left],a[right]=a[right],a[left]
  
  quick_sort(a,s,right-1)
  quick_sort(a,right+1,e)

quick_sort(a,0,len(a)-1)
print(a)

#퀵정렬2#
a=[5,7,9,0,3,1,6,2,4,8]

def quick_sort(a):
  if len(a)<=1:
    return a
  
  pivot = a[0]
  tail=a[1:]

  left_side=[x for x in tail if x<=pivot]
  right_side=[x for x in tail if x>pivot]

  return quick_sort(left_side)+[pivot]+quick_sort(right_side)

print(quick_sort(a))

#계수정렬#
a=[7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

count=[0]*(max(a)+1)

for i in range(len(a)):
  count[a[i]]+=1

for i in range(len(count)):
  for j in range(count[i]):
    print(i,end=' ')

a = [7,5,9,0,3,1,6,2,4,8]

result=sorted(a)
print(result)
a.sort()
print(a)

a=[('바나나',2),('사과',5),('당근',3)]

def setting(data):
  return data[1]

result = sorted(a,key=setting)
print(result)
'''