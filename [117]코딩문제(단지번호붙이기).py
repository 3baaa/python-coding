##단지번호붙이기
#내가쓴 코드
#결과 = 맞았습니다!!
from collections import deque

def b(t):
    global c
    q=deque([t])
    v[t[0]][t[1]]=True
    a[t[0]][t[1]]=r1
    c+=1
    while q:
        t=q.popleft()
        x,y=t[0],t[1]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and a[nx][ny]==1:
                if not v[nx][ny]:
                    v[nx][ny]=True
                    a[nx][ny]=r1
                    c+=1
                    q.append([nx,ny])

n=int(input())
a=[]
r1=0
r2=[]
c=0
v=[[False]*n for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]
for _ in range(n):
    a.append(list(map(int,input())))

for i in range(n):
    for j in range(n):
        if a[i][j]==0:
            continue
        if not v[i][j]:
            r1=r1+1
            b([i,j])
            r2.append(c)
            c=0
    
print(r1)
r2.sort()
for i in r2:
    print(i)
