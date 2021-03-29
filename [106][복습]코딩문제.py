##화성 탐사
#내가쓴 코드
#결과값이 나온다
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def zz(a,r):
    q=deque([(0,0)])
    r[0][0]=a[0][0]
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and r[nx][ny]>r[x][y]+a[nx][ny]:
                q.append((nx,ny))
                r[nx][ny]=r[x][y]+a[nx][ny]
                
t=int(input())
for _ in range(t):
    n=int(input())
    a=[]
    r=[[int(1e9)]*n for _ in range(n)]
    
    for i in range(n):
        a.append(list(map(int,input().split())))
    zz(a,r)
    print(r[n-1][n-1])
