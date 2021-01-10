##뱀##
'''
#내가쓴 코드#
#(결과값이 나온다)#
from collections import deque

n=int(input())
m=[[0]*n for _ in range(n)]
k=int(input())
for i in range(k):
  a,b=map(int,input().split())
  m[a-1][b-1]=2

L=int(input())
D=deque()
for i in range(L):
  X,C=input().split()
  D.append((int(X),C))

dx=[-1,0,1,0]
dy=[0,-1,0,1]

count=0

bem=deque([[0,0]])
x,y=bem[0]
t=3
while True:#-1<x<n and -1<y<n:
  count+=1
  x+=dx[t]
  y+=dy[t]
  if 0>x or x>=n or 0>y or y>=n:
    break
  if bem.count((x,y)):
    break
  bem.appendleft((x,y))
  if len(bem)>=2 and m[x][y]!=2:
    bem.pop()
  if D and count==D[0][0]:
    d=D.popleft()[1]
    if d=='D':
      t-=1
      if t==-1:
        t=3
    else:
      t+=1
      if t==4:
        t=1
  x,y=bem[0]

print(count)

##기둥과 보 설치##
#내가쓴 코드#
#(정확성 4.8)#
def solution(n, build_frame):
    answer = []
    m=[[5]*(n+1) for _ in range(n+1)]
    for i,v in enumerate(build_frame,start=1):
        y,x,a,b=v
        if b==1:
            if a==0:
                if x==0 or m[x][y]==1 or m[x][y]==0:
                    m[x][y]=0
                    m[x+1][y]=0
                    answer.append([y,x,0])
            else:
                if m[x][y]==0:
                    m[x][y]=2
                    m[x][y+1]=1
                    answer.append([y,x,1])
                elif m[x][y]==1 and m[x][y+1]==1:
                    m[x][y]=3
                    m[x][y+1]=3
                    answer.append([y,x,1])
                elif m[x][y+1]==0:
                    if m[x][y]==1:
                        m[x][y]=3
                    else:
                        m[x][y]=1
                    m[x][y+1]=2
                    answer.append([y,x,1])
                elif m[x][y]==2:
                    m[x][y+1]=1
                    answer.append([y,x,1])
        else:
            if a==0:
                if m[x+1][y-1]==3 and m[x+1][y+1]==3:
                    m[x][y]=5
                    if m[x+1][y]==2:
                        m[x+1][y]=3
                    answer.remove([y,x,0])
            else:
                if m[x][y]==2:
                    m[x][y]=0
                    m[x][y+1]=5
                    answer.remove([y,x,1])
                elif m[x][y]==3 and m[x][y+1]!=3:
                    m[x][y]=1
                    m[x][y+1]=1
                    answer.remove([y,x,1])
    answer.sort()
    return answer

#답#
def possible(answer):
    for x,y,stuff in answer:
        if stuff==0:
            if y==0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer:
                continue
            return False
        elif stuff==1:
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x,y,stuff,operate = frame
        if operate == 0:
            answer.remove([x,y,stuff])
            if not possible(answer):
                answer.append([x,y,stuff])
        if operate == 1:
            answer.append([x,y,stuff])
            if not possible(answer):
                answer.remove([x,y,stuff])
    return sorted(answer)
'''