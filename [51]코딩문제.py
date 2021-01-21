##감시 피하기##
'''
#내가쓴 코드#
#(결과값이 다나온다)#
import copy

def d(z):
  if z==3:
    map=copy.deepcopy(a)
    for i,j in p:
      map[i][j]='O'
    for xx,yy in t:
      for k in range(4):
        x1,y1=xx,yy
        while True:
          nx=x1+dx[k]
          ny=y1+dy[k]
          if nx>=0 and nx<n and ny>=0 and ny<n:
            x1,y1=nx,ny
            if map[nx][ny]=='S':
              return False
            elif map[nx][ny]=='O':
              break
          else:
            break
    return True

  for i,j in x:
    if not v[i][j]:
      p.append((i,j))
      v[i][j]=True
      if d(z+1):
        return True
      v[i][j]=False
      p.pop()

n=int(input())
a=[]
x=[]
t=[]
p=[]
result=False
v=[ [False]*n for _ in range(n) ]
dx=[-1,0,1,0]
dy=[0,1,0,-1]

for i in range(n):
  b=list(input().split())
  a.append(b)
  for j,val in enumerate(b):
    if val=='X':
      x.append((i,j))
    elif val=='T':
      t.append((i,j))

result=d(0)
if not result:
  print('NO')
else:
  print('YES')

##인구이동##
#내가쓴 코드#
#(몇개만 결과값이 나온다)#
from collections import deque

def b():
  s=(0,0)
  q=deque([s])
  c=0
  while q:
    x,y=q.popleft()
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if nx>=0 and nx<n and ny>=0 and ny<n and not v[nx][ny]:
        t=abs(a[nx][ny]-a[x][y])
        v[nx][ny]=True
        if l<=t<=r:
          data.append([abs(t-aver),(x,y),(nx,ny)])
        q.append((nx,ny))
    if data:
      data.sort()
      x,y=data[0][1]
      nx,ny=data[0][2]
      aver2=(a[x][y]+a[nx][ny])//2
      a[x][y],a[nx][ny]=aver2,aver2
      c+=1
      data.clear()

  return c

n,l,r=map(int,input().split())
aver=(l+r)//2
a=[]
dx=[-1,0,1,0]
dy=[0,1,0,-1]
v=[[False]*n for _ in range(n)]
data=[]
for i in range(n):
  a.append(list(map(int,input().split())))

print(b())

##인구이동##
#답#
from collections import deque

n,l,r=map(int,input().split())

a=[]

for _ in range(n):
  a.append(list(map(int,input().split())))

dx=[-1,0,1,0]
dy=[0,-1,0,1]

result=0

def process(x,y,idx):
  united=[]
  united.append((x,y))
  q=deque()
  q.append((x,y))
  union[x][y]=idx
  summary=a[x][y]
  count=1
  while q:
    x,y=q.popleft()
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if 0<=nx<n and 0<=ny<n and union[nx][ny]==-1:
        if l<=abs(a[nx][ny]-a[x][y])<=r:
          q.append((nx,ny))
          union[nx][ny]=idx
          summary+=a[nx][ny]
          count+=1
          united.append((nx,ny))
  for i,j in united:
    a[i][j]=summary//count
  return count

total_count=0

while True:
  union=[[-1]*n for _ in range(n)]
  index=0
  
  for i in range(n):
    for j in range(n):
      if union[i][j]==-1:
        process(i,j,index)
        index+=1
  if index==n*n:
    break
  total_count+=1

print(total_count)
'''