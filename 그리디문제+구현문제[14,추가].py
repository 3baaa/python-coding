#그리디#
'''
#### 그리디 문제1 답(2) ####
n,m,k=map(int,input().split())
data = list(map(int,input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

count = int(m/(k+1))*k
count+=m%(k+1)

result = 0
result += (count)*first
result += (m-count)*second

print(result)

#### 그리디 문제2 (숫자 카드 게임) ####
## 내가쓴 코드 ##
n,m=map(int,input().split())
a=[]
max=0
for i in range(n):
  a.append(list(map(int,input().split())))
for i in a:
  if max<min(i):
    max=min(i)
print(max)

#### 그리디 문제 3 (1이 될 때까지) ####
## 내가쓴 코드 ##
n,k=map(int,input().split())
count=0
while n!=1:
  if n%k==0:
    n//=k
  else:
    n-=1
  count+=1
print(count)

#### 구현 문제 1 (상하좌우) ####
## 내가쓴 코드 ##
n=int(input())
move=input().split()
person=[1,1]

for i in move:
  if i=='R':
    if person[1]>n:
      continue
    person[1]+=1    
  elif i == 'L':
    if person[1]==1:
      continue
    person[1]-=1
  elif i == 'U':
    if person[0]==1:
      continue
    person[0]-=1
  elif i == 'D':
    if person[0]==n:
      continue
    person[0]+=1
print(person[0],person[1])

##답##
n=int(input())
x,y=1,1
plans=input().split()

dx=[0,0,-1,1]
dy=[-1,1,0,0]
move_types=['L','R','U','D']

for plan in plans:
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x+dx[i]
      ny = y+dy[i]
  
  if nx < 1 or ny < 1 or nx > n or ny > n :
    continue
  x,y=nx,ny

print(x,y)

#### 구현 문제 2 (시각) ####
##답##
h = int(input())

count=0
for i in range(h+1):
  for j in range(60):
    for k in range(60):
      if '3' in str(i) + str(j) + str(k):
        count+=1

print(count)

#### 구현 문제 3 (왕실의 나이트) ####
##내가쓴 코드##
n=input()
l=[[1,-2],[-1,-2]]
r=[[1,2],[-1,2]]
d=[[-2,-1],[-2,1]]
u=[[2,-1],[2,1]]
a=[l,r,d,u]

count=0
for i in a:
  for j in i:
    x=int(n[1])+j[0]
    y=ord(n[0])+j[1]
    if x>8 or x<1 or y<ord('a') or y>ord('h'):
      continue
    count+=1
print(count)

##답##
input_data=input()
row=int(input_data[1])
column=int(ord(input_data[0])) - int(ord('a')) + 1

steps=[(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

result=0
for step in steps:
  next_row=row+step[0]
  next_column=column+step[1]
  if next_row>=1 and next_row<=8 and next_column>=1 and next_column<=8:
    result+=1
print(result)

#### 구현 문제 4 (게임 개발) ####
##내가쓴 코드##
n,m=map(int,input().split())
a,b,d=map(int,input().split())
arr=[]
#0321
move=[(-1,0),(0,-1),(1,0),(0,1)]
#move={0:(-1,0),3:(0,-1),2:(1,0),1:(0,1)}
#move={0:(-1,0),1:(0,1),2:(1,0),3:(0,-1)}
for i in range(n):
  for j in range(m):
    arr.append(list(map(int,input().split())))
while True:
  for i in range(0,4):
    ta=a+move[d+i%3][0]
    tb=a+move[d+i%3][1]
    if arr[ta][tb]==0:
      d=
      arr[a][b]=2
      a=ta
      b=tb
      break
##답##
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
  direction -= 1
  if direction == -1:
    direction = 3

count = 1
turn_time = 0
while True:
  turn_left()
  nx = x + dx[direction]
  ny = y + dy[direction]
  if d[nx][ny]==0 and array[nx][ny]==0:
    d[nx][ny]=1
    x=nx
    y=ny
    count+=1
    turn_time = 0
    continue
  else:
    turn_time+=1
  if turn_time == 4:
    nx = x - dx[direction]
    ny = y - dy[direction]
    if array[nx][ny]==0:
      x=nx
      y=ny
    else:
      break
    turn_time=0

print(count)
'''