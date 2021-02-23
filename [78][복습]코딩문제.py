##인구 이동##
'''
#내가쓴 코드#
#(결과값이 나온다)#
from collections import deque

def zz(s):
    q=deque([s])
    t=[]
    r=0
    z=[[False]*n for _ in range(n)]
    while q:
        x,y=q.popleft()
        r+=a[x][y]
        t.append([x,y])
        z[x][y]=True
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if -1<nx<n and -1<ny<n:
                if not z[nx][ny] and L<=abs(a[x][y]-a[nx][ny])<=R:
                    q.append([nx,ny])
    for i in t:
        a[i[0]][i[1]]=r//len(t)
    return len(t)

n,L,R=map(int,input().split())
a=[]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
for i in range(n):
    a.append(list(map(int,input().split())))

result=0
for i in range(n):
    for j in range(n):
        if zz([i,j])>1:
            result+=1
print(result)

##블록 이동하기##
#내가쓴 코드#
#(결과값은 나오나 정확성 0.0)#
from collections import deque

def zz(a,s,board):
    q=deque([s])
    n=len(board)
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    t=[]
    while q:
        n1=q.popleft()
        if n1[0]==[n-1,n-1] or n1[1]==[n-1,n-1]:
            return n1[2]
        x1,y1=n1[0]
        x2,y2=n1[1]
        z=n1[2]
        for i in range(4):
            nx1,nx2=x1+dx[i],x2+dx[i]
            ny1,ny2=y1+dy[i],y2+dy[i]
            if -1<nx1<n and -1<ny1<n and -1<nx2<n and -1<ny2<n:
                if board[nx1][ny1]!=1 and board[nx2][ny2]!=1:
                    a[nx1][ny1]=z+1
                    a[nx2][ny2]=z+1
                    q.append([[nx1,ny1],[nx2,ny2],z+1])
        if -1<x1+1<n and -1<x2+1<n and a[x1+1][y1]!=1 and a[x2+1][y1]!=1:
            q.append([[x1,y1],[x1+1,y1],z+1])
            q.append([[x2,y2],[x2+1,y2],z+1])
        if -1<x1-1<n and -1<x2-1<n and a[x1-1][y1]!=1 and a[x2-1][y1]!=1:
            q.append([[x1,y1],[x1-1,y1],z+1])
            q.append([[x2,y2],[x2-1,y2],z+1])
        if -1<y1+1<n and -1<y2+1<n and a[x1][y1+1]!=1 and a[x2][y2+1]!=1:
            q.append([[x1,y1],[x1,y1+1],z+1])
            q.append([[x2,y2],[x2,y2+1],z+1])
        if -1<y1-1<n and -1<y2-1<n and a[x1][y1-1]!=1 and a[x2][y2-1]!=1:
            q.append([[x1,y1],[x1,y1-1],z+1])
            q.append([[x2,y2],[x2,y2-1],z+1])

def solution(board):
    answer = 0
    a=[[0]*len(board) for _ in range(len(board))]
    answer=zz(a,[[0,0],[0,1],0],board)
    return answer
'''
