##아기 상어##
'''
#내가쓴 코드#
#(결과값이 나온다)#
from collections import deque

def check_fish(size,fish):
    for i in range(N):
        for j in range(N):
            if 0<a[i][j]<size:
                fish.append([i,j])
    if fish:
        fish.sort()
        return True
    else:
        return False

def b(s):
    size=2
    q=deque([s])
    c=0
    r=0
    while q:
        fish=[]
        x,y=q.popleft()
        r_fish=check_fish(size,fish)
        if not r_fish:
            continue
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>-1 and nx<N and ny>-1 and ny<N and a[nx][ny]<=size:
                if r_fish:
                    if [nx,ny] in fish:
                        if fish[0]==[nx,ny]:
                            fish.pop(0)
                            a[nx][ny]=0
                            c+=1
                            r=[nx,ny]
                            q=deque([])
                            
                    if c==size:
                        size+=1
                        c=0
                    q.append([nx,ny])
                    time[nx][ny]=max(time[nx][ny],time[x][y]+1)
                
                else:
                    return 0
    return r
                    
N=int(input())
a=[]
s=0
dx=[-1,1,0,0]
dy=[0,0,-1,1]
time=[[0]*N for _ in range(N)]

for i in range(N):
    t=list(map(int,input().split()))
    for j in range(N):
        if t[j]==9:
            s=[i,j]
            t[j]=0
    a.append(t)
r=b(s)
if r!=0:
    x,y=r
    print(time[x][y])
else:
    print(r)
'''
